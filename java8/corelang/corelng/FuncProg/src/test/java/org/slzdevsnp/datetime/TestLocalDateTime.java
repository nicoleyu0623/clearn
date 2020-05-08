package org.slzdevsnp.datetime;

import org.junit.jupiter.api.Test;

import java.time.*;
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
    void testFormattedZonedNow(){
        DateTimeFormatter formatter
                = DateTimeFormatter.ofPattern("yyyyMMdd'-'HH:mm:ss.SSS");
        Instant now = Instant.now();
        LocalDateTime ldt = LocalDateTime.ofInstant(now, ZoneOffset.UTC);
        System.out.println("ldt:"+ldt);
        ZonedDateTime udt = now.atZone(ZoneId.of("UTC"));
        System.out.println("udt:"+udt);
        //print with date formatter
        System.out.println("fmt ldt:"+formatter.format(ldt));
        System.out.println("fmt udt:"+formatter.format(udt));
        System.out.println(formatter.format(Instant.now().atZone(ZoneId.of("UTC"))));
        assertTrue(true);

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
