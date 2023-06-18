//Complete this code or write your own from scratch
import java.io.*;
import java.util.Scanner;
import java.util.HashMap;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        java.util.HashMap<String, Integer> map = new  HashMap<String, Integer>();
        for(int i = 0; i < n; i++){
            String name = in.next();
            int phone = in.nextInt();
            // Write code here
            map.put(name, phone);
        }
        while(in.hasNext()){
            String s = in.next();
            // Write code here
            if (map.containsKey(s)) {
                System.out.print(map.get(s));
            } else {

                System.out.print("Not Found");
            }
        }
        in.close();
    }
}