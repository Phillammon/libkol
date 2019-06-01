from typing import Optional
from .element import (
    Tag as Tag,
    SoupStrainer as SoupStrainer
)

class BeautifulSoup(Tag):
    def __init__(
        self,
        markup: str = ...,
        features: Optional[str] = ...,
        parse_only: Optional[SoupStrainer] = ...,
    ) -> None: ...
