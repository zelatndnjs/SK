package lab.student.entity;

public class Student {
    private String studentId;
    private String name;
    private String major;
    private int grade;

    // 생성자
    public Student(String studentId, String name, String major, int grade) {
        this.studentId = studentId;
        this.name = name;
        this.major = major;
        setGrade(grade); // 유효성 검사 포함
    }

    // getter
    public String getStudentId() {
        return studentId;
    }

    public String getName() {
        return name;
    }

    public String getMajor() {
        return major;
    }

    public int getGrade() {
        return grade;
    }

    // setter
    public void setGrade(int grade) {
        if (grade >= 1 && grade <= 4) {
            this.grade = grade;
        } else {
            System.out.println("학년은 1~4 사이여야 합니다.");
        }
    }
}