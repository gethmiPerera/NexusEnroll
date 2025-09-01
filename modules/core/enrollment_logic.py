from .dsa import Student, Course, Section


def check_prerequisites(student: Student, course: Course) -> bool:
    """Check if student has completed all prerequisites for the course"""
    return all(prereq in student.completed_courses for prereq in course.prerequisites)


def manage_waitlist(section: Section) -> str:
    """Pop next student from waitlist if seat is available"""
    if section.has_seat() and section.waitlist:
        next_student = section.waitlist.pop(0)
        section.increment_enrolled()
        return next_student
    return None


def validate_enrollment(student: Student, course: Course, section: Section) -> bool:
    """
    Validate whether a student can enroll in a section:
    - check prerequisites
    - check capacity
    - check duplicate enrollment
    """
    if course.course_id in student.current_enrollments:
        return False
    if not check_prerequisites(student, course):
        return False
    if not section.has_seat():
        return False
    return True
