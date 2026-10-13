#!/usr/bin/env python3
"""Build the local canvas starter without dependencies or network access."""
import argparse
from pathlib import Path


def build(template, model, output, force=False):
    template, model, output = map(Path, (template, model, output))
    if output.resolve() in (template.resolve(), model.resolve()):
        raise ValueError('Output must not overwrite either source file')
    html = template.read_text(encoding='utf-8')
    if html.count('/* MODEL */') != 1:
        raise ValueError('Template must contain exactly one /* MODEL */ marker')
    code = model.read_text(encoding='utf-8')
    if '</script' in code.lower():
        raise ValueError('Model contains an unsafe closing script tag')
    html = html.replace('/* MODEL */', code)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w' if force else 'x', encoding='utf-8') as stream:
        stream.write(html)
    return output


def main():
    assets = Path(__file__).resolve().parents[1] / 'assets/flow-canvas'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template', type=Path, default=assets / 'presentation.template.html')
    parser.add_argument('--model', type=Path, default=assets / 'canvas-model.js')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--force', action='store_true', help='Replace an existing output')
    args = parser.parse_args()
    try:
        result = build(args.template, args.model, args.output, args.force)
    except (OSError, ValueError) as error:
        parser.exit(1, f'Build failed: {error}\n')
    print(result)


if __name__ == '__main__':
    main()
