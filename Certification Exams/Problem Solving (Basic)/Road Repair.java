

 -- Road Repair



import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;



class Result {

    public static long getMinCost(List<Integer> crew_id, List<Integer> job_id) {

        long cost=0;
        Collections.sort(crew_id);
        Collections.sort(job_id);
        int len1=crew_id.size();
        int len2=job_id.size();
        if(len1==len2)
        {
            for(int i=0;i<len1;i++)
                {
                    if(job_id.get(i)>=crew_id.get(i))
                        {
                            cost=cost+(job_id.get(i)-crew_id.get(i));
                        }

                    else if(job_id.get(i)<crew_id.get(i))
                        {
                            cost=cost+(crew_id.get(i)-job_id.get(i));
                        }
                }
        }
        return cost;

    } 

}


public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int crew_idCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> crew_id = new ArrayList<>();

        for (int i = 0; i < crew_idCount; i++) {
            int crew_idItem = Integer.parseInt(bufferedReader.readLine().trim());
            crew_id.add(crew_idItem);
        }

        int job_idCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> job_id = new ArrayList<>();

        for (int i = 0; i < job_idCount; i++) {
            int job_idItem = Integer.parseInt(bufferedReader.readLine().trim());
            job_id.add(job_idItem);
        }

        long result = Result.getMinCost(crew_id, job_id);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

