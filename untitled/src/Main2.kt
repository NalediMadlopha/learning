import java.io.File
import kotlin.math.abs

fun main(args: Array<String>) {
    var line = readLine();
    while (line != null) {
        var (a, b) = line.split(' ');
        println(Math.abs(a.toLong() - b.toLong()));
        line = readLine();
    }
}

//fun main(args : Array<String>) {
//    println("hell")
//}

//object MainKt {
//    @JvmStatic
//    fun main(args: Array<String>) {

//        File("/Users/naledi/Workspace/learning/untitled/src/text.txt").forEachLine {line ->
////            if (line != null) {
//                val (a, b) = line.split(' ')
//                println(abs(a.toLong() - b.toLong()))
////                line = readLine()
////            }
//        }
//        var line = readLine()
//
//        while (line != null) {
//            var (a, b) = line.split(' ')
//            println(Math.abs(a.toLong() - b.toLong()))
//            line = readLine()
//        }
//    }
//}
//fun main() {
//    var line = readLine()
//    while (line != null) {
//        var (a, b) = line.split(' ')
//        println(Math.abs(a.toLong() - b.toLong()))
//        line = readLine()
//    }
//}