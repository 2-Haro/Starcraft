from random import *

class unit:
  def __init__(self, name, hp, speed, damage):
    self.name = name
    self.hp = hp
    self.speed = speed
    self.damage = damage
    print(f"{name} 유닛이 생성되었습니다.")

  def move(self, location):
    print(f"{self.name} 유닛이 {location} 방향으로 이동합니다. [속도 : {self.speed}]")

  def damaged(self, damage):
    print(f"{self.name} : {damage} 데미지를 입었습니다.")
    self.hp -= damage
    print(f"{self.name} 유닛의 현재 체력은 {self.hp}입니다.")
    if self.hp <= 0:
      print(f"{self.name} 유닛이 파괴되었습니다.")

class attackUnit(unit):
  def __init__(self, name, hp, speed, damage):
    super().__init__(name, hp, speed, damage)
  
  def attack(self, location):
    print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 : {self.damage}]")

class marine(attackUnit):
  def __init__(self):
    super().__init__("마린", 40, 1, 5)
    # attackUnit.__init__(self, "마린", 40, 1, 5)

  def stimpack(self):
    if self.hp >= 10:
      self.hp -= 10
      print(f"{self.name} 유닛이 스팀팩을 사용합니다. (HP 10 감소)")
    else:
      print(f"{self.name} 유닛의 체력이 부족해서 스팀팩을 사용할 수 없습니다.")

class tank(attackUnit):

  seize_developed: False

  def __init__(self):
    super().__init__("탱크", 150, 1, 35)
    # attackUnit.__init__(self, "탱크", 150, 1, 35)
    self.seize_mode = False

  def set_seize_mode(self):
    if tank.seize_developed == False:
      return
    elif self.seize_mode == False:
      print(f"{self.name} 유닛이 시즈모드로 전환합니다.")
      self.damage *= 2
      self.seize_mode = True
    else:
      print(f"{self.name} 유닛이 시즈모드를 해제합니다.")
      self.damage /= 2
      self.seize_mode = False

class flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed
  
  def fly(self, name, location):
    print(f"{name} 유닛이 {location} 방향으로 이동합니다. [속도 : {self.flying_speed}]")

class flyableAttackUnit(attackUnit, flyable):
  def __init__(self, name, hp, damage, flying_speed):
    attackUnit.__init__(self, name, hp, 0, damage)
    flyable.__init__(self, flying_speed)

  def move(self, location):
    self.fly(self.name, location)

class wraith(flyableAttackUnit):
  def __init__(self):
    super().__init__("레이스", 80, 20, 5)
    # flyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
    self.cloaked = False
  
  def cloaking(self):
    if self.cloaked == True:
      print(f"{self.name} 유닛의 클로킹 모드를 해제합니다.")
      self.cloaked = False
    else:
      print(f"{self.name} 유닛의 클로킹 모드를 활성화합니다.")
      self.cloaked = True

def game_start():
  print("새로운 게임을 시작합니다.")

def game_over():
  print("[Player] : gg")
  print("[Player]님이 게임에서 퇴장하셨습니다.")

game_start()

m1 = marine()
m2 = marine()
m3 = marine()

t1 = tank()
t2 = tank()

w1 = wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
  unit.move("1시")

tank.seize_developed = True
print("탱크 시즈모드 개발이 완료되었습니다.")

for unit in attack_units:
  if isinstance(unit, marine):
    unit.stimpack()
  elif isinstance(unit, tank):
    unit.set_seize_mode()
  elif isinstance(unit, wraith):
    unit.cloaking()

for unit in attack_units:
  unit.attack("1시")

for unit in attack_units:
  unit.damaged(randint(5, 20))

game_over()