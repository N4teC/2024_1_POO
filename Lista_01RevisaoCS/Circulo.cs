class Circulo {
    private double r, pi = 3.14;

    public void setRaio(double raio) {
        this.r = raio
    }
    public double getRaio() {
        return this.r
    }
    public double calcArea() {
        return r * r * pi;
    }
    public double calcCircunferencia() {
        return 2 * r * pi;
    }
}