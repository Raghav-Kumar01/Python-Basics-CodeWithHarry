def main():
    try:
        a = int(input("Enter a Number:"))
        print(a)


    except Exception as e:
        print(e)

    finally:
        print("i am inside of finally")

main()