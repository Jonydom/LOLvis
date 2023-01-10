package com.kirin.test_json;

import com.google.gson.Gson;
import com.kirin.test_json.bean.Hero;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.autoconfigure.json.JsonTest;
import org.springframework.boot.test.context.SpringBootTest;

import java.io.*;

/**
 * @author Xiyao Li
 * @date 2022/12/24 02:18
 */

public class InsertTest {
    Gson gson = new Gson();

    public static String readJsonFile(String fileName) {
        String jsonStr = "";
        try {
            File jsonFile = new File(fileName);
            FileReader fileReader = new FileReader(jsonFile);
            Reader reader = new InputStreamReader(new FileInputStream(jsonFile),"utf-8");
            int ch = 0;
            StringBuffer sb = new StringBuffer();
            while ((ch = reader.read()) != -1) {
                sb.append((char) ch);
            }
            fileReader.close();
            reader.close();
            jsonStr = sb.toString();
            return jsonStr;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
    @Test
    public void testFormat() {
        System.out.println("hello");
        String path = InsertTest.class.getClassLoader().getResource("com/kirin/test_json/result3.json").getPath();
        String s = readJsonFile(path);
        Hero hero = gson.fromJson(s, Hero.class);
        System.out.println(hero);

    }

}
