import csv


#WAP to dislpay aa the records from product.csv  whose price is greater than 300. format of record is [product_id, product_name, price]
# with open("product.csv","w",newline="") as f:
#     writer=csv.writer(f)
#     writer.writerow(["product_id","product_name","price"])

def add_product(id, name, price):
    with open("product.csv","a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([id,name,price])
        print("Product added successfully")

# add_product(1,"mobile",100)
# add_product(2,"laptop",500)
# add_product(3,"tv",3000)
# add_product(4,"watch",40)

def price_greater_than(price):
    with open("product.csv","r") as f:
        reader=list(csv.reader(f))
        data=reader[1:]
        for i in data:
            if int(i[2])>price:
                print(i)
    
n=int(input("Enter the price greater than which you want to search: "))
price_greater_than(n)