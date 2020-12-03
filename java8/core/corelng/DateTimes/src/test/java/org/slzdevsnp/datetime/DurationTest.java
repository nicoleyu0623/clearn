package org.slzdevsnp.datetime;

import org.junit.Test;

import java.time.Duration;
import java.time.ZonedDateTime;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

public class DurationTest {

    @Test
    public void givenNowCheckDuration() throws InterruptedException {

        ZonedDateTime zdt1 = ZonedDateTime.now();
        Thread.sleep(10L);
        ZonedDateTime zdt2 = ZonedDateTime.now();
        Duration  dlt = Duration.between(zdt1, zdt2);
        System.out.println("duration in miliis " +  dlt.toMillis());
        assertThat(dlt.toMillis(), greaterThanOrEqualTo(10L));
        assertThat(dlt.toMillis(), lessThan(20L));
    }
}
