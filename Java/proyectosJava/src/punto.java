public class punto {
    private double x;
    private double y;

    public punto(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public double getX() {
        return x;
    }
    public double getY() {
        return y;
    }
    public void setX(double x) {
        this.x = x;
    }
    public void setY(double y) {
        this.y = y;
    }

    @Override
    public String toString () {
        return "X: " + x + " Y: " + y;
    }

    public static void main(String [] args) {
        punto p1 = new punto(1, 3);
    }
}
