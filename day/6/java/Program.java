import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.stream.Collectors;


public class Program {

    public static int getMarkerLocation(String stream, int block_size) {
        String packet = "0".repeat(block_size);

        for (int i = 0; i < stream.length(); ++i) {
            packet = packet.substring(1) + stream.charAt(i);
            
            if (packet.chars().mapToObj(c -> (char) c)
                .collect(Collectors.toSet()).size() == block_size) {
                return i + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        try {
            var scanner = new Scanner(new File("../input.txt"));
            var stream = scanner.nextLine();
            scanner.close();

            System.out.println("Part 1: " + getMarkerLocation(stream, 4));
            System.out.println("Part 2: " + getMarkerLocation(stream, 14));

        }
        catch (FileNotFoundException e) {
            System.out.println("input file not found");
            e.printStackTrace();
        }
    }
}