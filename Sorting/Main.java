package Sorting;

public class Main {
  public static void main(String[] args) {
      int arr[] = {45, 25, 31, 66, 54, 87};
      MergeSort ms = new MergeSort();
      int[] sortedArray = ms.sort(arr);
      for (int x: sortedArray) {
          System.out.println(x);
      }
  }
}

class MergeSort {
  public int[] sort(int[] arr) {
      if (arr.length <= 1) return arr;

      int mid = arr.length / 2;

      int[] L = new int[mid];
      int[] R = new int[arr.length - mid];

      for (int i = 0, j = 0; i < arr.length; i++) {
          if (i < mid) {
              L[i] = arr[i];
          }
          else {
              R[j++] = arr[i];
          }
      }

      int lsa[] = sort(L);
      int rsa[] = sort(R);

      return merge(lsa, rsa);
  }

  public int[] merge(int[] L, int[] R) {
      int n = L.length + R.length;
      int[] sorted = new int[n];

      int i = 0, j = 0, k = 0;

      while (i < L.length && j < R.length) {
          if (L[i] < R[j]) {
              sorted[k++] = L[i++];
          }
          else {
              sorted[k++] = R[j++];
          }
      }

      while (i < L.length) sorted[k++] = L[i++];
      while (j < R.length) sorted[k++] = R[j++];

      return sorted;
  }
}
