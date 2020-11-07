package org.slzdevsnp.restclients.common.utils;

import static org.hamcrest.MatcherAssert.assertThat;


import org.junit.Test;

import java.util.Arrays;

import static org.hamcrest.Matchers.*;

public class UriBuilderTest {

    @Test
    public void shouldCreateEmptyUrl() {
        String b = UriBuilder.url("http://www.google.com").build();
        assertThat(b, is("http://www.google.com"));
    }

    @Test
    public void shouldHandleNullValuesAndParam() {
        UriBuilder builder = UriBuilder.url(
                "https://api.wattsight.com/api/instances/tagged/1"
        )
                .param("tag", null);

    }

    @Test
    public void shouldCreateSingleParam() {
        String b = UriBuilder.url("http://www.google.com")
                .param("id", 1)
                .build();
        assertThat(b, is("http://www.google.com?id=1"));
    }

    @Test
    public void shouldCreateMultipleParam() {
        String b = UriBuilder.url("http://www.google.com")
                .param("id", 1)
                .param("id", 2)
                .build();
        assertThat(b, is("http://www.google.com?id=1&id=2"));
    }

    @Test
    public void shouldCreateMultipleParamMultipleAttributes() {
        String b = UriBuilder.url("http://www.google.com")
                .param("id", 1)
                .param("id", 2)
                .param("name", "One")
                .param("name", "Two")
                .build();
        assertThat(b, is("http://www.google.com?id=1&id=2&name=One&name=Two"));
    }


    @Test
    public void shouldHandleListParams() {
        String b = UriBuilder.url("http://www.google.com")
                .param("id", Arrays.asList(1, 2))
                .build();
        assertThat(b, is("http://www.google.com?id=1&id=2"));
    }

    @Test
    public void shouldHandleNullValues() {
        String b = UriBuilder.url("http://www.google.com")
                .param("id", Arrays.asList(1, 2))
                .param("query", null)
                .build();
        assertThat(b, is("http://www.google.com?id=1&id=2"));
    }


    @Test
    public void shouldHandleAllNullValues() {
        String b = UriBuilder.url("http://www.google.com")
                .param("query", null)
                .param("name", null)
                .build();
        assertThat(b, is("http://www.google.com?"));
    }

}