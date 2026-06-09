public class CentroTraballo implements Comparable<CentroTraballo>{
    private String nome;
    private String direccion;
    private String localidade;
    private String provincia;

    public CentroTraballo(String nome, String direccion, String localidade, String provincia) {
        this.nome = nome;
        this.direccion = direccion;
        this.localidade = localidade;
        this.provincia = provincia;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getDireccion() {
        return direccion;
    }
    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    public String getLocalidade() {
        return localidade;
    }
    public void setLocalidade(String localidade) {
        this.localidade = localidade;
    }
    public String getProvincia() {
        return provincia;
    }
    public void setProvincia(String provincia) {
        this.provincia = provincia;
    }

    public String toString(){
        return "CentroTraballo: " + nome + ", " + direccion + ", " + localidade + ", " + provincia ;
    }

    @Override
    public int compareTo(CentroTraballo otroCentroTraballo) {
        return this.nome.compareTo(otroCentroTraballo.getNome()) + this.provincia.compareTo(otroCentroTraballo.getProvincia())  +
                this.localidade.compareTo(otroCentroTraballo.getLocalidade()) + this.direccion.compareTo(otroCentroTraballo.getDireccion());

    }
}
