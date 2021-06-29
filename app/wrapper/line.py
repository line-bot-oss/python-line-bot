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

import os
from os.path import dirname
from typing import List, Optional

from linebot import LineBotApi
from linebot.models import SendMessage


class LINE(LineBotApi):
    def save_content_from_message_id(self, message_id: str, path: str) -> None:
        """
        save content (image, video, auido) from message_id
        """

        os.makedirs(dirname(path), exist_ok=True)
        with open(path, "wb") as content_file:
            content_file.write(self.get_message_content(message_id).content)

    def reply_message(
        self,
        reply_token: str,
        *args: List[SendMessage],
        notification_disabled: bool = False,
        timeout: Optional[int] = None
    ) -> None:
        super().reply_message(
            reply_token,
            args,
            notification_disabled=notification_disabled,
            timeout=timeout,
        )
