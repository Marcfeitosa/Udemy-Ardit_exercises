import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id": str})


class Product:
    def __init__(self, product_id):
        self.id = product_id
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()
        self.in_stock_index = df.loc[df["id"] == self.id].index[0]  # Get index of the product row

    def available(self):
        """Check if the product is available"""
        in_stock = df.loc[df["id"] == self.id, "in stock"].squeeze()
        return in_stock > 0

    def decrease_stock(self):
        """Decrease stock by 1"""
        df.at[self.in_stock_index, "in stock"] -= 1
        df.to_csv("articles.csv",index=False) # Save the updated DataFrame to the CSV file


class Purchase:
    def __init__(self, article):
        self.article = article

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {article.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
order = input("Enter product's id you want to buy: ")
article = Product(product_id=order)
if article.available():
    article.decrease_stock()
    receipt = Purchase(article)
    receipt.generate()
    print("Purchase successful")
else:
    print("No such article in stock.")

