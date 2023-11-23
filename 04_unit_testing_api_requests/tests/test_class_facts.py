from lib.class_facts import CatFacts
from unittest.mock import Mock

def test_cat_fact_provide_returns_formatted_cat_fact():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock

    response_mock.json.return_value = {"fact":"Grown cats have 30 teeth. Kittens have about 26 temporary teeth, which they lose when they are about 6 months old.","length":114}

    cat_fact = CatFacts(requester_mock)
    result = cat_fact.provide()
    assert result == "Cat fact: Grown cats have 30 teeth. Kittens have about 26 temporary teeth, which they lose when they are about 6 months old."