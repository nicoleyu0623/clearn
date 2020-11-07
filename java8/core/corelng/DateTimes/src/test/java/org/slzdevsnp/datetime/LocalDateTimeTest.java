package org.slzdevsnp.datetime;


import org.junit.Test;

import java.time.*;
import java.time.format.DateTimeFormatter;


import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

public class LocalDateTimeTest {

    @Test
    public void given_now_getLocalDateTime(){
        LocalDateTime nowLdt = LocalDateTime.now();
        System.out.println("now LocalDateTime (corresponds to myzone clocl):"+nowLdt);
    }

    @Test
    public void testParsingDateTimeZ(){
         DateTimeFormatter formatterA
                 = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");
        DateTimeFormatter formatterZ
                = DateTimeFormatter.ISO_ZONED_DATE_TIME;

        String created_dtstr = "2020-03-02T13:52:56.446Z";
        ZonedDateTime dtCrez = ZonedDateTime.parse(created_dtstr,formatterZ);
        System.out.println("ldt_cre:"+dtCrez.toString());
        System.out.println(dtCrez.getZone());
        assertThat (dtCrez , not(nullValue()));
    }


    @Test
    public void testFormattedZonedNow(){
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

    }


    @Test
    public void givenNumbersCheckComponents() {
        LocalDateTime ldtFriday =
                LocalDateTime.of(2020, 11, 6, 22, 0, 0,
                        333000000);
        System.out.println("local datetime:" + ldtFriday);
        System.out.println("its local:" + ldtFriday.toLocalDate());
        System.out.println("its local time:" + ldtFriday.toLocalTime());
        //asserts
        assertThat(ldtFriday.toLocalDate().getDayOfWeek(), is(DayOfWeek.FRIDAY));
        assertThat(ldtFriday.toLocalTime().getHour(), is(22));
        assertThat(ldtFriday.toLocalTime().getMinute(), is(0));
        assertThat(ldtFriday.toLocalTime().getNano(), is(333000000));

    }

    @Test
    public void givenDateAddLocalTime() {

        //LocalDate ld = LocalDate.now();
        LocalDate ld = LocalDate.of(2020,11,6);
        LocalDateTime ldt = ld.atStartOfDay();
        System.out.println("today start of day local datetime:" + ldt);
        LocalTime lt = LocalTime.parse("22:01");
        ldt  = ldt.plusHours(lt.getHour()).plusMinutes(lt.getMinute());
        assertThat(ldt.toString(), is("2020-11-06T22:01"));
    }
}
