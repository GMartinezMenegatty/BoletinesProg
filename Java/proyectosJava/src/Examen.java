import java.util.ArrayList;
import java.util.Scanner;

//public class Examen{
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        ArrayList<ListaReproducion> ListaDeReproducion = new ArrayList<>();
//        int opcion = 0;
//
//        while (opcion != 6) {
//            System.out.println("\n--- Lista de Reproduccion ---");
//            System.out.println("1. Engadir Cancion");
//            System.out.println("2. Eliminar Cancion");
//            System.out.println("3. Buscar lista cancions por autor");
//            System.out.println("4. Reproducir Cancion");
//            System.out.println("5. Mostrar lista de canciones");
//            System.out.println("6. Salir");
//            System.out.print("Selecciona unha opción: ");
//
//            opcion = sc.nextInt();
//
//            if (opcion == 1) {
//                System.out.println("Introduce una cancion: ");
//                String cancion = sc.nextLine();
//                ListaDeReproducion.add(cancion);
//                System.out.println("Cancion añadida.");
//
//            }else if (opcion == 2) {
//                System.out.print("Nombre de la cancion a borrar: ");
//                String borrar = sc.nextLine();
//
//                ListaDeReproducion.removeIf(cancion -> cancion.equals(borrar));
//
//            }else if (opcion == 3) {
//                System.out.println("Busca a un autor: ");
//                String autor = sc.nextLine();
//                if(ListaDeReproducion.contains(autor)){
//
//                }
//
//            }else if (opcion == 4) {
//                for (ListaReproducion cancion : ) {
//                    System.out.println(cancion);
//                    }
//
//            }else if (opcion == 5) {
//                System.out.println(ListaDeReproducion);
//
//            }else if (opcion == 6) {
//                System.out.println("Saliendo del sistema, hasta la proxima...");
//
//            }else{
//                System.out.println("Opcion incorrecta");
//            }
//        }
//        sc.close();
//    }
//}
