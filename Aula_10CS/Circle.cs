class Circle {
    private double r;
    private double pi = 3.14;

    public void SetRadius(double v) {
        if (v > 0) this.r = v;
        else throw new ArgumentOutOfRangeException();
    }

    public double GetRadius() {
        return this.r;
    }
    public double CalcArea() {
        return r * r * pi;
    }
    public double CalcCircunferencia() {
        return 2 * r * pi;
    }
}