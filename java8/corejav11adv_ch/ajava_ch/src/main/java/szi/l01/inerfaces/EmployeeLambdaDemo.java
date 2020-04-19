package szi.l01.inerfaces;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;


import java.awt.event.ActionListener;
import java.util.Arrays;
import java.util.List;
import javax.swing.Timer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class EmployeeLambdaDemo {
    private static final Logger logger = LogManager.getLogger("EmployeeLambdaDemo");
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Max Levin", "Karl Zeus", "Vlad Ko");
        Stream<Employee>  stream = names.stream()
                                .map(Employee::new);
        Employee[] folks = stream.toArray(Employee[]::new);
        System.out.printf("employees from names %s%n",Arrays.asList(folks));

        List<Employee>  emps = names.stream()
                                .map(Employee::new)
                                .collect(Collectors.toList());
        System.out.println("same with shorter syntax");
        System.out.printf("employees from names %s%n",emps);

    }

    //example of a method as a closure
    public static void repeatMessage(String text, int delay){
        //closure
        ActionListener listener = event -> {
            System.out.println(text); //has access to attributes from outer scope
        };
        new Timer(delay, listener).start();
        logger.info("called repeat Message");
    }

}
