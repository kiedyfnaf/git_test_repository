import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

abstract class Shelter {
    String id;
    int volumeInM3;
    boolean availability;

    public Shelter(String id,int volumeInM3,boolean availability) {
        this.id = id;
        this.volumeInM3 = volumeInM3;
        this.availability = availability;
    }

    public String toString() {
        return "Id: " + id + " | Volume: " + volumeInM3 + " | Avaliability: " + availability;
    }
}

class CoastalShelter extends Shelter {
    int landSurfaceArea;
    final String waterType = "Cool Eutropic";
    final String climate = "Temperate";

    public CoastalShelter(String id, int volumeInM3, boolean availability,int landSurfaceArea) {
        super(id, volumeInM3, availability);
        this.landSurfaceArea = landSurfaceArea;
    }

    public String toString() {
        return "Land surface area: " + landSurfaceArea + " | Water type: " + waterType + " | Climate: " + climate;
    }
}

class TundraShelter extends Shelter {
    final String waterType = "Cool Eutrophic";
    final String climate = "Polar";

    public TundraShelter(String id,int volumeInM3,boolean availability) {
        super(id, volumeInM3, availability);
    }

    public String toString() {
        return "Water type: " + waterType + " | Climate: " + climate;
    }
}

class ReefShelter extends Shelter {
    int numberOfUniqueCoralTypes;
    final String waterType = "Warm Trophic";
    final String climate = "Tropical";

    public ReefShelter(String id, int volumeInM3, boolean availability, int numberOfUniqueCoralTypes) {
        super(id, volumeInM3, availability);
        this.numberOfUniqueCoralTypes = numberOfUniqueCoralTypes;
    }

    public String toString() {
        return "Number of unique coral types: " + numberOfUniqueCoralTypes + " | Water type: " + waterType + " | Climate: " + climate;
    }
}

public class ShelterReader {
    public static void main(String[] args) {
        ArrayList<Shelter> shelterList = new ArrayList<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader("Shelters.txt"));
            String line;

            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(" ");

                if (parts[0].equals("Coastal")) {
                    String id = parts[1];
                    int volumeInM3 = Integer.parseInt(parts[2]);
                    boolean availability = Boolean.parseBoolean(parts[3]);
                    int landSurfaceArea = Integer.parseInt(parts[4]);

                    shelterList.add(new CoastalShelter(id, volumeInM3, availability, landSurfaceArea));
                }
                else if (parts[0].equals("Tundra")) {
                    String id = parts[1];
                    int volumeInM3 = Integer.parseInt(parts[2]);
                    boolean availability = Boolean.parseBoolean(parts[3]);

                    shelterList.add(new TundraShelter(id, volumeInM3, availability));
                }
                else if (parts[0].equals("Reef")) {
                    String id = parts[1];
                    int volumeInM3 = Integer.parseInt(parts[2]);
                    boolean availability = Boolean.parseBoolean(parts[3]);
                    int numberOfUniqueCoralTypes = Integer.parseInt(parts[4]);

                    shelterList.add(new ReefShelter(id, volumeInM3, availability, numberOfUniqueCoralTypes));
                }
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("Problem found while reading the file.");
            e.printStackTrace();
        }

        for (Shelter p : shelterList) {
            System.out.println(p);
        }
    }
}