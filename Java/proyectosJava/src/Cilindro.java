public class Cilindro extends Circulo2{
    private int volumen;

    public Cilindro(int x, int y, int r,  int volumen) {
        super(x, y, r);
        this.volumen = volumen;
    }

    public int getVolumen (){
        return volumen;
    }
}

