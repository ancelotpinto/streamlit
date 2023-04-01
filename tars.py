
# https://medium.com/geekculture/web-page-content-analysis-made-easy-with-streamlit-a-step-by-step-guide-d5051ed6c3b7
# example to get the details directly from the webpage, instead of having configuration

import urllib.parse

import requests
import streamlit

streamlit.set_page_config(
    page_title="TARS",
    page_icon="🤖",
)

url = streamlit.text_input("URL", value="https://www.zalando.de/damenschuhe/")

parse_result = urllib.parse.urlparse(url)

response = requests.get(f"https://stt-tars-production.fashion-store.zalan.do/seo-text",
                        params={"uri": parse_result.path, "templates_only": True},
                        headers={"accept-language": "de-DE",
                                 "x-sales-channel": "01924c48-49bb-40c2-9c32-ab582e6db6f4",
                                 "content-type": "application/json",
                                 "x-zalando-entity-id": "ern:collection:cat:", })

streamlit.write(response.json())
