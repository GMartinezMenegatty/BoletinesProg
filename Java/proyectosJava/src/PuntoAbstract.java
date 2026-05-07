public abstract class PuntoAbstract {
    private int x;
    private int y;

    public PuntoAbstract(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
    public void setX(int x) {
        this.x = x;
    }
    public void setY(int y) {
        this.y = y;
    }

    public abstract double calcularArea();

    public abstract double calcularPerimetro();

    public static void main(String [] args) {
//    PuntoAbstract p1 = new PuntoAbstract(1, 3);
    }
}
