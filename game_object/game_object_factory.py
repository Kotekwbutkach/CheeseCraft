from typing import Dict

from game_object.object.cat import Cat
from game_object.object.cheese import Cheese
from game_object.object.mouse import Mouse


class GameObjectFactory:
    string_to_type: Dict[str, type] = {
        "Mouse": Mouse,
        "Cat": Cat,
        "Cheese": Cheese,
    }

    @staticmethod
    def create(x: int, y: int, object_type_name: str):
        if object_type_name not in GameObjectFactory.string_to_type.keys():
            raise ValueError(f"Failed to initialize unknown GameObject type {object_type_name}")
        object_type: type = GameObjectFactory.string_to_type[object_type_name]
        return object_type(x, y)
