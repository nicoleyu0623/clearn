package org.slzdevsnp.datetime;

import org.junit.jupiter.api.Test;

import java.time.*;
import java.time.format.DateTimeFormatter;

import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

public class ZonedDateTimeTest {

    @Test
    public void given_now_fromTs_inLocalTimeZone_toUtc(){
        LocalDateTime ldt = LocalDateTime.now();

        ZoneId zZoneId = ZoneId.of("UTC");
        ZoneId sysZone = ZoneId.systemDefault(); //from this system

        ZonedDateTime zldt = ldt.atZone(sysZone);
        //converting datetime from a system zone to utc zone
        ZonedDateTime zdtutc = zldt.withZoneSameInstant(ZoneId.of("UTC"));

        System.out.printf("utc zone: %s  system zone: %s\n",zZoneId, sysZone);
        System.out.printf("now dt %s in local zone: %s\n" , zldt, sysZone);
        System.out.printf("now dt %s in utc zone %s\n", zdtutc,zZoneId);

        assert(zldt.toInstant().toEpochMilli()==zdtutc.toInstant().toEpochMilli());
    }

    @Test
    public void given_UTCDateTime_toLocalDateTime(){
        LocalDateTime ldt = LocalDateTime.now();
        ZonedDateTime ldtz = ldt.atZone(ZoneId.of("UTC"));
        LocalDateTime ldtl = ldtz.toLocalDateTime();
        System.out.printf("zoneDatetime %s converted to local datetime %s  by stripping zone info\n", ldtz, ldtl);
        assert(true);
    }

    @Test
    public void testParsingDateTimeOffsetPlus(){

        DateTimeFormatter formatterZ
                = DateTimeFormatter.ISO_ZONED_DATE_TIME;

        String dtstr = "2020-03-03T00:00:00.009+01:00";
        ZonedDateTime zdt = ZonedDateTime.parse(dtstr,formatterZ);
        System.out.println("zone_dt:"+zdt);
        System.out.println("ldt_cre:"+zdt.toString());
        System.out.println("zone:"+zdt.getZone());
        System.out.println("offset in sec:"+zdt.getOffset().getTotalSeconds());

        assertTrue(zdt != null);
    }



    @Test
    public void testParsingDateTimeOffsetPlus_Alt() {
        String dtstr = "2020-03-03T00:00:00.009+01:00";
        //  DateTimeFormatter.ISO_ZONED_DATE_TIME  is used by default
        ZonedDateTime zdt = ZonedDateTime.parse(dtstr);
        System.out.println("zdt:"+zdt);
        System.out.println("zone offset:"+zdt.getOffset());
        System.out.println("zone:"+zdt.getZone());
        assertNotEquals(zdt, null);
    }

    @Test
    public void given_ZUTCStr_parse_ZonedDateTime(){
        String dtstr="2020-01-02T09:15Z[UTC]";
        ZonedDateTime zdt = ZonedDateTime.parse(dtstr);
        System.out.println("zdt:"+zdt);
        System.out.println("zone offset:"+zdt.getOffset());
        assert(zdt.getOffset().equals(ZoneOffset.UTC));
        assert(zdt!=null);
    }

    @Test
    public void given_ZUTCStr_epochmillis(){
        String dtstr="2020-01-02T09:15Z[UTC]";
        ZonedDateTime zdt = ZonedDateTime.parse(dtstr);
        long e = zdt.toInstant().toEpochMilli();
        System.out.println("zoned dt: "+zdt);
        System.out.println("epoch milli: "+e);

        String dtstr1="2020-01-02T10:15:00+01:00";
        ZonedDateTime zdt1 = ZonedDateTime.parse(dtstr1);
        long e1 = zdt1.toInstant().toEpochMilli();
        assert(e1==e);
    }

    @Test
    public void given_ZStr_epochmillis(){
        String dtstr="2020-06-09T07:43:13.490Z";
        ZonedDateTime zdt = ZonedDateTime.parse(dtstr);
        long e = zdt.toInstant().toEpochMilli();
        System.out.println(String.format("zoned dt: %s  from zone: %s ; epoch milli: %d",zdt, zdt.getZone(), e));
        assert(zdt.getOffset().equals(ZoneOffset.UTC));  //zdt is in UTC
        assert(zdt!=null);
    }

    @Test
    public void given_string_toZdt(){
        String dtstr="2020-06-09T07:43:13.490Z";
        ZonedDateTime zdt = ZonedDateTime.parse(dtstr);
        long e = zdt.toInstant().toEpochMilli();
        ZonedDateTime zzdt = ZonedDateTime.ofInstant(Instant.ofEpochMilli(e),ZoneId.of("UTC"));
        System.out.println(String.format("zone dt: %s",zzdt));
        assert(zzdt.toString().equals("2020-06-09T07:43:13.490Z[UTC]"));
        System.out.println(zzdt.format(DateTimeFormatter.ISO_ZONED_DATE_TIME));
    }

    @Test
    public void given_string_toZdt_toFormattedString(){
        String dtstr="2020-06-09T07:43:13.49Z";
        ZonedDateTime zdt = ZonedDateTime.parse(dtstr);
        System.out.println(zdt.format(DateTimeFormatter.ISO_ZONED_DATE_TIME));
        System.out.println(zdt.toString());
        assert(zdt.toString().equals("2020-06-09T07:43:13.490Z"));

        final DateTimeFormatter dateTimeFormatter =
                DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'");

        System.out.println("with formatter: " + zdt.format(dateTimeFormatter));
        assert(zdt.format(dateTimeFormatter).equals("2020-06-09T07:43:13.490Z"));

    }


    @Test
    void givenMillisToZdt() {
        long emilli = 1591688593490L;
        ZonedDateTime zzdt = ZonedDateTime.ofInstant(Instant.ofEpochMilli(emilli),ZoneId.of("Z"));
        System.out.println(String.format("zone dt: %s",String.valueOf(zzdt)));
        assert(zzdt.toString().equals("2020-06-09T07:43:13.490Z"));
    }

    @Test
    void givenEpochSecondsToZdt() {
        long epochsecs = 1599263700L;
        ZonedDateTime zdt = ZonedDateTime.ofInstant(Instant.ofEpochSecond(epochsecs),ZoneId.of("Z"));
        System.out.println(String.format("zone dt: %s",String.valueOf(zdt)));
        assert(zdt.toString().equals("2020-09-04T23:55Z"));
    }

    @Test
    void givenNowtoUTCString() {
        ZonedDateTime zdt = LocalDateTime.now().atZone(ZoneId.of("Z"));
        System.out.println(String.format("zdt of now:%s",zdt.toString()));
        assert(zdt!=null);
    }
}
