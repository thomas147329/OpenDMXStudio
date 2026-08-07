class Scene:
    def __init__(self, name):
        self.name = name
        self.values = {}

    def set_channel(self, channel, value):
        self.values[channel] = value

    def apply(self, universe):
        for channel, value in self.values.items():
            universe.set_channel(channel, value)

    def __str__(self):
        return self.name


class SceneManager:
    def __init__(self):
        self.scenes = []

    def add(self, scene):
        self.scenes.append(scene)

    def get(self, name):
        for scene in self.scenes:
            if scene.name == name:
                return scene
        return None
