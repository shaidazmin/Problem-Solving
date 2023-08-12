
class Compute
{
    String average(int A[], int N)
    {
        float sum = 0;
        for (int i = 0; i < N; i++) {
            sum += A[i];
        }
        double avg = sum / N;
        double roundedAvg = Math.round(avg * 100.0) / 100.0;
        return String.format("%.2f", roundedAvg);
        
    }
}