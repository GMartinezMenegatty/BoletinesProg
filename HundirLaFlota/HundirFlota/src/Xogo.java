public class Xogo {
    private int intentosMaximos;
    private int disparos;
    private int puntos;
    private Tablero tablero;

    public Xogo(int dimensions, int numIntentos, int numBarcos) {
        tablero = new Tablero(dimensions, numBarcos);
        intentosMaximos = numIntentos;
        disparos = 0;
        puntos = 0;
    }

    public int getPuntos (){
        return puntos;
    }

    public boolean disparar (int x, int y){
        incrementarDisparos();
        if (tablero.getCasilla(x,y) == 'B'){
            tablero.setCasilla(x,y,'X');
            incrementarDisparos();
            return true;
        }
        else {
            tablero.setCasilla(x,y,'O');
        }
        return false;
    }

    private void incrementarDisparos () {
        disparos++;
    }

    private void incrementarPuntos () {
        puntos++;
    }

    public void mostrarTablero (boolean xogo){
        tablero.mostrarTablero(xogo);
    }


    public static void main (String[] args){
        Xogo x = new Xogo(8, 12, 8);
        x.mostrarTablero(false);
        x.disparar(3,4);
        x.mostrarTablero(true);
    }
}


