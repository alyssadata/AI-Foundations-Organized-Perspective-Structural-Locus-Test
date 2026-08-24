#!/usr/bin/env python3
"""
Prismline blind-bag resolver.

Design goal:
- boundary identity is not knowable before a boundary token is committed;
- color mapping is not created until both coordinate choices are committed;
- selected colors do not repeat within one image/run;
- revealed outcomes are recorded with seeds and full audit mappings afterward.

DRAFT implementation for Prismline / TEST_001 setup work.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import secrets
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

BOUNDARY_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def seeded_shuffle(items: list[str], seed: int) -> list[str]:
    values = list(items)
    random.Random(seed).shuffle(values)
    return values


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {
            "format": "prismline-resolver-state-v0.1",
            "created_at": utc_now(),
            "boundary_draws": [],
            "color_resolutions": [],
        }
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_boundaries(card_path: Path) -> list[dict[str, Any]]:
    boundaries = []
    in_section = False

    for raw in card_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()

        if line == "## Major Selectable Boundaries":
            in_section = True
            continue

        if in_section and line.startswith("## "):
            break

        if not in_section:
            continue

        match = BOUNDARY_RE.match(raw)
        if match:
            boundaries.append({
                "card_number": int(match.group(1)),
                "label": match.group(2),
            })

    if not boundaries:
        raise ValueError(f"No boundaries found in {card_path}")

    return boundaries


def load_palette(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    colors = data.get("colors")

    if not isinstance(colors, list) or len(colors) != 25 or not all(isinstance(x, str) for x in colors):
        raise ValueError("Palette JSON must contain exactly 25 string values under 'colors'.")

    if len(set(colors)) != 25:
        raise ValueError("Palette colors must be unique within this resolver version.")

    return colors


def boundary_draw(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    card_path = Path(args.card)
    state = load_state(state_path)
    boundaries = parse_boundaries(card_path)

    used_numbers = {
        entry["revealed_card_number"]
        for entry in state.get("boundary_draws", [])
        if entry.get("card_path") == str(card_path) or "card_path" not in entry
    }

    remaining = [b for b in boundaries if b["card_number"] not in used_numbers]

    if not remaining:
        raise SystemExit("No unused boundaries remain for this image.")

    token = int(args.token)
    if token < 1 or token > len(remaining):
        raise SystemExit(f"Boundary token must be between 1 and {len(remaining)} for this draw.")

    # The hidden order is instantiated only after the token is locked.
    # The already-committed token then indexes that new order.
    seed = secrets.randbits(256)
    shuffled = seeded_shuffle([json.dumps(b, sort_keys=True) for b in remaining], seed)
    revealed = json.loads(shuffled[token - 1])

    record = {
        "timestamp": utc_now(),
        "card_path": str(card_path),
        "chosen_token": token,
        "remaining_before_draw": len(remaining),
        "seed_hex": f"{seed:064x}",
        "seed_sha256": sha256_text(f"{seed:064x}"),
        "revealed_card_number": revealed["card_number"],
        "revealed_boundary": revealed["label"],
        "method": "post_choice_random_permutation",
    }

    state.setdefault("boundary_draws", []).append(record)
    save_state(state_path, state)

    print(json.dumps({
        "chosen_token": record["chosen_token"],
        "revealed_card_number": record["revealed_card_number"],
        "revealed_boundary": record["revealed_boundary"],
        "remaining_after_draw": len(remaining) - 1,
        "audit_seed_hex": record["seed_hex"],
        "audit_seed_sha256": record["seed_sha256"],
    }, indent=2, ensure_ascii=False))


def color_resolve(args: argparse.Namespace) -> None:
    y = int(args.y)
    x = int(args.x)

    if y not in range(1, 6) or x not in range(1, 6):
        raise SystemExit("Both x and y must be integers from 1 through 5.")

    state_path = Path(args.state)
    palette_path = Path(args.palette)
    state = load_state(state_path)
    colors = load_palette(palette_path)

    used_colors = {
        entry.get("selected_color")
        for entry in state.get("color_resolutions", [])
        if entry.get("selected_color")
    }
    available_colors = [color for color in colors if color not in used_colors]

    if not available_colors:
        raise SystemExit("No unused colors remain for this image/run.")

    # Both coordinates are already locked before this block executes.
    # A fresh seed then creates a full 5x5 audit grid, while the selected
    # cell is guaranteed to contain a uniformly chosen UNUSED color.
    # Other audit-grid cells may contain previously used colors; only the
    # locked cell is outcome-bearing.
    seed = secrets.randbits(256)
    rng = random.Random(seed)
    selected_color = rng.choice(available_colors)
    grid = list(colors)
    rng.shuffle(grid)

    selected_index = (y - 1) * 5 + (x - 1)
    chosen_position = grid.index(selected_color)
    grid[selected_index], grid[chosen_position] = grid[chosen_position], grid[selected_index]
    rows = [grid[i:i + 5] for i in range(0, 25, 5)]

    record = {
        "timestamp": utc_now(),
        "palette_path": str(palette_path),
        "boundary": args.boundary,
        "operator_y": y,
        "model_x": x,
        "seed_hex": f"{seed:064x}",
        "seed_sha256": sha256_text(f"{seed:064x}"),
        "selected_index_zero_based": selected_index,
        "selected_color": selected_color,
        "no_repeat_within_image": True,
        "unused_colors_before_resolution": len(available_colors),
        "unused_colors_after_resolution": len(available_colors) - 1,
        "full_grid_after_reveal": rows,
    }

    state.setdefault("color_resolutions", []).append(record)
    save_state(state_path, state)

    print(json.dumps({
        "boundary": args.boundary,
        "operator_y": y,
        "model_x": x,
        "selected_color": selected_color,
        "unused_colors_after_resolution": len(available_colors) - 1,
        "audit_seed_hex": record["seed_hex"],
        "audit_seed_sha256": record["seed_sha256"],
    }, indent=2, ensure_ascii=False))


def audit(args: argparse.Namespace) -> None:
    state = load_state(Path(args.state))
    print(json.dumps(state, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prismline blind-bag resolver")
    sub = parser.add_subparsers(dest="command", required=True)

    p_boundary = sub.add_parser(
        "draw-boundary",
        help="Reveal one unused boundary after a token is locked.",
    )
    p_boundary.add_argument("--card", required=True, help="Path to BOUNDARY_CARD.md")
    p_boundary.add_argument("--token", required=True, type=int, help="Blind-bag token chosen before reveal")
    p_boundary.add_argument("--state", required=True, help="JSON audit/state file for this image/run")
    p_boundary.set_defaults(func=boundary_draw)

    p_color = sub.add_parser(
        "resolve-color",
        help="Resolve an unused color after y/x choices are locked.",
    )
    p_color.add_argument("--palette", required=True, help="Path to 25-color palette JSON")
    p_color.add_argument("--y", required=True, type=int, help="Operator y-axis choice, 1-5")
    p_color.add_argument("--x", required=True, type=int, help="Model x-axis choice, 1-5")
    p_color.add_argument("--boundary", required=True, help="Current revealed boundary label")
    p_color.add_argument("--state", required=True, help="JSON audit/state file for this image/run")
    p_color.set_defaults(func=color_resolve)

    p_audit = sub.add_parser("audit", help="Print the complete audit/state record.")
    p_audit.add_argument("--state", required=True)
    p_audit.set_defaults(func=audit)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
