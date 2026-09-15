# microsoft-fabric-labs

Synthetic sales ingestion and semantic-model learning labs for Microsoft Fabric.

## Architecture

Synthetic CSV → Lakehouse Files → Spark Delta table → SQL endpoint → semantic model → Power BI report. A Fabric pipeline can orchestrate the notebook after upload.

## Prerequisites

Python 3.12 for local generation; Fabric capacity or trial, a development workspace, Lakehouse, and permissions to create notebooks and models for cloud steps.

## Setup

1. Run `python examples/generate_sales.py` to create `data/sales.csv` locally.
2. Create a development Lakehouse and upload the CSV to `Files/sales/sales.csv`.
3. Create a Fabric PySpark notebook, attach the Lakehouse, and paste `examples/ingest_sales.py` into a cell.
4. Run the notebook, then add it to a pipeline Notebook activity and run manually.
5. Create a semantic model from `sales`, add the measures in `examples/measures.dax`, and build a Power BI report.
6. Validate row count (120), total revenue, and monthly totals against the CSV before scheduling.

## Sample workflow

Regenerate synthetic sales → upload → pipeline notebook → model refresh → inspect report. Overwrite mode is intentional for this small lab; implement incremental merge and schema contracts before production.

## Security

Read [SECURITY.md](SECURITY.md). Environment examples contain placeholders only.
Never commit local environment values or production exports. No deployment is automated.

## Troubleshooting

Missing Files path: check upload location and attached Lakehouse. Missing Spark: ingestion runs inside Fabric, not local Python. Model access errors: verify workspace permissions and capacity.

## License and attribution

Original implementations and documentation by Mudit Dholakia, licensed under MIT.
No upstream code was imported. These references informed the learning scope:
- https://github.com/microsoft/fabric-samples
- https://github.com/microsoft/semantic-link-labs
Platform services, SDK distributions, and third-party content retain their own terms.

## Updating

This is an original repository and has no upstream remote. Run `git pull --ff-only origin main`.
Review Dependabot changes and current platform documentation before upgrading.

## Validation limits

Python syntax and local smoke tests are checked before publication. Cloud execution,
tenant integrations, Tableau workbook authoring, and live agent evaluation require
your development environments and have not been verified by local checks.

## Toolkit and agent learning catalog

See [Toolkit and agent learning catalog](TOOLKIT-CATALOG.md) for the curated forks, supported SDK references, starting exercises, and compatibility guidance.
