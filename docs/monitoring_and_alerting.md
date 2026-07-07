# Monitoring and Alerting

## ADF Monitor
Use ADF Monitor to check pipeline runs, activity runs, start and end times, row counts, and failure messages.

## Logic Apps Failure Notification
The pipeline template includes a failure path with a Logic Apps webhook placeholder: `<logic-app-webhook-url>`.

In a real lab, create a Logic App with an HTTP trigger and replace the placeholder in ADF. Do not commit the real webhook URL.

## Audit Table
The `audit.pipeline_audit` table stores pipeline name, run ID, source name, target table, rows copied, status, error message, and load time. This gives a simple SQL-based operational view for reruns and troubleshooting.
