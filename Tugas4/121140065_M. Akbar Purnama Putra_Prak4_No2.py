#Nama   : M. Akbar Purnama Putra
#NIM    : 121140065
#Kelas  : RB
#No     : 2

import random

class Robot:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
    
    def attack(self):
        return self.dmg
    
    def heal(self):
        self.hp += 4000
    
    def decrease_hp(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
    
    def choose_hand(self):
        return random.randint(1, 3)
    
    def __str__(self):
        return f"{self.name} ({self.hp} HP)"

def perform_action(robot1, robot2, turn):
    hand1 = robot1.choose_hand()
    hand2 = robot2.choose_hand()
    
    if hand1 == 1 and hand2 == 2:
        dmg = robot1.attack()
        robot2.decrease_hp(dmg)
        print(f"Robotmu ({robot1}) menyerang sebanyak {dmg} DMG")
        
    elif hand1 == 1 and hand2 == 3:
        dmg = robot2.attack()
        robot1.decrease_hp(dmg)
        print(f"Robot lawan ({robot2}) menyerang sebanyak {dmg} DMG")
        
    elif hand1 == 2 and hand2 == 1:
        dmg = robot2.attack()
        robot1.decrease_hp(dmg)
        print(f"Robot lawan ({robot2}) menyerang sebanyak {dmg} DMG")
        
    elif hand1 == 2 and hand2 == 3:
        dmg = robot1.attack()
        robot2.decrease_hp(dmg)
        print(f"Robotmu ({robot1}) menyerang sebanyak {dmg} DMG")
        
    elif hand1 == 3 and hand2 == 1:
        dmg = robot1.attack()
        robot2.decrease_hp(dmg)
        print(f"Robotmu ({robot1}) menyerang sebanyak {dmg} DMG")
        
    elif hand1 == 3 and hand2 == 2:
        dmg = robot2.attack()
        robot1.decrease_hp(dmg)
        print(f"Robot lawan ({robot2}) menyerang sebanyak {dmg} DMG")
        
    elif hand1 == 1 and hand2 == 1:
        robot2.heal()
        print(f"Robot lawan ({robot2}) menambah darah sebanyak 4000 HP")
        
    elif hand1 == 2 and hand2 == 2:
        robot1.heal()
        print(f"Robotmu ({robot1}) menambah darah sebanyak 4000 HP")
        
    else:
        print("Kedua robot memilih tangan yang sama.")
    
    print(f"Turn saat ini: {turn}")
    print(f"Robotmu ({robot1}), robot lawan ({robot2})")
    print(f"Pilih tangan robotmu ({robot1.name}): {hand1}")
    print(f"Pilih tangan robot lawan ({robot2.name}): {hand2}")
    print()
    
    return robot1.hp == 0 or robot2.hp == 0

print("Selamat datang di pertandingan robot Yamako")
print("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus)")
while True:
    robot_choice = int(input("Pilih robot yang akan kamu gunakan: "))
    if robot_choice == 1:
        robot = Robot("Antares", 20000, 1000)
        opponent = Robot("Robot Lawan", 10000, 1500)
    elif robot_choice == 2:
        robot = Robot("Alphasetia", 25000, 800)
        opponent = Robot("Robot Lawan", 1000, 1500)
    elif robot_choice == 3:
        robot = Robot("Lecalicus", 18000, 1200)
        opponent = Robot("Robot Lawan", 10000, 1500)
    else:
        print("Input salah. Silakan pilih lagi.")
        continue
    break

robot_lawan = Robot("Robot Lawan", 10000, random.randint(1000, 2000))

print("Robotmu: ", robot)
print("Robot lawan: ", robot_lawan)

turn = 1

while True:
    print(f"----- Turn {turn} -----")
    
    if perform_action(robot, opponent, turn):
        print("Pertandingan berakhir!")
        break
    
    turn += 1
    robot1 = Robot('Antares', 20000, 4000)
    robot2 = Robot("Alphasetia", 25000, 800)
    robot3 = Robot("Lecalicus", 18000, 1200)
    
if robot.hp <= 0:
    print("Maaf, "+robot.name+" kalah dalam pertandingan ini.")
elif robot_lawan.hp <= 0:
    print("Selamat, "+robot.name+" menang dalam pertandingan ini!")
elif robot.hp == robot.hp:
    print("Pertandingan berakhir seri.")
    print(f"Robotmu ({robot}), robot lawan ({robot})")
    print("Kedua robot memiliki HP yang sama.")


    



