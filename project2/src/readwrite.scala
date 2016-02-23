import scala.io.Source
import java.io._

object readwrite
{
   def main(args :Array[String])
   {
     //read something, replace all string of "asset" to "video", then save a new file
     
     val srcFileName="/Users/jzhai001c/work/hql/assets.hql"
     val tgtFileName="/Users/jzhai001c/work/hql/assets_replaced.hql"
     val mywriter=new PrintWriter(new File(tgtFileName))
     for (l<-Source.fromFile(srcFileName).getLines())
     { 
       var array1= l.split("\t")
       var firstword=array1(0)
       println(firstword)
       println(array1.length)
       var newline=""
       for (i<-0 to array1.length-1)
       {
         newline=newline+array1(i)+"|"
       }
       println(newline)
       mywriter.write(newline+"\n")
     }
     //write newline into new file
     mywriter.close()
     
     
   }
   

}