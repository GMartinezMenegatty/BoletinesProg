import java.util.ArrayList;

public class Empresa {
    private String razonSocial;
    private String cif;
    private String actividadePrincipal;
    private String representanteLegal;
    private ArrayList<CentroTraballo> centrosDeTraballo;

    public Empresa(String razonSocial, String cif, String actividadePrincipal, String representanteLegal) {
        this.razonSocial = razonSocial;
        this.cif = cif;
        this.actividadePrincipal = actividadePrincipal;
        this.representanteLegal = representanteLegal;
        centrosDeTraballo = new ArrayList<>();
    }
    public String getRazonSocial() {
        return razonSocial;
    }
    public void setRazonSocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }
    public String getCif() {
        return cif;
    }
    public void setCif(String nif) {
        this.cif = cif;
    }
    public String getActividadePrincipal() {
        return actividadePrincipal;
    }
    public void setActividadePrincipal(String actividadePrincipal) {
        this.actividadePrincipal = actividadePrincipal;
    }
    public String getRepresentanteLegal() {
        return representanteLegal;
    }
    public void setRepresentanteLegal(String representanteLegal) {
        this.representanteLegal = representanteLegal;
    }

    @Override
    public boolean equals(Object otra) {
        return cif.equals(((Empresa) otra).cif);
    }
    public String toString(){
        return "Razon Social: " + this.razonSocial + "CIF: " + this.cif + "Actividade Principal: " + this.actividadePrincipal +  "Representante Legal: " + this.representanteLegal;
    }

    public boolean getCentroTraballo(String nome){
        if (nome.equals(CentroTraballo.getNome())) {
            return centro;
        }
        return false;
    }

    public boolean engadeCentroTraballo(CentroTraballo centro){
        return centrosDeTraballo.add(centro);
    }

    /**
     * Metodo que retorna una lista de objetos CentroTraballo da localidade pasada por parametro
     * @param localidade
     * @return CentroTraballo
     */

    ArrayList<CentroTraballo> CentrosTraballoPorLocalidade(String localidade) {
        ArrayList<CentroTraballo> centrosTraballoPorLocalidade = new ArrayList<>();
        for (CentroTraballo centro : this.localidade) {
            if (centro.getLocalidade().equals(localidade))
                return centrosTraballoPorLocalidade;
            }
        return null;
    }

}
