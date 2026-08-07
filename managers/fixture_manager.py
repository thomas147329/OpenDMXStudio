import json
import os

from models.fixture import Fixture


class FixtureManager:
    def __init__(self, profile_path="profiles"):
        self.fixtures = []
        self.profile_path = profile_path

    def load_profile(self, filename):
        path = os.path.join(self.profile_path, filename)

        with open(path, "r") as file:
            data = json.load(file)

        return data

    def add_fixture(self, name, address, profile):
        fixture = Fixture(
            name,
            address,
            len(profile.get("channels", []))
        )

        fixture.profile = profile
        self.fixtures.append(fixture)

        return fixture

    def remove_fixture(self, fixture):
        if fixture in self.fixtures:
            self.fixtures.remove(fixture)

    def get_fixture(self, name):
        for fixture in self.fixtures:
            if fixture.name == name:
                return fixture

        return None
