from builtins import super


class ApiError(RuntimeError):
    """
    An API Error is any error returned from the API.  These
    typically have a status code in the 400s or 500s.  Most
    often, this will be caused by invalid input to the API.
    """

    def __init__(self, message, status=400, json=None):
        super().__init__(message)
        self.status = status
        self.json = json
        self.errors = []
        if json and "errors" in json and isinstance(json["errors"], list):
            self.errors = [e["reason"] for e in json["errors"]]
