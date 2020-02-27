package com.example.consumingrest;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.web.client.RestTemplate;

// see https://spring.io/guides/gs/consuming-rest/
// https://github.com/spring-guides/gs-consuming-rest.git

@SpringBootApplication
public class ConsumingRestApplication {

	private static final Logger log = LoggerFactory.getLogger(ConsumingRestApplication.class);
	private static final String QUOTER_REST_ENDPOINT = "https://gturnquist-quoters.cfapps.io/api/random";
	private static final String WATTSIGHT_AUTH_ENDPOINT="https://auth.wattsight.com/oauth2/token";

	public static void main(String[] args) {

		SpringApplication.run(ConsumingRestApplication.class, args);
	}

	@Bean
	public RestTemplate restTemplate(RestTemplateBuilder builder) {
		return builder.build();
	}



	//CommandLineRunner
	@Bean
	public ApplicationRunner run(RestTemplate restTemplate) throws Exception {
		return args -> {
			//add headers here
			Quote quote = restTemplate.getForObject(
					QUOTER_REST_ENDPOINT, Quote.class);
			log.info(quote.toString());
		};



	}
}
