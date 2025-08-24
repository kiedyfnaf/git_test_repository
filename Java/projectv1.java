public class Main{
    public static void main(String[] args) {
        Bolo bolognese = new Bolo();
        bolognese.cook();
    }
}

class Noodle {
    public String texture;
    public String shape;
    public double length;
    protected String[] ingredients;
    protected String color = "white";
    Noodle(String t, String s, double l, String[] i) {
        this.texture = t;
        this.shape = s;
        this.length = l;
        this.ingredients = i;
    }
    public void cook() {
        System.out.println("Cooking noodles.");
        this.texture = "cooked";
    }
}

class Bolo extends Noodle {
    Bolo() {
        super("soft", "string", 10.5, new String[]{"egg","flour","water"});
        this.color= "orange";
    }
    public void cook() {
        System.out.println("Cooking noodles");
        this.texture = "overcooked";
    }
}