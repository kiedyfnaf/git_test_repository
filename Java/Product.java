import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

class Product {
    String name;

    public Product(String name) {
        this.name = name;
    }

    public String toString() {
        return "Product: " + name;
    }
}

class iPhone extends Product {
    double screenSize;
    String processor;
    String typeOfModem;
    String color;
    String memory;
    boolean is3DTouchTechnology;
    double price;

    public iPhone(String name, double screenSize, String processor, String typeOfModem, String color, String memory, boolean is3DTouchTechnology, double price) {
        super(name);
        this.screenSize = screenSize;
        this.processor = processor;
        this.typeOfModem = typeOfModem;
        this.color = color;
        this.memory = memory;
        this.is3DTouchTechnology = is3DTouchTechnology;
        this.price = price;
    }
    
    public String toString() {
        return "iPhone: " + name + " | " + screenSize + " | $" + price + " | " + memory + "GB | " + color + 
               " | Has 3D touch technology: " + is3DTouchTechnology + " | Type of modem: " + typeOfModem + " | Processor: " + processor;
    }
}

class iPad extends Product {
    double screenSize;
    String processor;
    boolean is4G;
    String color;
    String memory;
    double price;

    public iPad(String name, double screenSize, String processor, boolean is4G, String color, String memory, double price) {
        super(name);
        this.screenSize = screenSize;
        this.processor = processor;
        this.is4G = is4G;
        this.color = color;
        this.memory = memory;
        this.price = price;
    }
    
    public String toString() {
        return "iPad: " + name + " | " + screenSize + " | $" + price + " | " + memory + "GB | " + color + 
               " | Has 4G: " + is4G + " | Processor: " + processor;
    }
}

class ProductReader {
    public static void main(String[] args) {
        ArrayList<Product> productList = new ArrayList<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader("apple.txt"));
            String line;

            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");

                if (parts.length == 7) {
                    String name = parts[0].trim();
                    double screenSize = Double.parseDouble(parts[1].trim());
                    String processor = parts[2].trim();
                    boolean is4G = Boolean.parseBoolean(parts[3].trim());
                    String color = parts[4].trim();
                    String memory = parts[5].trim();
                    double price = Double.parseDouble(parts[6].trim());

                    // Create iPad object and add it to the list
                    productList.add(new iPad(name, screenSize, processor, is4G, color, memory, price));
                } 
                else if (parts.length == 8) {
                    String name = parts[0].trim();
                    double screenSize = Double.parseDouble(parts[1].trim());
                    String processor = parts[2].trim();
                    String typeOfModem = parts[3].trim();
                    String color = parts[4].trim();
                    String memory = parts[5].trim();
                    boolean is3DTouchTechnology = Boolean.parseBoolean(parts[6].trim());
                    double price = Double.parseDouble(parts[7].trim());

                    // Create iPhone object and add it to the list
                    productList.add(new iPhone(name, screenSize, processor, typeOfModem, color, memory, is3DTouchTechnology, price));
                }
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("Error reading the file.");
            e.printStackTrace();
        }

        // Print all products
        for (Product p : productList) {
            System.out.println(p);
        }
    }
}
