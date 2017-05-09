import java.util.Scanner;
import java.io.*;

public class DataGrabber{
	
	static Scanner reader;
	static Scanner reader2;
	static PrintWriter printer;
	static String[] tokens;
	static String[] ID;
	static int a;
	
	public static void main(String [] args) throws IOException {
		
		reader = new Scanner(new File("yelp_academic_dataset_business.json"));
		printer = new PrintWriter("ARIZONA_yelp_academic_dataset_business.json");
		String line = "";
		int numberOfLinesInNewFile = 0;
		
		while(reader.hasNextLine()){
			line = reader.nextLine();
			
			tokens = line.split(",");
			
			if(tokens[1].contains("\"state\":\"AZ\"") ||tokens[2].contains("\"state\":\"AZ\"")||
				tokens[3].contains("\"state\":\"AZ\"")||tokens[4].contains("\"state\":\"AZ\"")||
				tokens[5].contains("\"state\":\"AZ\"")||tokens[6].contains("\"state\":\"AZ\"")||
				tokens[7].contains("\"state\":\"AZ\"")||tokens[8].contains("\"state\":\"AZ\"")||
				tokens[9].contains("\"state\":\"AZ\"")||tokens[10].contains("\"state\":\"AZ\"")){
				numberOfLinesInNewFile++;
				printer.println(line);
				
				}
			}
			printer.close();
			
			ID = new String[numberOfLinesInNewFile];
			reader = new Scanner(new File("ARIZONA_yelp_academic_dataset_business.json"));
			line = "";
			int counter = 0;
			while(reader.hasNextLine()){
				line = reader.nextLine();
				String[] tokensLocal = line.split(",");
				String id = tokensLocal[0].substring(16, tokensLocal[0].length()-1);
				//System.out.println(id);
				
				ID[counter] = id;
				counter++;
				
				}
			

			//---------------------------------------------------------------------
			
		reader2 = new Scanner(new File("yelp_academic_dataset_checkin.json"));
		printer = new PrintWriter("ARIZONA_yelp_academic_dataset_checkin.json");
		line = "";
		//a = 0;
		while(reader2.hasNextLine()){
			line = reader2.nextLine();
			tokens = line.split(",");
			
			String y = tokens[tokens.length-2].substring(15, tokens[tokens.length-2].length()-1);
			
			if(idTokenFound(y)){
				printer.println(line);
				}
			else{
				;
				}
				
			//a++;			
			//System.out.println(a);
			
		}
		printer.close();
	
	
			//---------------------------------------------------------------------
	
		reader2 = new Scanner(new File("yelp_academic_dataset_review.json"));
		printer = new PrintWriter("ARIZONA_yelp_academic_dataset_review.json");
		line = "";
		//a = 0;
		while(reader2.hasNextLine()){
				
			line = reader2.nextLine();
			tokens = line.split(",");
			
			
			String y = tokens[2].substring(15, tokens[2].length()-1);
			
			if(idTokenFound(y)){
				printer.println(line);
				}
			else{
				;
				}
				
			//a++;
			//System.out.println(a);

		}
		printer.close();
		
			//---------------------------------------------------------------------

		
		reader2 = new Scanner(new File("yelp_academic_dataset_tip.json"));
		printer = new PrintWriter("ARIZONA_yelp_academic_dataset_tip.json");
		line = "";
		//a = 0;
		while(reader2.hasNextLine()){
				
			line = reader2.nextLine();
			tokens = line.split(",");
			
			String y = tokens[tokens.length-3].substring(15, tokens[tokens.length-3].length()-1);
			
			if(idTokenFound(y)){
				printer.println(line);
				}
			else{
				;
				}
				
			//a++;
			//System.out.println(a);

		}
		printer.close();
	
		//---------------------------------------------------------------------
		
		reader2 = new Scanner(new File("yelp_academic_dataset_tip.json"));
		printer = new PrintWriter("ARIZONA_yelp_academic_dataset_tip.json");
		line = "";
		a = 0;
		while(reader2.hasNextLine()){
				
			line = reader2.nextLine();
			tokens = line.split(",");
			
			String y = tokens[tokens.length-3].substring(15, tokens[tokens.length-3].length()-1);
			
			if(idTokenFound(y)){
				printer.println(line);
				}
			else{
				;
				}
				
			a++;
			System.out.println(a);

		}
		printer.close();
	}

	
	static public boolean idTokenFound(String a) throws IOException{

		for(int i = 0; i < ID.length; i++){
			
			if(a.equals(ID[i])){
				//System.out.println(1);
				return true;
				}
			else{
				//System.out.println(0);
				continue; 
				}
			}
		return false;

	}

}
