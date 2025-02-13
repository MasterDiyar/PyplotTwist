from config.const import *
import json


class Technology:
    def __init__(self, name, x, y, requirements=None, cost=None):
        self.name = name
        self.unlocked = False
        self.requirements = requirements if requirements else []
        self.cost = cost if cost else {}
        self.rect = pygame.Rect(x, y, 120, 50)

    def unlock(self, unlocked_techs, resources):
        if all(req in unlocked_techs for req in self.requirements) and all(
                resources.get(res, 0) >= amount for res, amount in self.cost.items()):
            for res, amount in self.cost.items():
                resources[res] -= amount
            self.unlocked = True
            return True
        return False


class TechTree:
    def __init__(self):
        self.techs = {}
        self.resources = {"stone": 200, "glass": 100}

    def add_tech(self, name, x, y, requirements=None, cost=None):
        self.techs[name] = Technology(name, x, y, requirements, cost)

    def unlock_technology(self, name):
        if name in self.techs:
            tech = self.techs[name]
            if tech.unlock([t for t, obj in self.techs.items() if obj.unlocked], self.resources):
                print(f"{name} unlocked!")
                return True
            else:
                print(f"Cannot unlock {name}, requirements not met or insufficient resources.")
                print(f"required resources : {tech.cost}")
        return False

    def save_file(self, filename):
        data = {
            name: {"unlocked": tech.unlocked, "requirements": tech.requirements, "cost": tech.cost, "x": tech.rect.x,
                   "y": tech.rect.y} for name, tech in self.techs.items()}
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for name, info in data.items():
                    self.techs[name] = Technology(name, info["x"], info["y"],
                                                  info.get("requirements", []),
                                                  info.get("cost", {}))
                    self.techs[name].unlocked = info["unlocked"]
        except FileNotFoundError:
            print("Save file not found, starting fresh.")

    def draw(self, screen):
        for name, tech in self.techs.items():
            color = (0, 255, 0) if tech.unlocked else (255, 0, 0)
            new_rect = tech.rect.copy()
            new_rect.width = 8 * len(name) + 20
            pygame.draw.rect(screen, color, new_rect, border_radius=5)
            text = font.render(name, True, (255, 255, 255))
            screen.blit(text, (tech.rect.x + 10, tech.rect.y + 15))
            for req in tech.requirements:
                if req in self.techs:
                    pygame.draw.line(screen, (255, 255, 255), tech.rect.center, self.techs[req].rect.center, 2)

    def handle_click(self, pos):
        for name, tech in self.techs.items():
            if tech.rect.collidepoint(pos):
                self.unlock_technology(name)

