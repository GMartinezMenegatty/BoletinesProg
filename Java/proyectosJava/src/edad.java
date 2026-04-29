import java.util.Arrays;

public class edad {
    public static void main (String args[]){
        int []edad = {25, 27, 28, 22, 24, 29};
        Arrays.sort (edad);
        System.out.println(Arrays.toString (edad));
        int encontrar = 27;
        int i=0;
        boolean encontrado = false;
        for (; i<edad.length; i++){
            if (edad[i]==encontrar){
                encontrado = true;
                break;
            }
        }
        if (encontrado) {
            System.out.println("Esta na posicion: "+ i);
        }
        else {
            System.out.println("Non foi encontrado");
        }
        System.out.println();
    }
}
