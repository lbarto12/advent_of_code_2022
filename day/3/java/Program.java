import java.util.HashMap;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;


public class Program {

    public static Character intersection(String... strings) {

        for (var c : strings[0].toCharArray()) {
            boolean isCommon = true;
            for (var s : strings) {
                if (!s.contains(c + "")) {
                    isCommon = false;
                    break;
                }
            }
            if (isCommon) 
                return c;
        }

        return null;
    }

    public static HashMap<Character, Integer> priority = new HashMap<>(){{
        for (Character c = 'a'; c <= 'z'; c++) put(c, c - 'a' + 1);
        for (Character c = 'A'; c <= 'Z'; c++) put(c, c - 'A' + 26 + 1);
    }};

    public static void main(String[] args) {

        var lines = new ArrayList<String>();

        try {
            var scanner = new Scanner(new File("../input.txt"));

            while (scanner.hasNextLine()) lines.add(scanner.nextLine());
            scanner.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("input file not found");
            e.printStackTrace();
        }

        // Part 1
        int part1Sum = 0;

        for (var line : lines) {
            int middle = line.length() / 2;
            var r1 = line.substring(0, middle);
            var r2 = line.substring(middle);

            part1Sum += priority.get(intersection(r1, r2));
        }

        System.out.println("Part 1: " + part1Sum);

        // Part 2
        int part2Sum = 0;

        for (var i = 0; i < lines.size(); i += 3) {
            part2Sum += priority.get(intersection(lines.get(i), lines.get(i + 1), lines.get(i + 2)));
        }

        System.out.println("Part 2: " + part2Sum);
    }
}