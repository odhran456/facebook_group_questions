import pandas as pd
import random


df = pd.DataFrame(columns = ['options', 'probability'])
df['options'] = ['Green', 'Red', 'Blue']
df['probability'] = [0.2, 0.5, 0.3]

monte_carlo_selection = random.choices(population=[x for x in df['options'].tolist()], weights=[y for y in df['probability'].tolist()], k=1)[0]
print(monte_carlo_selection)

