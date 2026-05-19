interface Son {
    void voz ();
}

interface Viviparo {
    boolean viviparo = true;
}

public class Animal implements Comparable<Animal>{
    int numPatas;

    public Animal(int patas) {
        numPatas = patas;
    }
    public static void rascarConPata (){
        System.out.println("Ras, ras, ras");
    }

    @Override
    public int compareTo(Animal outro) {
        if (this.numPatas==outro.numPatas)return 0;
        else return this.numPatas-outro.numPatas;
    }
    public static void main(String [] args) {
        Animal can = new Animal(4);
        Animal serpe = new Animal(0);
        System.out.println(can.compareTo(serpe));
    }
}
