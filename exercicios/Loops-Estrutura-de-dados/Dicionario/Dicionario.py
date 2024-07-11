def main():
    
    estados = {"AM": "amazonas",
                "BA": "bahia", 
                "SC": "santa catarina",
                "SP": "são paulo", 
                "TO": "tocantins"}

    print(estados.items())

    # dict.keys()
    print(estados.keys())

    # dict.get(item) != dict[item] - não existe
    print(estados["AM"])
    print(estados.get("AY"))

    estados["RJ"] = "rio de janeiro"

    estados.pop("TO")
    print(estados)

main()




