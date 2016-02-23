import scala.io._
import java.io._
object io1 
{
   def main(args: Array[String]) 
   {
      val filename="/Users/jzhai001c/89.txt"
      val w = new BufferedWriter(new FileWriter("/Users/jzhai001c/output.txt"))
      for (line <- Source.fromFile(filename).getLines())
      {
        println(line)
        w.write(line+"\n")
      }
   w.close
      
   }
}
