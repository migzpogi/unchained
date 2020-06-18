number = 73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724271218839987979087922749219016997208880937766572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397536978179778461740649551492908625693219784686224828397224137565705605749026140797296865241453510047482166370484403199890008895243450658541227588666881164271714799244429282308634656748139191231628245861786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408071984038509624554443629812309878799272442849091845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
str_num = str(number)
adjacent = 13
loops = len(str_num) - adjacent + 1


def get_product_adjacent(n):
    numbers = list(n)

    product = 1
    for x in numbers:
        product *= int(x)

    return product


list_of_digits = []
list_of_products = []
for x in range(0, loops):
    d = str_num[x:x+adjacent]
    list_of_digits.append(d)
    list_of_products.append(get_product_adjacent(d))


answer = max(list_of_products)
answer_2 = list_of_digits[list_of_products.index(answer)]
print(answer, answer_2)