from ninja import Ninja

from pet import Dog


chubbs = Dog('Chubbs', 'sit, walk, backflip')
print(chubbs.name)

billy = Ninja('Billy', 'The Kid', 'Bacon', 'Kibbles&Bits')

billy.all_pets.append(chubbs)
print(billy.all_pets[0].name)

billy.walk(0).feed(0).bathe(0)




demon = Dog('Demon', 'Break-dancing')
print(demon.name)


jon = Ninja('Jon', 'Griggs', 'Cookies', 'Ice Cream')
print(jon.first_name)

jon.all_pets.append(demon)

jon.walk(0).feed(0).bathe(0)
