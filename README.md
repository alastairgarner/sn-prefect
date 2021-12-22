# sn-prefect

## Download

1. Clone this repo locally
2. Download Prefect locally, as you'll need to run some commands through the terminal. Maybe best to do this inside a virtualenv

```bash
pip install prefect
```

## Setup

1. Spin up the Prefect stack using `docker-compose up` in our sn-sql-datastack repo
2. Inside this repo, run the following commands

```bash
# Use a local server, rather than the cloud, as our backend
prefect backend server
# First time setup config. Not needed on later sessions
prefect server create-tenant --name test_tenant
prefect create project "test_project"
# Register the flows in our local file with the backend
prefect register -p ./test-flows.py --project test_project
```

3. Spin up the Prefect Docker Agent

```bash
prefect agent docker start --show-flow-logs
```

4. Navigate to `localhost:8081` to access the Prefect GUI. You should now see that the flows have been registered and are available to run.

---

## Notes

Any updates to the flow file will need to be pushed to this repo, as the Docker container that Prefect spins up to run the flow will pull the code from this repo.
