import pykollib
from bs4 import BeautifulSoup
from typing import List

from ..Trophy import Trophy
from .request import Request


class trophy(Request):
    def __init__(self, session: "pykollib.Session") -> None:
        super().__init__(session)

        self.request = session.request("trophy.php")

    @staticmethod
    async def parser(html: str, **kwargs) -> List:
        soup = BeautifulSoup(html, "html.parser")

        ids = [trophy["value"] for trophy in soup.find_all("input", attrs={"name": "whichtrophy"})]

        return await Trophy.filter(id__in=ids)
