def reorderLogFiles(logs):
    results1 = []
    results2 = []
    for log in logs:
        if (log.split()[1]).isdigit():
            results2.append(log)
        else:
            results1.append(log.split())
    results1.sort(key=lambda x: x[0])
    results1.sort(key=lambda x: x[1:])
    
    for i in range(len(results1)):
        results1[i] = (" ".join(results1[i]))
        results1.extend(results2)
    
    print(results1)
   
    


# Driver Function
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
reorderLogFiles(logs)
