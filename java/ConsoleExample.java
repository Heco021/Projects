import java.io.Console;

public class ConsoleExample {
    public static void main(String[] args) {
        Console console = System.console();
        if (console == null) {
            System.err.println("No console.");
            System.exit(1);
        }

        String input = console.readLine("Enter something: ");
        console.printf("You entered: %s%n", input);
    }
}