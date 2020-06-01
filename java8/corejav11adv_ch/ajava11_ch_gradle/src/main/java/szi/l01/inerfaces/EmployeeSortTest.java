package szi.l01.inerfaces;





import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;


import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;

public class EmployeeSortTest {

    private static final Logger logger = LogManager.getLogger("EmployeeSortTest");
    public static void main(String[] args) {

        logger.info("hello infoing");

        Employee[] emps = new Employee[3];

        emps[0] = new Employee("Harry Hacker", 75000);
        emps[1] = new Employee("Carl Cracker", 76000);
        emps[2] = new Employee("Tony Tester", 38000);
        testCompareEmployeesWithCompratorInner(emps);

        testCompareEmployeesWithLambda(emps);

        testCompareEpmloyeesWith2comparison(emps);

        System.out.println("## sorting on collecton with method referencing");
        List<String> words =
                Arrays.asList("this", "Is", "a", "list", "of", "Strings");

        testSortCollWithMethodReference(words);
    }

    private static void testSortCollWithMethodReference(List<String> l){
        l.sort(String::compareToIgnoreCase);
        System.out.printf("words after sorting %s%n",l);
    }

    private static void testCompareEmployeesWithCompratorInner(Employee[] staff) {
        System.out.println("## sorting on compareTo in Employee class");
        Arrays.sort(staff);
        System.out.println(Arrays.toString(staff));

        System.out.println("### sorting employees on another criteria");
        //inner class
        class NameComparator implements Comparator<Employee> {
            @Override
            public int compare(Employee left, Employee right) {
                logger.info("comparing " + left + " and " + right);
                return left.getName().compareTo(right.getName());
            }
        }
        Arrays.sort(staff, new NameComparator());
        System.out.println(Arrays.toString(staff));
    }
    private static void testCompareEmployeesWithLambda(Employee[] staff){
        //now the syntaxis for the same is so much shorter
        System.out.println("### sorting on compareTo implemented as lambda");
        Arrays.sort(staff,
                (left,right)-> right.getName().length() - left.getName().length());
        System.out.println(Arrays.toString(staff));
    }
    private static void testCompareEpmloyeesWith2comparison(Employee[] staff){
        System.out.println("### sort on 2 criterias");
        Arrays.sort(staff,
                    Comparator.comparingDouble(Employee::getSalary)
                    .thenComparing(Employee::getName));
        System.out.println(Arrays.toString(staff));
    }

}