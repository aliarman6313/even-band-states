import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# تعریف معادله ترنسندنتال برای حالات زوج
def even_equation(Eu):
    left = np.sqrt(10 - Eu) * np.tan(np.sqrt(10 - Eu))
    right = np.sqrt(Eu)
    return left - right

# محدوده جستجوی ریشه‌ها: Eu بین 0 و 10 (چون Eu < V0)
energies = []
guesses = np.linspace(0.1, 9.9, 1000)

for g in guesses:
    try:
        E_sol = fsolve(even_equation, g)[0]
        if 0 < E_sol < 10:
            # جلوگیری از تکرار
            if not any(np.isclose(E_sol, e, atol=1e-2) for e in energies):
                energies.append(E_sol)
    except:
        pass

# حذف تکراری‌ها و مرتب‌سازی
energies = sorted(set([round(e, 6) for e in energies]))

# نمایش انرژی‌های مجاز
print("Even bound state energies (dimensionless):")
for i, e in enumerate(energies):
    print(f"  E{i+1} = {e:.6f}")

# رسم طرفین معادله
x = np.linspace(0.01, 10, 1000)
lhs = np.sqrt(10 - x) * np.tan(np.sqrt(10 - x))
rhs = np.sqrt(x)

plt.figure(figsize=(8, 5))
plt.plot(x, lhs, label=r"$\sqrt{10 - E} \tan(\sqrt{10 - E})$", color='blue')
plt.plot(x, rhs, label=r"$\sqrt{E}$", color='red')
plt.axhline(0, color='gray', lw=0.5)
plt.title("Even Bound States: Intersection of Curves")
plt.xlabel("Dimensionless Energy $E$")
plt.ylabel("Function Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()