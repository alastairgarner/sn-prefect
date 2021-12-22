# flows/my_flow.py

from prefect import task, Flow
from prefect.storage import GitHub
from prefect.run_configs import DockerRun


@task
def get_data():
    return [1, 2, 3, 4, 5]


@task
def print_data(data):
    print(data)


with Flow("test-flow") as flow:
    data = get_data()
    print_data(data)

flow.run_config = DockerRun(
    image="prefecthq/prefect:latest-python3.8"
)
flow.storage = GitHub(
    repo="alastairgarner/sn-prefect",                            # name of repo
    path="test_flows.py",                    # location of flow file in repo
    # name of personal access token secret
    # access_token_secret="GITHUB_ACCESS_TOKEN"
)
