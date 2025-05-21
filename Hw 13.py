# 1
import json
from typing import List, Dict, Optional

class UserProfile:
    def __init__(self, name: str, age: int, interests: List[str]):
        self.name = name
        self.age = age
        self.interests = interests

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "age": self.age,
            "interests": self.interests
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'UserProfile':
        return cls(
            name=data["name"],
            age=data["age"],
            interests=data["interests"]
        )

def save_profile(user: UserProfile, filename: str) -> bool:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(user.to_dict(), file, ensure_ascii=False, indent=4)
        return True
    except (IOError, TypeError) as e:
        print(f"Ошибка при сохранении файла: {e}")
        return False

def load_profile(filename: str) -> Optional[UserProfile]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return UserProfile.from_dict(data)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except json.JSONDecodeError:
        print(f"Файл {filename} содержит невалидный JSON.")
    except KeyError as e:
        print(f"В файле {filename} отсутствует обязательное поле: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке файла: {e}")
    return None

if __name__ == "__main__":
    user = UserProfile("Alice", 25, ["Python", "AI"])
    save_profile(user, "profile.json")
    new_user = load_profile("profile.json")
    if new_user:
        print(f"Загружен профиль: {new_user.name}, {new_user.age}, {new_user.interests}")


# 2
import pickle
import os
from typing import List, Optional

class Task:
    def __init__(self, name: str, priority: int, completed: bool = False):
        self.name = name
        self.priority = priority
        self.completed = completed

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.name} (приоритет: {self.priority})"

class TaskManager:
    def __init__(self, filename: str = "tasks.pickle"):
        self.filename = filename
        self.tasks: List[Task] = self._load_tasks()

    def _load_tasks(self) -> List[Task]:
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'rb') as file:
                try:
                    return pickle.load(file)
                except EOFError:
                    print("Файл задач пуст, создан новый список")
                    return []
        except Exception as e:
            print(f"Ошибка при загрузке задач: {e}, создан новый список")
            return []

    def save_tasks(self):
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(self.tasks, file)
        except Exception as e:
            print(f"Ошибка при сохранении задач: {e}")

    def add_task(self, name: str, priority: int):
        self.tasks.append(Task(name, priority))
        self.save_tasks()

    def remove_task(self, task_name: str) -> bool:
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False

    def mark_completed(self, task_name: str) -> bool:
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                self.save_tasks()
                return True
        return False

    def show_tasks(self):
        if not self.tasks:
            print("Нет задач в списке")
            return
        
        print("\nСписок задач:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Купить молоко", 2)
    manager.add_task("Сделать домашку", 1)
    manager.add_task("Позвонить маме", 3)

    manager.mark_completed("Купить молоко")

    manager.remove_task("Позвонить маме")

    manager.show_tasks()


# 3
import json
from typing import List, Dict, Optional


class UserValidator:
    @staticmethod
    def validate_user(user_data: Dict) -> bool:
        try:
            if not all(key in user_data for key in ['id', 'name', 'email']):
                print(f"Ошибка: отсутствуют обязательные поля в пользователе {user_data}")
                return False

            if not isinstance(user_data['id'], int):
                print(f"Ошибка: id должен быть целым числом (пользователь {user_data})")
                return False

            if not isinstance(user_data['name'], str):
                print(f"Ошибка: name должен быть строкой (пользователь {user_data})")
                return False

            if not isinstance(user_data['email'], str) or '@' not in user_data['email']:
                print(f"Ошибка: email должен быть строкой с символом @ (пользователь {user_data})")
                return False

            return True

        except Exception as e:
            print(f"Неизвестная ошибка при валидации пользователя {user_data}: {e}")
            return False


def load_users(filename: str) -> Dict[str, List[Dict]]:
    result = {
        'valid': [],
        'invalid': []
    }

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            users = json.load(file)

            if not isinstance(users, list):
                print("Ошибка: файл должен содержать список пользователей")
                return result

            for user in users:
                if UserValidator.validate_user(user):
                    result['valid'].append(user)
                else:
                    result['invalid'].append(user)

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден")
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} содержит невалидный JSON")
    except Exception as e:
        print(f"Неизвестная ошибка при загрузке файла: {e}")

    return result


def print_stats(users_data: Dict[str, List[Dict]]):
    print(f"\nСтатистика загрузки:")
    print(f"Успешно загружено: {len(users_data['valid'])}")
    print(f"Пропущено из-за ошибок: {len(users_data['invalid'])}")
    print("\nПример корректного пользователя:")
    if users_data['valid']:
        print(users_data['valid'][0])
    else:
        print("Нет корректных пользователей")


if __name__ == "__main__":
    users_data = load_users("users.json")
    print_stats(users_data)


# 4
import pickle
import os
from datetime import datetime
from typing import List, Optional

class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        self.creation_date = datetime.now()

    def __repr__(self):
        return (f"Заметка: {self.title}\n"
                f"Дата: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Текст: {self.content}\n"
                f"{'-'*30}")

class NoteManager:
    def __init__(self, filename: str = "notes.pkl"):
        self.filename = filename
        self.notes: List[Note] = self._load_notes()

    def _load_notes(self) -> List[Note]:
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            print("Файл заметок поврежден, создан новый список")
            return []
        except Exception as e:
            print(f"Ошибка при загрузке заметок: {e}, создан новый список")
            return []

    def _save_notes(self):
        try:
            with open(self.filename, 'wb') as file:
                pickle.dump(self.notes, file)
        except Exception as e:
            print(f"Ошибка при сохранении заметок: {e}")

    def add_note(self, title: str, content: str):
        self.notes.append(Note(title, content))
        self._save_notes()

    def delete_note(self, title: str) -> bool:
        for i, note in enumerate(self.notes):
            if note.title == title:
                del self.notes[i]
                self._save_notes()
                return True
        return False

    def show_all_notes(self):
        if not self.notes:
            print("Нет сохраненных заметок")
            return
        
        print("\nВсе заметки:")
        for i, note in enumerate(self.notes, 1):
            print(f"{i}. {note}")

if __name__ == "__main__":
    manager = NoteManager()

    manager.add_note("Покупки", "Молоко, хлеб, яйца")
    manager.add_note("Идеи", "Разработать новый проект на Python")
    manager.add_note("Важное", "Не забыть поздравить с днем рождения")

    manager.delete_note("Идеи")

    manager.show_all_notes()
