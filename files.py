with open('models.txt', 'w') as f:
    f.write('hello\nhello\nhello\n1234end')
    f.close()
with open('models.txt', 'r') as f:
    result = f.readline()
    print(result)
    print(100 * '*')
    result = f.readline()
    print(result)
    print(100 * '*')
    result = f.readline()
    print(result)
    print(100 * '*')
    result = f.readline()
    print(result)
    print(100 * '*')