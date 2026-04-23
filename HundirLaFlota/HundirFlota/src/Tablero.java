import java.util.Random;

public class Tablero {
    private char [][] tablero;
    private int numeroBarcos;

    public Tablero(int dimension, int barcos){
        tablero = new char[dimension][dimension];
        numeroBarcos = barcos;
        iniciarTablero(barcos);
    }

    public int getNumeroBarcos (){
        return numeroBarcos;
    }

    public char getCasilla(int x, int y){
        return tablero [x][y];
    }

    public void setCasilla(int x, int y, char simbolo){
        tablero[x][y] = simbolo;
    }

    private void iniciarTablero(int numBarcos){
        for (int i = 0; i < tablero.length; i++){
            for (int j = 0; j < tablero[0].length; j++){
                tablero [i][j] = '\u007E';
            }
        }
        for (int i = 0; i < numBarcos; i++){
            Random r = new Random();
            while (true) {
                int x = r.nextInt(tablero.length );
                int y = r.nextInt(tablero.length );
                if (tablero[x][y]!='B'){
                    tablero[x][y] = 'B';
                    break;
                }
            }
        }
    }
    public void mostrarLinha(int dimension){
        for (int i=0; i < dimension; i++){
            System.out.print("+-");
        }
        System.out.println("+");
    }
    public void mostrarTablero(boolean xogo){
        mostrarLinha(tablero[0].length);
        for (int i=0; i < tablero.length; i++){
            for (int j=0; j < tablero[0].length; j++) {
                char simbolo = tablero[i][j];
                if (tablero[i][j] == 'B' && xogo) {
                    simbolo = '\u007E';

                }
                System.out.print("|" + simbolo);
            }
            System.out.println("|");
        }
        mostrarLinha(tablero[0].length);
    }




    public static void main (String[] args){
        Tablero t= new Tablero(4, 4);
        t.iniciarTablero(4);
        t.mostrarTablero(true);
    }
}
