public class Punto2 implements Area {
    private int x;
    private int y;

    public Punto2(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int getX() {
        return x;
    }
    public void setX(int x) {this.x = x;}

    public int getY() {
        return y;
    }
    public void setY(int y) {
        this.y = y;
    }

    @Override
    public String toString () {
        return "X: " + x + " Y: " + y;
    }

    public static void main(String [] args) {
        Punto2 p1 = new Punto2(2, 3);
        System.out.println(p1.calcularArea());
    }
}

