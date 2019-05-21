import pykollib.Error as Error
from .GenericRequest import GenericRequest
from pykollib.old_database import ItemDatabase
from pykollib.pattern import PatternManager
from pykollib.util import parsing


class MakePasteRequest(GenericRequest):
    "Creates meat paste, meat stacks, or dense meat stacks."

    def __init__(self, session, itemId, quantity=1):
        super(MakePasteRequest, self).__init__(session)
        self.url = session.server_url + "craft.php"
        self.requestData["pwd"] = session.pwd
        self.requestData["action"] = "makepaste"
        self.requestData["qty"] = quantity

    def parseResponse(self):
        # Check for errors.
        noMeatForPastePattern = PatternManager.getOrCompilePattern(
            "noMeatForMeatpasting"
        )
        if noMeatForPastePattern.search(self.responseText):
            raise Error.Error(
                "Unable to make the requested item. You don't have enough meat.",
                Error.NOT_ENOUGH_MEAT,
            )

        # Get the item(s) we received.
        items = parsing.parseItemsReceived(self.responseText, self.session)
        if len(items) > 0:
            self.responseData["items"] = items
        else:
            raise Error.Error(
                "Unknown error. No items received.", Error.REQUEST_GENERIC
            )
