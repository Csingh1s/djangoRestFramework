from rbasis.urlrouter import router
from . import views

def RegPath():
    router.register(r'user', views.userView, "user", "")
    router.register(r'receipt', views.receiptView, "receipt", "")
    router.register(r'step', views.stepView, "step", "")
    router.register(r'ingredient', views.ingredientView, "ingredient", "")
