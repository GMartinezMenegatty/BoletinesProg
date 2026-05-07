public class Can extends Animal implements Son, Viviparo{
    public Can(int patas) {
        super(patas);
    }

    public void voz(){
        System.out.println("Guau, Guau");
    }

    public static void main (String[] args) {
        Can c1 = new Can(4);
        System.out.println(Can.viviparo);
        Animal.rascarConPata();
    }
}

