from levenshtein import Levenshtein

while(1):
    p1 = input("Primeira palavra: ")
    p2 = input("Segunda palavra: ")
    print("Distância de Levenshtein: %d" % Levenshtein(p1,p2).distance())
    print("____________________________________________")