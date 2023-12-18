from rest_framework import serializers
from .models import Student, Parent, AcademicDetails, Document

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'
        extra_kwargs = {'student': {'required': False}}

class AcademicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDetails
        fields = '__all__'
        extra_kwargs = {'student': {'required': False}}

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        extra_kwargs = {'student': {'required': False}}

class StudentCreateSerializer(serializers.ModelSerializer):
    parent = ParentSerializer()
    academic_details = AcademicDetailsSerializer()
    documents = DocumentSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        parent_data = validated_data.pop('parent')
        academic_details_data = validated_data.pop('academic_details')
        documents_data = validated_data.pop('documents')

        student = Student.objects.create(**validated_data)

        Parent.objects.create(student=student, **parent_data)
        AcademicDetails.objects.create(student=student, **academic_details_data)

        for document_data in documents_data:
            Document.objects.create(student=student, **document_data)

        return student
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.adhar_card_number = validated_data.get('adhar_card_number', instance.adhar_card_number)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.identification_marks = validated_data.get('identification_marks', instance.identification_marks)
        instance.admission_category = validated_data.get('admission_category', instance.admission_category)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.mail_id = validated_data.get('mail_id', instance.mail_id)
        instance.contact_detail = validated_data.get('contact_detail', instance.contact_detail)
        instance.address = validated_data.get('address', instance.address)

        instance.save()

        parent_data = validated_data.pop('parent', {})
        parent_instance, _ = Parent.objects.update_or_create(student=instance, defaults=parent_data)
        parent_instance.__dict__.update(parent_data)
        parent_instance.save()

        academic_details_data = validated_data.pop('academic_details', {})
        academic_details_instance, _ = AcademicDetails.objects.get_or_create(student=instance, defaults=academic_details_data)
        academic_details_instance.__dict__.update(academic_details_data)
        academic_details_instance.save()

        documents_data = validated_data.pop('documents', [])
        instance.documents.all().delete()
        Document.objects.bulk_create([Document(student=instance, **doc_data) for doc_data in documents_data])

        return instance

class StudentSerializer(serializers.ModelSerializer):
    parent = ParentSerializer()
    academic_details = AcademicDetailsSerializer(source='academicdetails')  # Use source to specify the related name

    documents = DocumentSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'