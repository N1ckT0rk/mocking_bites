import requests


class CatFacts:
    def __init__(self, fact):
        self.fact = fact

    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self.fact.get("https://catfact.ninja/fact")
        return response.json()