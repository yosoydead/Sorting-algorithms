import processing.core.PApplet

//to get to use the Processing library and its features, i have to create a class and have it implement
//the PApplet() thing
//settings(), setup(), draw() are core functions in order to get this thing working
class Lines(): PApplet(){

    //in here i generate some random numbers/floats
    private var values = arrayListOf<Float>()

    override fun settings(){
        //fullScreen()
        size(640, 480)
    }

    //in setup i populate the array with numbers so i have the values ready to go
    override fun setup(){
        background(0)
        frameRate(60f)
        for(i in 0 until width){
            //stroke(random(255f), random(255f), random(255f))
            //values[i] = random(height.toFloat())
            values.add(random(height.toFloat()))
        }
        kotlin.io.println(values)
        //line(30f, 30f, 30f, 200f)
    }

    private var i = 0
    private var j = 0

    //this function is going to draw frames on the screen endlessly at a set framerate
    override fun draw(){
        background(0)
        var a = values[j]
        var b  = values[j+1]

        //YOU CAN UNCOMMENT THIS PART OF THE CODE SO YOU CAN SEE THE SORT HAPPENING ON EACH FRAME
        //IT TAKES A REALLY LONG TIME
//        if(a > b){
////            var temp = values[j]
////            values[j] = values[j+1]
////            values[j+1] = temp
//
//            delay(2000)
//            stroke(255f,0f,102f)
//            line(j.toFloat(), height.toFloat(), j.toFloat(), height - a)
//
//            stroke(0f,255f,0f)
//            line(j+1.toFloat(), height.toFloat(), j+1.toFloat(), height - b)
//            swap(values, j, j+1)
//        }
//
//        if(i< values.size){
//            j++
//            if(j >= values.size-i-1){
//                j = 0
//                i++
//            }
//
//        }else{
//            println("finished")
//            noLoop()
//        }


        //because the draw() is a loop, i use it to do an operation for each frame it draws
        //here is an adapted version of bubble sort to work with this stuff
        if(i < values.size){
            //in here, for each frame, i do some part of the sorting because if i were to do
            //a part of the sorting on each frame, it would take it ages to finish because of bubble sort
            for(j in 0 until values.size - i - 1){
//                stroke(255f,0f,0f)
//                line(i.toFloat(), height.toFloat(), i.toFloat(), height - values[i])
                var a = values[j]
                var b  = values[j+1]
                if(a > b){
                    var temp = values[j]
                    values[j] = values[j+1]
                    values[j+1] = temp
                }
            }

            //this loop is used to just display the lines on the screen with the given location
            for(i in 0 until values.size){
                //stroke(random(255f), random(255f), random(255f))
                //values[i] = random(height.toFloat())

                //stroke gives the color for the lines
                stroke(255f, 100f)
                //the line needs 4 arguments
                //X axis - starting point
                //Y axis - starting point
                //X2 axis - ending point
                //Y2 axis - ending point
                //for Y2 i used the coresponding number from the values array to calculate its ending point
                line(i.toFloat(), height.toFloat(), i.toFloat(), height - values[i])//random(height.toFloat())
            }

            i++
        }else{
            //this part triggers only when the sort is done
            //after it is done, i draw the lines one more time with a green background
            //to indicate that it is done
            println("finished")
            for(i in 0 until values.size){
                //stroke(random(255f), random(255f), random(255f))
                //values[i] = random(height.toFloat())
                stroke(0f,255f, 0f)
                line(i.toFloat(), height.toFloat(), i.toFloat(), height - values[i])//random(height.toFloat())
            }

            //noLoop stops the execution of draw()
            noLoop()
        }
        //stroke(255)
        //line(j++.toFloat(), height.toFloat(), j.toFloat(), 200f)
    }

    //with the help of this function, if i press on the window while doing its thing
    //i can stop the execution
    override fun mousePressed() {
        noLoop()
    }

    //if i release the mouse button, the window resumes its execution
    override fun mouseReleased() {
        loop()
    }

    private fun swap(array: ArrayList<Float>, a: Int, b: Int){
        var temp = array[a]
        array[a] = array[b]
        array[b] = temp
    }
}


fun main(args: Array<String>){
    PApplet.main("Lines")
}