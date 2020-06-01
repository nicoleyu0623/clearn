package org.szi.l01Interfaces.interfaces;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class EmployeeSortDemo {

    private static final Logger logger = LoggerFactory.getLogger(EmployeeSortDemo.class);

    private  void testSortCollWithMethodReference(List<String> l){
        logger.info("## sorting on collecton with method referencing");
        l.sort(String::compareToIgnoreCase);
        logger.info("words after sorting %s%n",l);
    }

    private  void testCompareEmployeesWithCompratorInner(Employee[] staff) {
        logger.info("## sorting on compareTo in Employee class");
        Arrays.sort(staff);
        logger.info(Arrays.toString(staff));

        logger.info("### sorting employees on another criteria");
        //inner class
        class NameComparator implements Comparator<Employee> {
            @Override
            public int compare(Employee left, Employee right) {
                logger.info("comparing " + left + " and " + right);
                return left.getName().compareTo(right.getName());
            }
        }
        Arrays.sort(staff, new NameComparator());
        logger.info(Arrays.toString(staff));
    }
    private  void testCompareEmployeesWithLambda(Employee[] staff){
        //now the syntaxis for the same is so much shorter
        System.out.println("### sorting on compareTo implemented as lambda");
        Arrays.sort(staff,
                (left,right)-> right.getName().length() - left.getName().length());
        System.out.println(Arrays.toString(staff));
    }
    private   void testCompareEpmloyeesWith2comparison(Employee[] staff){
        System.out.println("### sort on 2 criterias");
        Arrays.sort(staff,
                Comparator.comparingDouble(Employee::getSalary)
                        .thenComparing(Employee::getName));
        System.out.println(Arrays.toString(staff));
    }

    public static void main(String[] args) {


        Employee[] emps = new Employee[3];

        emps[0] = new Employee("Harry Hacker", 75000);
        emps[1] = new Employee("Carl Cracker", 76000);
        emps[2] = new Employee("Tony Tester", 38000);

        logger.debug("all tests started {}.","youppi");

        EmployeeSortDemo d = new EmployeeSortDemo();
        logger.info("testCompareEmployeesWithCompratorInner");
        d.testCompareEmployeesWithCompratorInner(emps);
        logger.info("testCompareEmployeesWithLambda");
        d.testCompareEmployeesWithLambda(emps);
        logger.info("testCompareEpmloyeesWith2comparison");
        d.testCompareEpmloyeesWith2comparison(emps);

        List<String> words =
                Arrays.asList("this", "Is", "a", "list", "of", "Strings");
        logger.info("testSortCollWithMethodReference");
        d.testSortCollWithMethodReference(words);

        logger.debug("all tests done..");
    }


}