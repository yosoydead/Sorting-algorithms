import processing.core.PApplet

class bla: PApplet(){

    private var values = arrayListOf<Float>()
    private val rectWidth = 10
    private var numOfRect = 0

    override fun settings(){
        size(640, 480)
    }

    override fun setup(){
        frameRate(60f)

        numOfRect = width/rectWidth

        for(i in 0 until width){
            values.add(random(height.toFloat()))
        }

        println(values)
    }

    private var i = 0
    private var j = 0

    override fun draw(){
        background(0)

        if(i < values.size-1){
            var smallestAtIndex = findSmallest(i, values)

            swap(values, i, smallestAtIndex)
            i++
            j = i

            for(i in 0 until values.size){
//            stroke(255)
//            line(i.toFloat(),height.toFloat(), i.toFloat(), height-values[i])
//                fill(255)
//                rect((rectWidth*i).toFloat(), height-values[i], rectWidth.toFloat(), values[i])
//
////                fill(255f,0f,0f)
////                rect(rectWidth*(j).toFloat(), height-values[j],rectWidth.toFloat(),values[j])
//
//                fill(0f,0f,255f)
//                rect(rectWidth*(smallestAtIndex).toFloat(), height-values[smallestAtIndex],rectWidth.toFloat(),values[smallestAtIndex])
//
                stroke(255)
                line(i.toFloat(),height.toFloat(), i.toFloat(), height-values[i])
            }
        }else{
            println("finished")

            for(i in 0 until values.size){
//            stroke(255)
//            line(i.toFloat(),height.toFloat(), i.toFloat(), height-values[i])
//                fill(0f, 255f, 0f)
//                rect((rectWidth*i).toFloat(), height-values[i], rectWidth.toFloat(), values[i])

                stroke(0f, 255f, 0f)
                line(i.toFloat(),height.toFloat(), i.toFloat(), height-values[i])
            }
            noLoop()
        }
    }

    private fun findSmallest(index: Int, array: ArrayList<Float>): Int{
        var smallestNumIndex = index

        for(i in index+1 until array.size){
            if(array[i] < array[smallestNumIndex]){
                smallestNumIndex = i
            }
        }

        return smallestNumIndex
    }

    private fun swap(array: ArrayList<Float>, a: Int, b: Int){
        var temp = array[a]
        array[a] = array[b]
        array[b] = temp
    }

    override fun mousePressed() {
        noLoop()
    }

    override fun mouseReleased() {
        loop()
    }
}


fun main(args: Array<String>){
    PApplet.main("bla")
}