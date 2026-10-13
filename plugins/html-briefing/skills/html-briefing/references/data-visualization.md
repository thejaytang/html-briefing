# Quantitative evidence in a briefing

Create charts and tables directly using the project’s existing tools and the guidance below. A separate plotting or results-table skill is not required. Use readable projection sizes rather than tiny journal text.

## Define the comparison

For every material metric, establish the source, unit, denominator, time window, sample, aggregation, missing-data treatment and baseline. Distinguish observed results, calculations, estimates, illustrative inputs and targets. Compare like definitions. Do not turn missing data into zero, cumulative counts into rates, or planned tests into passed tests.

| Question | Starting representation |
|---|---|
| Compare categories | Sorted bars or dots; disclose meaningful ordering |
| Change over time | Line chart with consistent time intervals and gaps |
| Distribution or variation | Points, histogram, box/violin with sample context |
| Relationship | Scatter; association is not causation |
| Part of a whole | Stacked bar or a small simple part-whole chart with a valid denominator |
| Uncertainty or effect estimates | Point and interval; identify interval type |
| Exact figures or mixed definitions | Readable semantic table with units and notes |

Chart type follows the audience question. Do not impose one library. Small native SVG charts may suffice; an available Plotly/ECharts or other implementation is appropriate when it earns its dependency cost. Package any required runtime locally for offline delivery and retain its license.

## Integrity and readability

- Reconcile displayed values with source output; recompute critical calculations independently where practical.
- Use consistent scales for comparisons. Bar magnitude normally needs a zero baseline; explain necessary transformations or truncation rather than exaggerating effects.
- Identify sample size and uncertainty where they affect interpretation. Do not infer confidence intervals, p-values or model performance from a picture.
- Use categorical versus sequential/diverging colors according to meaning. Do not rely on red/green alone.
- Keep labels, units, notes and sources legible at actual viewing size. Provide a text summary or table for information that would otherwise exist only on hover.
- Explain filtering and show empty/missing states accurately. Parameter changes must update the displayed method and evidence as well as the plot.
- Preserve scientific meaning when simplifying. Put essential qualifications beside the figure; full definitions can be expanded.

## Check the final artifact

Verify values and definitions, then inspect the rendered figure at relevant window sizes. Check clipping, label overlap, legend-to-series mapping, keyboard-accessible interactions, final offline resources and the printed/static state when requested. A correct plotting script does not establish that the exported HTML works.
