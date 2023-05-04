import random
import time


class Player:
    def __init__(self, player_name, player_hp, player_damage):
        self.name = player_name
        self.hp = player_hp
        self.damage = player_damage
        self.exp = 0
        self.level = 1

    @staticmethod
    def create_player(player_name, player_race, player_class):
        hp = 10
        damage = 10
        player_name = player_name
        if player_race == races_list[0]:
            hp += 10
            damage += 7
            if player_class == class_list[0]:
                hp -= 2
                damage += 3
            elif player_class == class_list[1]:
                hp += 2
                damage += 1
            else:
                print('Такого класса не существует!!!')
                quit()
        elif player_race == races_list[1]:
            hp += 7
            damage += 8
            if player_class == class_list[0]:
                hp -= 3
                damage += 4
            elif player_class == class_list[1]:
                hp += 2
                damage += 2
            else:
                print('Такого класса не существует!!!')
                quit()
        elif player_race == races_list[2]:
            hp += 8
            damage += 8
            if player_class == class_list[0]:
                hp -= 1
                damage += 3
            elif player_class == class_list[1]:
                hp += 2
                damage += 3
            else:
                print('Такого класса не существует!!!')
                quit()
        elif player_race == races_list[3]:
            hp += 10
            damage += 9
            if player_class == class_list[0]:
                hp += 1
                damage += 3
            elif player_class == class_list[1]:
                hp += 3
                damage += 3
            else:
                print('Такого класса не существует!!!')
                quit()
        else:
            print('Такой расы не существует!!!')
            quit()
        return Player(player_name=player_name, player_hp=hp, player_damage=damage)

    @staticmethod
    def create_weapon():
        weapon_type = ["Меч", "Лук", "Сковородка", "Топор", "Секира", "Экспалибур"]
        weapon_rare = {
            1: "обычный",
            2: "редкий",
            3: "мифический"
        }
        weapon_random = random.choice(weapon_type)
        weapon_random_rare = random.choice(list(weapon_rare.keys()))
        if weapon_random == weapon_type[0]:
            character.damage += 10 * weapon_random_rare
        elif weapon_random == weapon_type[1]:
            character.damage += 9 * weapon_random_rare
        elif weapon_random == weapon_type[2]:
            character.damage += 13 * weapon_random_rare
        elif weapon_random == weapon_type[3]:
            character.damage += 12 * weapon_random_rare
        elif weapon_random == weapon_type[4]:
            character.damage += 14 * weapon_random_rare
        elif weapon_random == weapon_type[5]:
            character.damage += 15 * weapon_random_rare
        return weapon_random, weapon_rare[weapon_random_rare]

    @staticmethod
    def create_heal():
        health = {
            5: 'таблетки',
            10: "бинты",
            20: "малая аптечка",
            30: "аптечка"
        }
        health_type_random = random.choice(list(health.keys()))
        character.hp += health_type_random
        return health[health_type_random]

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.hp += 10 * self.level
        self.damage += 8 * self.level
        print(f'Ваш уровень равен: {self.level}')

    def attack(self, victim):
        victim.hp -= self.damage
        print(f'Ваш урон: {self.damage}')
        time.sleep(.5)
        if victim.hp <= 0:
            rnd_exp = self.level * 13
            print(f'Поздрвляяем, {victim.name} повержен! + {rnd_exp}')
            item = random.randint(0, 2)
            if item == 1:
                weapon = self.create_weapon()
                print(f'Вам выпало оружие!!\n'
                      f'{weapon[0]} {weapon[1]}\n'
                      f'Ваш урон: {self.damage}')
                time.sleep(.7)
            elif item == 2:
                health = self.create_heal()
                print(f"Вы получили: {health}\n"
                      f"Ваше здоровье: {self.hp}")
            elif item == 0:
                print('Вам ничего не выпало')
                time.sleep(.7)
            self.exp += rnd_exp
            max_exp = self.level * 78
            if self.exp >= max_exp:
                self.level_up()
                max_exp = self.level * 78
                print(f'До следующего уровня осталось: {max_exp} опыта')
                time.sleep(.7)
            time.sleep(.7)
            return False
        elif victim.hp > 0:
            print(f'{victim.name}, оставшееся здоровье: {victim.hp}')
            return True


class Enemy:
    def __init__(self, enemy_name, enemy_hp, enemy_damage):
        self.name = enemy_name
        self.hp = enemy_hp
        self.damage = enemy_damage

    @staticmethod
    def create_enemy():
        enemy_names = ["Вампир", "Скелет", "Орк"]
        enemy_name = random.choice(enemy_names)
        enemy_hp = random.randint(8, 20) + 15 * character.level
        enemy_damage = random.randint(7, 10) + 10 * character.level
        return Enemy(enemy_name, enemy_hp, enemy_damage)

    def attack(self, victim):
        victim.hp -= self.damage
        print(f'{self.name}, его урон: {self.damage}')
        time.sleep(.5)
        if victim.hp <= 0:
            print(f'Вы поиграли, игра окончена')
            quit()
        elif victim.hp > 0:
            print(f'{victim.name}, оставшееся здоровье: {victim.hp}')
            time.sleep(.5)


print(f'Здравствуйте как вас зовут?')
name = input()

races_list = ['эльф', "гном", "хоббит", "человек"]
class_list = ["лучник", "рыцарь"]

print("К какой расе вы относитесь?")
for race_player in races_list:
    print(race_player, end=' ')
print()

race = input().lower()

print('Какой класс вы выберите?')
for player_class in class_list:
    print(player_class, end=' ')
print()

class_player = input().lower()

character = Player.create_player(player_name=name, player_race=race, player_class=class_player)


def fight_choice():
    choice = int(input('Атаковать(1) или бежать(2)'))
    if choice == 1:
        result = character.attack(enemy)
        if result:
            enemy.attack(character)
            fight_choice()
    elif choice == 2:
        plan = random.randint(0, 1)
        if plan == 0:
            print(f'Вы сбежали от монстра')
            time.sleep(.7)
        elif plan == 1:
            print('Вас поймали')
            time.sleep(.7)
            enemy.attack(character)
            time.sleep(.3)
            fight_choice()


while True:
    event = random.randint(0, 2)
    if event == 0 or event == 1:
        print('Вы никого не встретили, идём дальше...')
        time.sleep(1)
    elif event == 2:
        enemy = Enemy.create_enemy()
        print(f'Вас заметил {enemy.name}!')
        fight_choice()
