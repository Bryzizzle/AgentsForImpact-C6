# AgentsForImpact-C6
To deploy to Agent Engine as an API
```
adk deploy agent_engine bayviewapi --display_name "bayviewapi" --staging_bucket gs://<bucket-name>
```

To deploy to Cloud Run with the Web UI and without authentication
```
adk deploy cloud_run --project=qwiklabs-gcp-02-7374929129a9 --region=us-central1 --service_name=bayflowapi --app_name=bayflowapi --with_ui bayflowapi
```