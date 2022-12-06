import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.HashMap;

public class Program {

    private static HashMap<Character, Integer> vals = new HashMap<Character, Integer>() {{
        put('A', 1);
        put('B', 2);
        put('C', 3);
        put('X', 1);
        put('Y', 2);
        put('Z', 3);
    }};

    private static HashMap<Character, HashMap<Character, Integer>> getResult = 
    new HashMap<Character, HashMap<Character, Integer>>() {{
        put('A', new HashMap<Character, Integer>(){{
            put('X', 3); put('Y', 6); put('Z', 0);
        }});
        put('B', new HashMap<Character, Integer>(){{
            put('X', 0); put('Y', 3); put('Z', 6);
        }});
        put('C', new HashMap<Character, Integer>(){{
            put('X', 6); put('Y', 0); put('Z', 3);
        }});
    }};

    private static HashMap<Character, HashMap<Character, Character>> actions = 
    new HashMap<Character, HashMap<Character, Character>>() {{
        put('X', new HashMap<Character, Character>(){{
            put('A', 'Z'); put('B', 'X'); put('C', 'Y');
        }});
        put('Y', new HashMap<Character, Character>(){{
            put('A', 'X'); put('B', 'Y'); put('C', 'Z');
        }});
        put('Z', new HashMap<Character, Character>(){{
            put('A', 'Y'); put('B', 'Z'); put('C', 'X');
        }});
    }};

    public static void main(String[] args) {
         try {
            var scanner = new Scanner(new File("../input.txt"));

            int part_1_sum = 0;
            int part_2_sum = 0;

            while (scanner.hasNextLine()) {
                var line = scanner.nextLine();

                var opponent    = line.charAt(0);
                var me          = line.charAt(2);

                // Part 1
                part_1_sum += vals.get(me) + getResult.get(opponent).get(me);

                // Part 2
                var p2_action = actions.get(me).get(opponent);
                part_2_sum += vals.get(p2_action) + getResult.get(opponent).get(p2_action);
            }
            scanner.close();

            System.out.println("Part 1: " + part_1_sum);
            System.out.println("Part 2: " + part_2_sum);
        }
        catch (FileNotFoundException e) {
            System.out.println("input file not found");
            e.printStackTrace();
        }
    }
}