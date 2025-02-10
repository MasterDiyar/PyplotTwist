def decoder(data:list[list[str]], types, pix):
    turn = [[] for _ in range(8)]
    match types:
        case "farm":
            for i in range(len(data)):
                for j in range(len(data[i])):
                    turn[i].append(farm(data[i][j]))

    return turn[pix[0]][pix[1]]

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

