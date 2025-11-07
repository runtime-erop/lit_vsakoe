
using System;
class Programm
{
    static void Main(string[] args) {}
}
class Polynominal
{
    private readonly int degree;
    private readonly  ёdouble[] coefficients;

    public Polynominal()
    {
        this.degree = 0;
        this.coefficients = [0];
    }

    public Polynominal(double[] new_coefficients)
    {
        this.degree = new_coefficients.Length - 1;
        this.coefficients = (double[])new_coefficients.Clone();
    }
    public int Degree { get; }
    public double[] Coefficients
    {
        get
        {
            return (double[])this.coefficients.Clone();
        }
    }
    public override string ToString()
    {
        string result = "";

        for (int i = degree; i >= 0; i--)
        {
            double coeff = coefficients[i];

            if (coeff == 0) continue;

            if (result != "" && coeff > 0)
                result += " + ";

            if (coeff < 0)
                result += " - ";

            double absCoeff = Math.Abs(coeff);

            if (absCoeff != 1 || i == 0)
                result += absCoeff.ToString();

            if (i > 1)
                result += $"x^{i}";
            else if (i == 1)
                result += "x";
        }

        if (result == "")
            return "0";

        return result;
    }
}
