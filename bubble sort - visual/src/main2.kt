import processing.core.PApplet

class Rectangles: PApplet(){

    //private val rectHeight = 80
    private val rectWidth = 10
    private var numOfRect = 0
    private var values = arrayListOf<Float>()

    //rect(x,y, width,height)

    override fun settings() {
        size(800, 600)
        numOfRect = width / rectWidth
    }

    override fun setup() {
        frameRate(60f)
        for(i in 0 until numOfRect){
            values.add(random(height.toFloat()))
        }

        println("width: $width")
        println("numOfRects: $numOfRect")
        println("cate dreptunghiuri ar trebui sa am in teorie ${values.size}")
    }

    private var i = 0
    private var j = 0

    override fun draw(){
        redraw()
        background(0)

        var a = values[j]
        var b = values[j+1]
        //println("a: $a, b: $b")

        if(i < values.size){
            if(a > b){
                swap(values, j, j+1)
            }
            j++
            if(j >= values.size - i - 1){
                j = 0
                i++
            }

            for(i in 0 until values.size){
                fill(255)
                rect((rectWidth*i).toFloat(), height-values[i], rectWidth.toFloat(), values[i])

                fill(255f,0f,0f)
                rect(rectWidth*(j).toFloat(), height-a,rectWidth.toFloat(),a)

            }
        }else{
            println("finished")

            for(i in 0 until values.size){
                fill(0f,255f,0f)
                rect((rectWidth*i).toFloat(), height-values[i], rectWidth.toFloat(), values[i])
            }
            noLoop()
        }

        //saveFrame("dreptunghiuri/frame-####.jpg")
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
    PApplet.main("Rectangles")
}