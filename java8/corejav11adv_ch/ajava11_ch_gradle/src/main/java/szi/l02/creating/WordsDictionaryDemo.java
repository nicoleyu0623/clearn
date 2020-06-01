package szi.l02.creating;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class WordsDictionaryDemo {

    public static void main(String[] args) throws IOException{

        WordsDictionaryDemo wd = new WordsDictionaryDemo();
        Stream<String> words = wd.getWords("/usr/share/dict/words");

        System.out.println("### check how many words in dict has length > 12");
        System.out.printf(" words: %d%n",
                words.filter(w -> w.length() > 12)
                .count());

    }

    Stream<String> getWords(String fspath) throws IOException {
        Stream<String>  lines = Files.lines(Paths.get(fspath));
        return lines;
    }

}
