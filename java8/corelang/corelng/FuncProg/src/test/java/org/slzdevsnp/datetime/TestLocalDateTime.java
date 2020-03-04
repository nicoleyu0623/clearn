package org.slzdevsnp.datetime;

import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

import static org.junit.jupiter.api.Assertions.*;


public class TestLocalDateTime {

    @Test
    void testParsingDateTimeZ(){
         DateTimeFormatter formatterA
                 = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
        DateTimeFormatter formatterZ
                = DateTimeFormatter.ISO_ZONED_DATE_TIME;

        String created_dtstr = "2020-03-02T13:52:56.446Z";
        ZonedDateTime dtCrez = ZonedDateTime.parse(created_dtstr,formatterZ);
        System.out.println("ldt_cre:"+dtCrez.toString());
        System.out.println(dtCrez.getZone());
        assertTrue(dtCrez != null);
    }
    @Test
    void testParsingDateTimeOffset(){

        DateTimeFormatter formatterZ
                = DateTimeFormatter.ISO_ZONED_DATE_TIME;

        String dtstr = "2020-03-03T00:00:00+01:00";
        ZonedDateTime dtOff = ZonedDateTime.parse(dtstr,formatterZ);
        System.out.println("ldt_cre:"+dtOff.toString());
        System.out.println("zone:"+dtOff.getZone());
        System.out.println("offset in sec:"+dtOff.getOffset().getTotalSeconds());

        assertTrue(dtOff != null);
    }


}
