class StudentClass:
    def __init__(self):
        self.full_name = None
        self.date_of_birth = None
        self.age = None
        self.gender = None
        self.mobile_number = None
        self.email_address = None
        self.password = None
        self.preferred_language = None
        self.school_college_name = None
        self.class_grade = None
        self.board_curriculum = None
        self.academic_year = None
        self.subjects_for_tuition = []
        self.subject_levels = {}
        self.areas_needing_help = []

        self.parent_guardian_name = None
        self.parent_guardian_relationship = None
        self.parent_guardian_mobile_number = None
        self.parent_guardian_email_address = None
        self.preferred_communication_method = None

    def set_login_credentials(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def username_and_password(self, email_address, password):
        self.set_login_credentials(email_address, password)

    def __str__(self):
        student_name = self.full_name or getattr(self, "name", None) or "Unknown Student"
        return (
            f"Student: {student_name}, DOB: {self.date_of_birth}, "
            f"Age: {self.age}, Gender: {self.gender}, Mobile: {self.mobile_number}, "
            f"Email: {self.email_address}, Language: {self.preferred_language}"
        )