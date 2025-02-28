def decoder(data:list[list[str]], types, pix, all=False):
    turn = [[] for _ in range(8)]
    match types:
        case "farm":
            for i in range(len(data)):
                for j in range(len(data[i])):
                    turn[i].append(farm(data[i][j]))
    if all:
        return turn
    else :
        try:
            return turn[pix[1]][pix[0]]
        except IndexError:
            return "nothing"

def farm(data):
    t = ""
    for i in range(0, len(data), 2):
        t = t+farmn(data[i:i+2])+"#"

    return t[:-1]

def farmn(data):
    match data:
        case "00":
            return "nothing"
        case "AA":
            return "gryadka"
        case "BB":
            return "2"
        case "A1":
            return "irrigation"
        case "A2":
            return "melnitsa1"
        case "A3":
            return "waterwheel"
        case "A4":
            return "melnitsa2"
        case "C1":
            return "wheat"
        case "C2":
            return "corn"
        case "C3":
            return "rise"
    return "nothing"

def reset(file):
    mad =[[]for _ in range(8)]
    for i in range(8):
        for j in range(14):
            mad[i].append("00")
    with open(file, "w") as f:
        for i in mad:
            f.write(" ".join(map(str, i)) + "\n")

def gettilefromtextpos(pos):
    with open("saves/firstmap.txt", "r") as f:
        sadas = f.readlines()
        for i in range(len(sadas)):
            for j in range(len(sadas[i].split())):
                if i == pos[1] and j == pos[0]:
                    return sadas[i].split()[j]

def tiledecode(num):
    match num:
        case 1:return "GRASS"
        case 2: return "FARMLAND"
        case 3: return "WATER"
        case 4: return "FOREST"
        case 5: return "SAVANNA"
        case 6: return  "ASHLAND"
        case 7: return "DESERT"
        case 8: return "MOUNTAIN"

