
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, adminviews, userviews, pacdviews,odsusviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('userlogs/', userviews.user_logs, name='userlogs'),

    # This is admin version two
    path('AdminversionTwo', adminviews.ADMINVERSIONTWO, name='adminversiontwo'),

    # This is admin panel
    path('Admin/AdminHome', adminviews.ADMINHOME, name='admin_home'),
    path('Admin/AddCategory', adminviews.ADD_CATEGORY, name='add_category'),
    path('Admin/AddCategoryCityMun', adminviews.ADD_CATEGORY_CITYMUN, name='add_category_citymun'),
    path('Admin/ManageCategory', adminviews.MANAGE_CATEGORY, name='manage_category'),

    path('Admin/ManageCategoryCityMunc', adminviews.MANAGE_CATEGORY_CITYMUNC, name='manage_category_citymunc'),
    path('UpdateCategoryCityMunc/<str:id>/', adminviews.UPDATE_CATEGORY_CITYMUNC, name='update_category_citymunc'),
    path('UpdateCategoryDetailsCityMunc/<str:id>/', adminviews.UPDATE_CATEGORY_DETAILS_CITYMUNC, name='update_category_details_citymunc'),
    path('Admin/DeleteCategoryCityMunc/<str:id>', adminviews.DELETE_CATEGORY_CITYMUNC, name='delete_category_citymunc'),

    path('Admin/AddSubcategoryCityMunc', adminviews.ADD_SUBCATEGORY_CITYMUNC, name='add_subcategory_citymunc'),
    path('Admin/ManageSubcategoryCityMunc', adminviews.MANAGE_SUBCATEGORY_CITYMUNC, name='manage_subcategory_citymunc'),
    path('UpdateSubcategoryCityMunc/<str:id>', adminviews.UPDATE_SUBCATEGORY_CITYMUNC, name='update_subcategory_citymunc'),

    path('Admin/DeleteCategory/<str:id>', adminviews.DELETE_CATEGORY, name='delete_category'),
    path('UpdateCategory/<str:id>', adminviews.UPDATE_CATEGORY, name='update_category'),
    path('UpdateCategoryDetails', adminviews.UPDATE_CATEGORY_DETAILS, name='update_category_details'),
    path('Admin/AddSubcategory', adminviews.ADD_SUBCATEGORY, name='add_subcategory'),
    path('Admin/ManageSubcategory', adminviews.MANAGE_SUBCATEGORY, name='manage_subcategory'),
    path('Admin/DeleteSubcategory/<str:id>', adminviews.DELETE_SUBCATEGORY, name='delete_subcategory'),
    path('UpdateSubcategory/<str:id>', adminviews.UPDATE_SUBCATEGORY, name='update_subcategory'),
    path('UpdateSubcategoryDetails', adminviews.UPDATE_SUBCATEGORY_DETAILS, name='update_subcategory_details'),
    
    path('UpdateSubcategoryDetailsCityMunc', adminviews.UPDATE_SUBCATEGORY_DETAILS_CITYMUNC, name='update_subcategory_details_citymunc'),
    

    path('Admin/AddState', adminviews.ADD_STATE, name='add_state'),
    path('Admin/ManageState', adminviews.MANAGE_STATE, name='manage_state'),
    path('Admin/DeleteState/<str:id>', adminviews.DELETE_STATE, name='delete_state'),
    path('UpdateState/<str:id>', adminviews.UPDATE_STATE, name='update_state'),
    path('UpdateStateDetails', adminviews.UPDATE_STATE_DETAILS, name='update_state_details'),
    
    path('LodgedComplaint', adminviews.LODGEDCOMPLAINTS, name='lodgedcomplaint'),
    
     path('odsuslodgedcomplaint', odsusviews.LODGEDCOMPLAINTS, name='odsuslodgedcomplaint'),



    path('ViewLodgedComplaint/<str:id>', adminviews.VIEWLODGEDCOMPLAINTS, name='viewlodgedcomplaint'),


    path('LodgedComplaintRemark', adminviews.LODGEDCOMPLAINTSREMARK, name='lodgedcomplaintremark'),
    path('ManageUser', adminviews.MANAGEUSERS, name='manageusers'),
    path('ViewUser/<str:id>',adminviews.VIEWUSERS, name='viewusers'),   
    path('Admin/DeleteUser/<str:id>', adminviews.DELETEUSERS, name='delete_user'),
    path('Admin/UserComplaints/<str:id>', adminviews.USERSCOMPLAINTS, name='view_complaints'),   
    
    path('NewComplaints', adminviews.NEWCOMPLAINTS, name='newcomplaints'),
    path('InprocessComplaints', adminviews.INPROCESSCOMPLAINTS, name='inprocesscomplaints'),
    path('ResolvedComplaints', adminviews.RESOLVEDCOMPLAINTS, name='resolvedcomplaints'),
    path('ClosedComplaints', adminviews.CLOSEDCOMPLAINTS, name='closedcomplaints'),
    
    path('ComplaintsBetweenDateReport', adminviews.COMPLAINTSREPORT, name='complaintsreports'),
    
     path('odsuscomplaintsreports', odsusviews.COMPLAINTSREPORT, name='odsuscomplaintsreports'),
    
    path('UserBetweenDateReport', adminviews.USERBDREPORT, name='userbdreports'),
    path('SearchComplaints', adminviews.Search_Complaints, name='searchcomplaints'),
    path('SearchUsers', adminviews.Search_Users, name='searchusers'),
    
     # This is user panel
    path('Comuser/UserHome', userviews.USERHOME, name='user_home'),
    path('usersignup/', userviews.USERSIGNUP, name='usersignup'),
    path('RegisterComplaint', userviews.REGCOMPLAINT, name='regcomplaint'),
    path('PaceRegisterComplaint', userviews.PACEREGCOMPLAINT, name='paceregcomplaint'),
    path('CscCcbComplaint', userviews.CSCCCB, name='cscccbcomplaint'),
    path('Non8888RegComplaint', userviews.NON8888REGCOMPLAINT, name='non8888regcomplaint'),
    
    
    path('usernewcomplaints', userviews.NEWCOMPLAINTS, name='usernewcomplaints'),
    path('userinprocesscomplaints', userviews.INPROCESSCOMPLAINTS, name='userinprocesscomplaints'),
    path('userresolvedcomplaints', userviews.RESOLVEDCOMPLAINTS, name='userresolvedcomplaints'),
    path('userclosedcomplaints', userviews.CLOSEDCOMPLAINTS, name='userclosedcomplaints'),
        
    path('UserViewLodgedComplaint/<str:id>', userviews.VIEWLODGEDCOMPLAINTS, name='userviewlodgedcomplaint'),
    
    path('pacdcomplaint', userviews.PACDOCOMPLAINT, name='pacdcomplaint'),
    path('get_subcat/', userviews.get_subcat, name='get_subcat'),
    path('get_subcats/', userviews.get_subcats, name='get_subcats'),
    path('ComplaintHistory', userviews.COMPLAINTHISTORY, name='complainthistory'),
    path('UserDashboardHistory', userviews.USERDASHBOARDHISTORY, name='userdashboardhistory'),
    path('UserDashboardDetails/<str:id>', userviews.USERDASHBOARDHISTORYDETAILS, name='userdashboarddetails'),
    path('ComplaintHistoryDetails/<str:id>', userviews.COMPLAINTHISTORYDETAILS, name='complainthistorydetails'),
    
    path('UserLodgedComplaintRemark', userviews.USERLODGEDCOMPLAINTSREMARK, name='userlodgedcomplaintremark'),
    
    
    # This is pacd panel
    path('pacdusersignup/', pacdviews.PACDUSERSIGNUP, name='pacdusersignup'),
    path('Pacduser/PacdHome', pacdviews.PACDUSERHOME, name='pacd_home'),
    path('PacdComplaintHistory', pacdviews.PACDCOMPLAINTHISTORY, name='pacdcomplainthistory'),
    path('PacdComplaintHistoryDetails/<str:id>', pacdviews.PACDCOMPLAINTHISTORYDETAILS, name='pacdcomplainthistorydetails'),
    path('PacDeveReg', pacdviews.PACDEVEREG, name='pacdevereg'),


    # This is odsus panel
    path('OdsusSignup/', odsusviews.ODSUSSIGNUP, name='odsussignup'),
    path('Odsus/OdsusHome', odsusviews.ODSUSHOME, name='odsus_home'),
    path('OdsusHistory', odsusviews.ODSUSHISTORY, name='odsushistory'),
    path('OdsusReg', odsusviews.ODSUSREG, name='odsusreg'),
    path('OdsusHistoryDetails/<str:id>', odsusviews.ODSUSHISTORYDETAILS, name='odsushistorydetails'),
    
    path('odsusnewcomplaints/', odsusviews.NEWCOMPLAINTS, name='odsusnewcomplaints'),
    path('odsusinprocesscomplaints', odsusviews.INPROCESSCOMPLAINTS, name='odsusinprocesscomplaints'),
    path('odsusresolvedcomplaints', odsusviews.RESOLVEDCOMPLAINTS, name='odsusresolvedcomplaints'),
    path('odsusclosedcomplaints', odsusviews.CLOSEDCOMPLAINTS, name='odsusclosedcomplaints'),


    #profile path
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('Password', views.CHANGE_PASSWORD, name='change_password'),
    path('notifications/', views.notifications, name='notifications'),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
