#!/usr/bin/env python3
"""Start a new briefing from editable canvas sources; never overwrite an existing directory."""
import argparse
from pathlib import Path
import shutil
from build_flow_canvas import build


def create(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=False)
    assets = Path(__file__).resolve().parents[1] / 'assets/flow-canvas'
    for name in ('presentation.template.html', 'canvas-model.js'):
        shutil.copy2(assets / name, directory / name)
    return build(directory / 'presentation.template.html', directory / 'canvas-model.js', directory / 'presentation.html')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    args = parser.parse_args()
    try:
        output = create(args.directory)
    except (OSError, ValueError) as error:
        parser.exit(1, f'Creation failed; existing files preserved: {error}\n')
    print(output)
    print('Canvas starter created. Replace fictional content and select the visual direction before delivery.')


if __name__ == '__main__':
    main()
