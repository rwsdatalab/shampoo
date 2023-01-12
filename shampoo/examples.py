# %%
import shampoo
print(dir(shampoo))
print(shampoo.__version__)

# %%
from shampoo import shampoo
model = shampoo(verbose=10)
model.fit_transform()

# %%
