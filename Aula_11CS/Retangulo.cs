using System;

class Retangulo{
    private double b;
    private double h;

    public void SetBase(double b){
        if (b > 0) this.b = b;
        else throw new ArgumentOutOfRangeException();
    }
    public void SetAltura(double h){
        if (h > 0) {
            this.h = h;
        } else throw new ArgumentOutOfRangeException();
    }
    public double GetBase() {
        return this.b;
    }    
    public double GetAltura() {
        return this.h;
    }
    public double CalcArea() {
        return this.GetAltura() * this.GetBase();
    }

    public double CalcDiagonal() {
        return (Math.Sqrt((this.GetAltura() * this.GetAltura()) + (this.GetBase() * this.GetBase())));
    }

    public override string ToString() {
        return $"Base = {this.GetBase()} Altura = {this.GetAltura()}";
    }

}