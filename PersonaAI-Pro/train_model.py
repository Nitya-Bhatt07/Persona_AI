import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
import pickle

personalities = ["Leader","Creative","Analytical","Social","Calm"]
rows = []

for p in personalities:
    for _ in range(50):  # 250 rows
        q = []
        for i in range(15):
            if (p=="Leader" and i<3) or \
               (p=="Creative" and 3<=i<6) or \
               (p=="Analytical" and 6<=i<9) or \
               (p=="Social" and 9<=i<12) or \
               (p=="Calm" and 12<=i<15):
                q.append(random.randint(4,5))
            else:
                q.append(random.randint(1,3))

        rows.append(q + [p])

cols = [f"q{i}" for i in range(1,16)] + ["personality"]
df = pd.DataFrame(rows, columns=cols)
df.to_csv("dataset.csv", index=False)

X = df.drop("personality", axis=1)
y = df["personality"]

model = RandomForestClassifier(n_estimators=300)
model.fit(X,y)

pickle.dump(model, open("persona_model.pkl","wb"))

print("Premium model ready ✅")