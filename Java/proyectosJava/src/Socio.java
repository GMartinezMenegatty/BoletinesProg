import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Date;

public class Socio extends Persoa2{
    public LocalDate data_Alta;


    public Socio(String nome, String dni, int edade, String dAlta) {
        super(nome, dni, edade);
        DateTimeFormatter f = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        data_Alta = LocalDate.parse(dAlta, f);
    }

    public int antiguedade(){
        return (int)data_Alta.until(LocalDate.now(), ChronoUnit.YEARS);
    }

    public

}
