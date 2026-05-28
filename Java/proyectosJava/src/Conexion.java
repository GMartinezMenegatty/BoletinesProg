import java.sql.*;

public class Conexion {
    public static void main (String [] args){
        Connection conexion;
        Statement sentencia;
        String sql;
        String url = "jdbc:postgresql://10.0.8.172:5432/usuarios";
        try {
            conexion = DriverManager.getConnection(url,"postgres", "vboxuser");
            System.out.println("Conectado");
            String crearTaboaSql = " CREATE TABLE persoas (nome VARCHAR(50), dni VARCHAR (9), edade INTEGER);";

            sentencia = conexion.createStatement();
            //sentencia.execute(crearTaboaSql); solo se ejecuta 1 vez para crear la tabla

            sentencia.executeUpdate("INSERT INTO persoas (nome, dni, edade)"
                                         + "VALUES ('Pepe', '1234J', 23);");
            sentencia.executeUpdate("INSERT INTO persoas (nome, dni, edade)"
                                         + "VALUES ('Ana', '1234H', 24);");
            sentencia.executeUpdate("INSERT INTO persoas (nome, dni, edade)"
                                         + "VALUES ('Juan', '1234K', 25);");


        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
