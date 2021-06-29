"""
   Copyright 2021 line-bot-oss

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import json
from os.path import dirname, join
from typing import Dict

FLEX = {"messages": [{"type": "flex", "altText": "This is a Flex Message"}]}
RESOURCE_DIR = "resources"


def get_flex_content(key: str) -> dict:
    with open(
        join(dirname(__file__), RESOURCE_DIR, "/flex.json")
    ) as json_file:
        flex: Dict[str, dict] = json.load(json_file)

    if flex.get(key) is None:
        raise Exception(f"Not found flex content: {key}")

    return flex[key]
