from dagster import (
    Definitions, load_assets_from_modules, define_asset_job, AssetSelection, ScheduleDefinition
)

from .assets import resources

# Define job
bigstar_pipeline_job = define_asset_job("bigstar_pipeline_job", selection=AssetSelection.all())

# Add a schedule definition for the job
bigstar_pipeline_schedule = ScheduleDefinition(
    job=bigstar_pipeline_job,
    cron_schedule="0 * * * *"
)

defs = Definitions(
    assets=load_assets_from_modules(
    [assets]),
    resources=resources,
    jobs=[bigstar_pipeline_job],
    schedules=[bigstar_pipeline_schedule]
)
