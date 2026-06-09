import java.sql.*;
import java.util.ArrayList;

public class CentroTraballoDAO {
    /**
     * Xestión da táboa centro_traballo en PostgreSQL.
     */

    //  Conexión
    private static Connection conectar(String url, String usuario, String contrasinal) {
        Connection con = null;
        System.out.println("Conectando á base de datos...");
        try {
            con = DriverManager.getConnection(url, usuario, contrasinal);
        } catch (SQLException e) {
            System.out.println("Erro realizando a conexión a base de datos.\n");
        }
        System.out.println("Conexión establecida correctamente.\n");
        return con;
    }

    //  creación da táboa

    public static void crearTaboa() {
        Connection con = conectar("jdbc:postgresql://10.0.8.172:5432/usuarios", "postgres", "vboxuser");
        String sql = """
                CREATE TABLE IF NOT EXISTS centro_traballo (
                    cif         VARCHAR(9)   PRIMARY KEY,
                    nome        VARCHAR(100) NOT NULL,
                    direccion   VARCHAR(200) NOT NULL,
                    localidade  VARCHAR(100) NOT NULL,
                    provincia   VARCHAR(100) NOT NULL
                )
                """;
        try {
            Statement st = con.createStatement();
            st.execute(sql);
            con.close();
            System.out.println("Táboa 'centro_traballo' creada (ou xa existía).\n");
        } catch (SQLException e) {
            System.out.println("Erro o crear a táboa");
        }
    }

    //  inserción de datos de exemplo

    public static void inserirDatosExemplo() {
        Connection con = null;
        try {
            con = conectar("jdbc:postgresql://10.0.8.172:5432/usuarios", "postgres", "vboxuser");
            String sql = """
                     INSERT INTO centro_traballo (cif, nome, direccion, localidade, provincia)  VALUES ("B36012345", "Industrias Galicia S.L.", "Rúa do Mar 12" , "Vigo", "Pontevedra") """;
            Statement ps = con.createStatement();
            ps.executeUpdate(sql);
            sql = """                    
                     INSERT INTO centro_traballo (cif, nome, direccion, localidade, provincia)  VALUES ("A15098765", "Construcións do Norte S.A.", "Avda. da Coruña 45", "A Coruña", "A Coruña") """;
            ps.executeUpdate(sql);
            sql = """                    
                     INSERT INTO centro_traballo (cif, nome, direccion, localidade, provincia)  VALUES ("B27054321", "Servizos Lugo S.L.", "Praza Maior 3", "Lugo", "Lugo") """;

            ps.executeUpdate(sql);
            sql = """                    
                     INSERT INTO centro_traballo (cif, nome, direccion, localidade, provincia)  VALUES ("A32011223", "Tecnoloxías Ourense S.A.", "Rúa Progreso, 88", "Ourense", "Ourense") """;
            ps.executeUpdate(sql);
            sql = """                    
                     INSERT INTO centro_traballo (cif, nome, direccion, localidade, provincia)
                          VALUES ("B36099887", "Pesca e Mar Cooperativa", "Porto Pesqueiro, s/n", "Marín", "Pontevedra") """;
            ps.executeUpdate(sql);
            con.close();
            System.out.printf("Datos de exemplo insertados"); }catch (SQLException e){
            System.out.println("Erro o insertar os datos de exemplo: " + e.getMessage());
        }
    }
    public static ArrayList<CentroTraballo> importarCentrosPorCif (String cif){
        Connection con = null;
        ArrayList<CentroTraballo> centroTraballo = new ArrayList<>();
        Connection conexion = conectar("jdbc:postgresql://10.0.8.172:5432/usuarios", "postgres", "vboxuser");
        String sql = "SELECT cif FROM centro_traballo";
        try {
            PreparedStatement sentencia = conexion.prepareStatement(sql);
            sentencia.setString(1, cif);
            ResultSet consulta = sentencia.executeQuery();
            consulta.next();
            conexion.close();
        } catch (SQLException error) {
            System.out.println("Error al importar datos: " + error);
        }
        return centroTraballo;
    }
    public static void main (String [] args) {
        crearTaboa();
        inserirDatosExemplo();
    }
}
