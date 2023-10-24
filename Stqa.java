/* Practical-3 */
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class Practical3 {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver","C:\\Users\\USER\\Desktop\\chromedriver_win32_v85-2\\chromedriver.exe");
        WebDriver driver= new ChromeDriver();
        driver.get("https://google.com");
        driver.manage().window().maximize();
       }

/* Practical-4 */
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class Practical4stqa {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver","C:\\Users\\USER\\Desktop\\chromedriver_win32_v85-2\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("http://localhost/login.html");
        driver.findElement(By.id("user")).sendKeys("adnankhan");
        driver.findElement(By.id("pass")).sendKeys("adnankhan123");
        driver.findElement(By.id("btn")).click();
        if(driver.getTitle().contains("Welcome"))
        {
            System.out.println("Login Successful!");
        }
        else
        {
            System.out.println("Login Failed!");
        }
        driver.quit();
    }
}

/* Practical-5 */
import java.io.FileInputStream;
import java.io.FileOutputStream;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
import jxl.Workbook;
import jxl.Sheet;
import jxl.write.Label;
public class PracticalNo5 {   
    public static void main(String[] args)throws Exception {
        FileInputStream fi =new FileInputStream("F:\\adnan\\Book1.xls");
        Workbook w = Workbook.getWorkbook(fi);
        Sheet s= w.getSheet(0);
        String a[][] = new String[s.getRows()][s.getColumns()];
        FileOutputStream fo=new FileOutputStream("F:\\adnan\\Bookres.xls");
        WritableWorkbook wwb = Workbook.createWorkbook(fo);
        WritableSheet ws = wwb.createSheet("Book", 0);
        for (int i=0; i<s.getRows(); i++)
        {
            for (int j=0; j<s.getColumns(); j++)
            {
                a[i][j] = s.getCell(j,i).getContents();
                Label l = new Label(j, i, a[i][j]);
                ws.addCell(l);
            }
        }
        Label l = new Label(6, 0, "Book");
        ws.addCell(l);
        for(int i=1; i<s.getRows(); i++)
        {
            for(int j=5; j<s.getColumns(); j++)
            {
                a[i][j] = s.getCell(j,i).getContents();
                int x = Integer.parseInt(a[i][j]);
                if(x/3 >= 35)
                {
                    Label l1 = new Label(6, i, "pass");
                    ws.addCell(l1);
                }
                else{
                    Label l1 = new Label(6,i,"fail");
                    ws.addCell(l1);
                    break;
                }
            }
        }
        wwb.write();
        wwb.close();          
               }
   }


/* Practical-6 */
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import jxl.Sheet;
import jxl.Workbook;
import jxl.write.Label;
import jxl.write.WritableSheet;
import jxl.write.WritableWorkbook;
public class Prcatical6stqa {
    public static void main(String[] args) throws Exception {
            FileInputStream fi=new FileInputStream("F:\\adnan\\Marks.xls");
            Workbook w = Workbook.getWorkbook(fi);
            Sheet s= w.getSheet(0);
            FileOutputStream fo = new FileOutputStream("F:\\adnan\\Marksfin.xls");
            WritableWorkbook wwb= Workbook.createWorkbook(fo);
            WritableSheet ws= wwb.createSheet("result1", 0);
            System.out.println();
            for (int i=0; i<s.getRows(); i++)
            {
                String temp[] = new String[s.getColumns()];
                boolean flag = false;
                for (int j=0; j<s.getColumns(); j++)
                {
                    temp[j] = s.getCell(j, i).getContents();
                    if(i>= 1 && j>= 2 && j<=4)
                    {
                        if(Integer.parseInt(temp[j])>=60)
                        {
                            flag=true;
                        }
                    }
                }
             if(flag)
               {
                 for(int k=0; k<temp.length; k++)
                   {
                     Label l2 = new Label(k,i,temp[k]);
                     ws.addCell(l2);
                   }
               }
            }
             wwb.write();
             wwb.close();
           }      
}


/* Practical-7 */
import java.util.List;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

/**
 *
 * @author USER
 */
public class Practical7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         System.setProperty("webdriver.chrome.driver","C:\\Users\\USER\\Desktop\\chromedriver_win32_v85-2\\chromedriver.exe");
        WebDriver driver= new ChromeDriver();
        driver.get("https://google.com");
        driver.manage().window().maximize();
        List <WebElement>links = driver.findElements(By.tagName("a"));
         List <WebElement>buttons = driver.findElements(By.tagName("button"));
          List <WebElement>fields = driver.findElements(By.tagName("input"));
          System.out.println("Total No.of Links = " + links.size());
          System.out.println("Total No.of Button = " + buttons.size());
          System.out.println("Total No.of fields = " + fields.size());
     }
    }


/* Practical-8 */
import java.util.List;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class Practical8 {
    

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver","C:\\Users\\USER\\Desktop\\chromedriver_win32_v85-2\\chromedriver.exe");
        WebDriver driver= new ChromeDriver();
        driver.get("C:\\xampp\\htdocs\\listandcombo.html");
        driver.manage().window().maximize();
        List <WebElement> lists = driver.findElements(By.xpath("//select/option"));
        List <WebElement> lst;
        lst = driver.findElements(By.xpath("//ol/li"));
        System.out.println("Total no.of lists:" + lists.size());
        System.out.println("Total no.of lists:" + lst.size());
         driver.quit();
    }
    
}


/* Practical-9 */
import java.util.List;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class Practical9 {

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver","C:\\Users\\USER\\Desktop\\chromedriver_win32_v85-2\\chromedriver.exe");
        WebDriver driver= new ChromeDriver();
        driver.manage().window().maximize();
        driver.get("http://localhost/checkbox.html");
        List<WebElement> checkbox= driver.findElements(By.xpath("//input[@type='checkbox']"));
        int checked=0 , unchecked=0;
        for(int i=0;i<checkbox.size();i++){
            if(checkbox.get(i).isSelected()){
                checked++;
            }
            else{
                unchecked++;
                }

        }
        System.out.println("total no.of checkbox is checked:" + checked);
        System.out.println("total no.of checkbox is unchecked:" + unchecked);
        driver.quit();

      
    }

