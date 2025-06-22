def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "NOT FOUND"
        case 500:
            return "INTERNAL SERVER ERROR"
        case _:             
            return    "Unknown status" #Usage print(http_status(200)) # output: OK like that other one

print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(505))