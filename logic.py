from random import randint
import requests
from datetime import datetime, timedelta
import time

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.last_feed_time = datetime.now()

        # Pokemon.pokemons[pokemon_trainer] = self
#    def __init__(self, pokemon_card):
#
 #       self.pokemon_card = pokemon_card

        self.pokemon_hp = randint(50,70)
        self.pokemon_damage = randint(1,20)
   #     self.pokemon_hp = self.get_hp()
   #     self.pokemon_damage = self.get_damage()
        Pokemon.pokemons[pokemon_trainer] = self
    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "error"
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['home']['front_default'])
        else:
            return "Pikachu"


    def feed(self, feed_interval=11, hp_increase=7):
        current_time = datetime.now()   
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.pokemon_hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.pokemon_hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  




    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.pokemon_hp > self.pokemon_damage:
            enemy.pokemon_hp -= self.pokemon_damage
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.pokemon_hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name} Здоровье: {self.pokemon_hp} Урон: {self.pokemon_damage}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.pokemon_damage += super_power
        result = super().attack(enemy)
        self.pokemon_damage -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    
    def feed(self):
        return super().feed(hp_increase=10,feed_interval=15)


class Wizard(Pokemon):
    def feed(self):
        return super().feed(feed_interval=7, hp_increase=5)






if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))
    print(wizard.feed())
    time.sleep(12)
    print(wizard.feed())
