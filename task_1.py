from pulp import LpProblem, LpMaximize, LpVariable

model = LpProblem(name="Optimization", sense=LpMaximize)

lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="FruitJuice", lowBound=0, cat="Integer")

model += 3 * lemonade + 5 * fruit_juice, "Total_Products"

model += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
model += lemonade <= 50, "Sugar_Constraint"
model += lemonade <= 30, "LemonJuice_Constraint"
model += 2 * fruit_juice <= 40, "FruitPuree_Constraint"

model.solve()

print(f"Optimal quantity of Lemonade: {lemonade.varValue}")
print(f"Optimal quantity of Fruit Juice: {fruit_juice.varValue}")
print(f"Maximum Total Products: {model.objective.value()}")
