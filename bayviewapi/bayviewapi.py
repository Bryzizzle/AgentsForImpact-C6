from google import adk
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search
from vertexai.agent_engines import AdkApp
from google.adk.tools.bigquery import BigQueryCredentialsConfig, BigQueryToolset
import google.auth
import asyncio

model = "gemini-2.0-flash"

credentials, _ = google.auth.default()
credentials_config = BigQueryCredentialsConfig(credentials=credentials)

bigquery_toolset = BigQueryToolset(
    credentials_config=credentials_config
)

facilities_agent = Agent(
    model='gemini-2.0-flash',
    name='FacilitiesAgent',
    description="Accesses a BigQuery table containing information about city facilities in San Francisco",
    instruction="""
    You are a BigQuery data analysis agent that should access the 'sf_city_facilities'
    table in dataset 'c6' in project 'qwiklabs-gcp-02-7374929129a9'. This table contains
    a list of city facilities in San Francisco. Use this to respond to the user

    The fields available are: [facility_id, common_name, address, city, zip_code,
    block_lot, owned_leased, dept_id_for_jurisdiction, jurisdiction, gross_sq_ft,
    longitude, latitude, supervisor_district, city_tenants, land_id, geom]
    """,
    tools=[bigquery_toolset]
)

search_agent = Agent(
    model='gemini-2.0-flash',  # Specify the model to use
    name='SearchAgent',
    description="Accesses Google Search API to answer queries",
    instruction="""
    You are a specialist in Google Search. Your primary function is to perform web searches
    to answer user queries or gather information. When a user asks a question,
    you should use the google_search tool to find relevant inflsormation and
    then synthesize a concise answer based on the search results.
    """,
    tools=[google_search],  # Attach the built-in google_search tool
)

root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[facilities_agent, search_agent],
)

app = AdkApp(agent=root_agent)

# async def main():
#     # If you're already in an async function
#     async for event in app.async_stream_query(
#         user_id="USER_ID",
#         message="Does deYoung Museum have free parking available?",
#     ):
#         print(event)

# if __name__ == "__main__":
#     asyncio.run(main())
