public class FruitTest {
    public static void main(String[] args) {
        Fruit f = new Fruit("Mango", 50, 35.5);

        System.out.println("Name: " + f.getFruit());
        System.out.println("Quantity: " + f.getQuantity());
        System.out.println("Price: " + f.getPrice());

        f.setQuantity(45);
        f.setPrice(40.0);
        System.out.println("After update -> Quantity: " + f.getQuantity() + ", Price: " + f.getPrice());
    }
}