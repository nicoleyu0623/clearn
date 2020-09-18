package org.slzdev.unirest;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import kong.unirest.HttpResponse;
import kong.unirest.JsonNode;
import kong.unirest.Unirest;
import kong.unirest.UnirestException;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

public class HttpClientLiveTest {


    @BeforeClass
    public static void setup() {
        // Unirest.setProxy(new HttpHost("localhost", 8080));

//        Unirest.setTimeouts(20000, 15000);
//        Unirest.setDefaultHeader("X-app-name", "baeldung-unirest");
//        Unirest.setDefaultHeader("X-request-id", "100004f00ab5");
//        Unirest.setConcurrency(20, 5);
//        Unirest.setObjectMapper(new ObjectMapper() {
//            com.fasterxml.jackson.databind.ObjectMapper mapper = new com.fasterxml.jackson.databind.ObjectMapper();
//
//            public String writeValue(Object value) {
//                try {
//                    return mapper.writeValueAsString(value);
//                } catch (JsonProcessingException e) {
//                    throw new RuntimeException(e);
//                }
//
//            }
//
//            public <T> T readValue(String value, Class<T> valueType) {
//
//                try {
//                    return mapper.readValue(value, valueType);
//                } catch (Exception e) {
//                    throw new RuntimeException(e);
//                }
//
//            }
//        });
    }

    @AfterClass
    public static void tearDown() throws IOException {
        //Unirest.clearDefaultHeaders();
        //Unirest.shutdown();
    }

    @Test
    public void shouldReturnStatusOkay() throws UnirestException {
        HttpResponse<JsonNode> jsonResponse = Unirest.get("http://www.mocky.io/v2/5a9ce37b3100004f00ab5154")
                .header("accept", "application/json")
                .queryString("apiKey", "123")
                .asJson();
        assertNotNull(jsonResponse.getBody());
        assertEquals(200, jsonResponse.getStatus());
    }

    @Test
    public void shouldReturnStatusAccepted() throws UnirestException {

        Map<String, String> headers = new HashMap<String, String>();
        headers.put("accept", "application/json");
        headers.put("Authorization", "Bearer 5a9ce37b3100004f00ab5154");

        Map<String, Object> fields = new HashMap<String, Object>();
        fields.put("name", "Sam Baeldung");
        fields.put("id", "PSP123");

        HttpResponse<JsonNode> jsonResponse = Unirest.put("http://www.mocky.io/v2/5a9ce7853100002a00ab515e")
                .headers(headers)
                .fields(fields)
                .asJson();
        assertNotNull(jsonResponse.getBody());
        assertEquals(202, jsonResponse.getStatus());
    }

}
