import java.util.Arrays;
import java.util.Scanner;

public class triangles {

    static final class Triangle implements Comparable<Triangle> {
        final int a;
        final int b;
        final double g;

        Triangle(final int a, final int b, final double g) {
            this.a = a;
            this.b = b;
            this.g = g;
        }

        @Override
        public int compareTo(final Triangle o) {
            return Double.compare(g, o.g);
        }
    }

    public static void main(final String... args) {

        final Scanner sc = new Scanner(System.in);
        final int N = 6 * Integer.parseInt(sc.next());
        final Triangle[] triangle = new Triangle[N];
        for (int i = 0; i < N; i += 6) {
            final int a = Integer.parseInt(sc.next());
            final int b = Integer.parseInt(sc.next());
            final int c = Integer.parseInt(sc.next());
            final double g = Double.parseDouble(sc.next());
            triangle[i] = new Triangle(a, b, g);
            triangle[i+1] = new Triangle(b, a, g);
            triangle[i+2] = new Triangle(a, c, g);
            triangle[i+3] = new Triangle(c, a, g);
            triangle[i+4] = new Triangle(b, c, g);
            triangle[i+5] = new Triangle(c, b, g);
        }
        Arrays.sort(triangle);
        final int[] table = new int[N];
        Arrays.fill(table, 1);
        int max = 1;
        for (int i = 1; i < N; ++i) {
            final Triangle ti = triangle[i];
            final int tia = ti.a;
            final double tig = ti.g;
            for (int j = 0; j < i; ++j) {
                final Triangle tj = triangle[j];
                if (tia == tj.b && tig > tj.g)
                    table[i] = Math.max(table[i], 1 + table[j]);
            }
            max = Math.max(max, table[i]);
        }
        System.out.println(max);
    }

}
