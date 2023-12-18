from django.urls import path
from .views import StudentCreateAPIView, ExcelImportAPIView, StudentPdfView, ExportExcelView

urlpatterns = [
   
    path('students/', StudentCreateAPIView.as_view(), name='create-student'),
    path('students/<int:pk>/', StudentCreateAPIView.as_view(), name='student-detail'), 
    # import excel
    path('excel-import/', ExcelImportAPIView.as_view(), name='excel_import'),
    # export as pdf
    path('export-pdf/', StudentPdfView.as_view(), name='student_pdf'),
    # export as excel
    path('export-excel/', ExportExcelView.as_view(), name='student_excel'),

]
