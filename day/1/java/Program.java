import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;


public class Program {
    public static void main(String[] args) {

        var elves = new ArrayList<ArrayList<Integer>>() {{
            add(new ArrayList<Integer>());
        }};

        int index = 0;

        try {
            var scanner = new Scanner(new File("../input.txt"));

            while (scanner.hasNextLine()) {
                var line = scanner.nextLine();

                if (line.length() == 0) {
                    elves.add(new ArrayList<Integer>());
                    index += 1;
                }
                else {
                    elves.get(index).add(Integer.parseInt(line));
                }
            }
            scanner.close();
        }
        catch (FileNotFoundException e) {
            System.out.println("input file not found");
            e.printStackTrace();
        }

        var sums = new ArrayList<Integer>();

        for (var elf : elves) {
            Integer sum = 0;
            for (var food_item : elf) sum += food_item;
            sums.add(sum);
        }
        
        Collections.sort(sums, Collections.reverseOrder());

        System.out.println("Part 1: " + sums.get(0));
        System.out.println("Part 2: " + (sums.get(0) + sums.get(1) + sums.get(2)));
    }
}