/**
 *
 */
package project2

/**
 * @author jzhai001c
 *
 */
object test1 {
  def main(args: Array[String])
  {
    val x=100;
    val y=100;
    var greeting:String="heoll"
   greeting="aegag"
    println(greeting.toUpperCase())
    if(x!=y) 
    {
      println("x!=y")
    }
    else if (x>y)
    {
      println("x>y")
    }
    else
    {
      println("something else")
    }
    val z=x%y
    println (z)
    println(xplusy(9,89))
    testunit(9,89)
   // var myList= range (1,10,2)
    //val max=maxValue(myList)
    //println("max from function is="+max)
  }
  
  def xplusy(x : Int, y : Int) : Int=
  {
    val sum=x+y
    return sum
  }
  
  def testunit(w:Int,y:Int):Unit=
  {
    println("this is" +  w + "and" + y)
  }
  
  def maxValue(a:Array[Int]):Int=
  {
    var b=a(0)
    for(x<- a)
    {
      println(x+"\n")
      if (x>b)
      {
        b=x
      }    
    }
    return b
    
  }
  


}