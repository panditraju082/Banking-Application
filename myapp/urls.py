from django.urls import path,include
from . import views
urlpatterns = [
path("",views.indexview,name="index"),
path("loginpage/",views.loginview,name="user_login"),
path("regispage/",views.regisview,name="user_regis"),
path("user_homepage/",views.insertviews,name="user_data"),
path("user_loginpage/",views.user_loginview,name="user_homelogin"),
path("user_logpage/",views.user_logviews,name="user_logout"),
path("user_profilepage/",views.user_profileview,name="user_profile"),
path("user_afterloginhomepage/",views.after_loginhomeview,name="afterloginhome"),
path("sendmoneypage/",views.send_moneyview,name="send_money"),
path("t_historypage/",views.t_hisview,name="t_hisotry"),
path("upi_page/",views.upi_view,name="upi_transfer"),
path("banktransferpage/",views.bank_transferview,name="sent_bank"),
path("depositemoneypage/",views.deposite_moneyview,name="deposite_money"),
path("upi_paymentpage/",views.upi_payment,name="upi_payment"),
path("bank_paymentpage/",views.bank_payment,name="bank_payment"),
path("deposite_paymetpage/",views.deposite_paymet,name="deposite_paymet"),
path('transaction_history/', views.transaction_history, name='transaction_history')
]