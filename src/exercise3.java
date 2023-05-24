public class exercise3 {
    public double addThreeNumbers(double num1, double num2, double num3)
    {
        double result;
        result = num1 + num2 + num3;
        return result;
    }

    public static void main(String[] args){
        exercise3 object = new exercise3();
        double result;
        result = object.addThreeNumbers(3.0, 4.5, 6.3);
        System.out.print(result);
    }
}
