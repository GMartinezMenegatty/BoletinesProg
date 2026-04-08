import java.util.Scanner;

public class bucles {
    public static void main (String[]args){
        //Bucle while
        int contador = 0;
        while (contador <= 5){
            System.out.println("Bucle while " + contador);
            contador++;
        }

        //Bucle do-while
        contador = 0;
        do{
            System.out.println("Bucle do-while " + contador);
            contador++;
        } while (contador <= 5);


        Scanner teclado = new Scanner (System.in);
        int opcion = 0;
        while (opcion != 3) {
            System.out.println("Elixe unha opcion");
            System.out.println("1.Saudar");
            System.out.println("2.Despedirse");
            System.out.println("3.Sair");
            String op = teclado.nextLine();
            opcion = Integer.parseInt(op);
        }
        for (int i = 5; i<20; i+=3){
            System.out.println("Indice: "+i);
        }
    }
}
