from google.cloud import bigquery

def run_query_from_file(filepath, project_id):
    client = bigquery.Client(project=project_id)
    with open(filepath, "r") as file:
        query = file.read()
    return client.query(query).to_dataframe()
