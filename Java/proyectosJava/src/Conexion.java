import java.sql.*;
import java.util.Scanner;

public class Conexion {
    public static void main (String [] args){
        Connection conexion;
        Statement sentencia;
        ResultSet resultados;
        PreparedStatement sentenciaP;
        String sql;
        String url = "jdbc:postgresql://10.0.8.172:5432/usuarios";
        try {
            conexion = DriverManager.getConnection(url,"postgres", "vboxuser");
            System.out.println("Conectado");
            String crearTaboaSql = " CREATE TABLE persoas (nome VARCHAR(50), dni VARCHAR (9) PRIMARY KEY, edade INTEGER);";

            sentencia = conexion.createStatement();
            //sentencia.execute(crearTaboaSql); solo se ejecuta 1 vez para crear la tabla

//            sentencia.executeUpdate("INSERT INTO persoas (nome, dni, edade)"
//                                         + "VALUES ('Pepe', '1234J', 23);");
//            sentencia.executeUpdate("INSERT INTO persoas (nome, dni, edade)"
//                                         + "VALUES ('Ana', '1234H', 24);");
//            sentencia.executeUpdate("INSERT INTO persoas (nome, dni, edade)"
//                                         + "VALUES ('Juan', '1234K', 25);");

            sql = "INSERT INTO persoas(nome, dni, edade) VALUES (?,?,?)";
            sentenciaP = conexion.prepareStatement(sql);
            sentenciaP.setString(1,"Roque3");
            sentenciaP.setString(2,"123452");
            sentenciaP.setInt(3,28);
            //sentenciaP.executeUpdate(); Para que se haga lo de arriba de sql y eso
            sql = "SELECT nome, dni, edade FROM persoas";
            sentenciaP = conexion.prepareStatement(sql);
            resultados = sentenciaP.executeQuery();
            if (resultados.isBeforeFirst()) System.out.println("Estoy antes del primer registro");
            while(resultados.next()){
                if (resultados.isFirst()) System.out.println("Este es el primer registro");
                else if (resultados.isLast()) System.out.println("Este es el ultimo registro");
                String n = resultados.getString("nome");
                String d = resultados.getString("dni");
                int e = resultados.getInt("edade");
                System.out.println("Nombre: "+n+", dni: "+d+", edade: "+e);
            }
            if (resultados.isAfterLast()) System.out.println("Estoy despues del ultimo registro");
            resultados.close();
            sentenciaP.close();
            conexion.close();
            //Usando objeto DAO
            //DAO_Usuario.crearUsuarioBD(new Persoa3 ("Victor", "8888B", 45));
            System.out.println(DAO_Usuario.obterUsuario("8888B"));
            Scanner teclado = new Scanner(System.in);
            System.out.println("Escribe o novo nome: ");
            String novoNome = teclado.nextLine();
            System.out.println("Escribe a nova edade: ");
            int novaEdade = teclado.nextInt();
            DAO_Usuario.modificarUsuario("8888B", novoNome, novaEdade);
            System.out.println(DAO_Usuario.obterUsuario("8888B"));




        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
