package Sorting.quick;

public class Main {
    public static void main(String[] args) {
        int infinity = 5000000;
        int arr[] = {5, 4, 3, 2, 1, infinity};
        QuickSort qs = new QuickSort();
        qs.sort(arr, 0, arr.length-1);
        
        for (int x:arr) if (x!=infinity) System.out.println(x);
        
    }
}

class QuickSort {
    void sort(int arr[], int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            sort(arr, low, pi);
            sort(arr, pi+1, high);
        }
    }

    int partition(int arr[], int low, int high)  {
        int pi = arr[low];
        int p = low;
        int q = high;

        while (p < q) {
            while (arr[p] <= pi) {
                p++;
            }
            while (arr[q] > pi) {
                q--;
            }
            if (p <  q) {
                swap(arr, p, q);
            }
        }
        swap(arr, low, q);
        return q;
    }

    void swap(int arr[], int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
