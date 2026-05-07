public class Circulo extends PuntoAbstract{
    public static final double PI = 3.141592;
    private int radio;

    public Circulo(int x, int y, int r) {
        super(x, y);
        radio = r;
    }

    public int getRadio (){
        return radio;
    }

    public void setRadio (int radio) {
        this.radio = radio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * Math.pow(radio, 2);
    }

    @Override
    public double calcularPerimetro(){
        return 2 * Math.PI * radio;
    }

    public String toString(){
        return super.toString() + "\nradio: " + radio;
    }
}
