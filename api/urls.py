from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('credits/', views.getCredits, name='credits'),
    path('credit-info/<int:id>', views.getCredit, name='credit-info'),
    path('apply-credit/', views.postCredit, name='apply-credit'),
    path('update-credit/<int:id>', views.updateCredit, name='update-credit'),
]
