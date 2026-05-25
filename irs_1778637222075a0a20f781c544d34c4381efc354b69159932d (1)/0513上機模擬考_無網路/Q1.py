'''
請依程式碼行號解說以下程式碼的功能
'''
def validate_receipt(receipt):
    if len(receipt) < 4:
        print("不合法的收據編號")
        return
    if not receipt.isdigit():
        print("不合法的收據編號")
        return
    digits = [int(d) for d in receipt[:-1]]
    checksum = (sum(digits) * 3) % 10
    if checksum == int(receipt[-1]):
        print("合法的收據編號")
    else:
        print("不合法的收據編號")

while True:
    user_input = input("請輸入收據編號 (輸入exit結束): ")
    if user_input.lower() == "exit":
        break
    validate_receipt(user_input)
