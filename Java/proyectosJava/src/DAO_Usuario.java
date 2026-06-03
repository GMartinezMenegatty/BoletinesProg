import java.sql.DriverManager;
import java.sql.*;
import java.util.Scanner;

public class DAO_Usuario {
    private static Connection conectaDB(String ip, int port, String nomebd, String usuario, String contraseña) {
        Connection con = null;
        String url = "jdbc:postgresql://" + ip.strip() + ":" + port + "/" + nomebd;
        try {
            con = DriverManager.getConnection(url, usuario, contraseña);
        } catch (SQLException e) {
            System.out.println("Erro o conectar co servidor" + ip + ":" + port);
        }
        return con;


    }

    public static void crearUsuarioBD(Persoa3 usuario) {
        if (usuario != null) {
            Connection conexion = conectaDB("10.0.8.172", 5432, "usuarios", "postgres", "vboxuser");
            String sql = "INSERT INTO persoas(nome, dni, edade) VALUES (?,?,?)";
            try {
                PreparedStatement sentencia = conexion.prepareStatement(sql);
                sentencia.setString(1, usuario.getNome());
                sentencia.setString(2, usuario.getDni());
                sentencia.setInt(3, usuario.getEdade());
                sentencia.executeUpdate();
                conexion.close();
            } catch (SQLException e) {
                System.out.println("Erro o insertar o usuario");
            }
        }

    }


    public static Persoa3 obterUsuario(String dni) {
        Persoa3 p = null;
        if (dni != null || dni.length() != 0) {
            Connection conexion = conectaDB("10.0.8.172", 5432, "usuarios", "postgres", "vboxuser");
            String sql = "SELECT nome, dni, edade FROM persoas WHERE dni = ?";
            try {
                PreparedStatement sentencia = conexion.prepareStatement(sql);
                sentencia.setString(1, dni);
                ResultSet consulta = sentencia.executeQuery();
                consulta.next();
                String nom = consulta.getString("nome");
                String d = consulta.getString("dni");
                int ed = consulta.getInt("edade");
                p = new Persoa3(nom, d, ed);
                conexion.close();
            } catch (SQLException erro) {
                System.out.println("Erro o insertar o usuario: " + erro);
            }
        }
        return p;
    }
    public static void modificarUsuario (String dni, String novoNome, int novaEdade) {
        if (dni != null || dni.length() != 0) {
            Connection conexion = conectaDB("10.0.8.172", 5432, "usuarios", "postgres", "vboxuser");
            String sql = "SELECT nome, dni, edade FROM persoas WHERE dni = ?";

            try {
                PreparedStatement sentencia = conexion.prepareStatement(sql, ResultSet.TYPE_SCROLL_SENSITIVE,ResultSet.CONCUR_UPDATABLE);
                sentencia.setString(1, dni);
                ResultSet consulta = sentencia.executeQuery();
                if (consulta.first()){
                    consulta.updateString("nome", novoNome);
                    consulta.updateInt("edade", novaEdade);
                    consulta.updateRow();
                }
                conexion.close();
            } catch (SQLException erro) {
                System.out.println("Erro o modificar usuario: " + erro);
            }
        }
    }

}