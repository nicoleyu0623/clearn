@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  advancedjava_szi startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%..

@rem Resolve any "." and ".." in APP_HOME to make it shorter.
for %%i in ("%APP_HOME%") do set APP_HOME=%%~fi

@rem Add default JVM options here. You can also use JAVA_OPTS and ADVANCEDJAVA_SZI_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windows variants

if not "%OS%" == "Windows_NT" goto win9xME_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\lib\advancedjava_szi.jar;%APP_HOME%\lib\javax.json-api-1.1.4.jar;%APP_HOME%\lib\hibernate-entitymanager-5.4.13.Final.jar;%APP_HOME%\lib\guava-28.2-jre.jar;%APP_HOME%\lib\javax.json-1.1.4.jar;%APP_HOME%\lib\mysql-connector-java-8.0.19.jar;%APP_HOME%\lib\groovy-ant-2.5.9.jar;%APP_HOME%\lib\groovy-cli-commons-2.5.9.jar;%APP_HOME%\lib\groovy-groovysh-2.5.9.jar;%APP_HOME%\lib\groovy-console-2.5.9.jar;%APP_HOME%\lib\groovy-groovydoc-2.5.9.jar;%APP_HOME%\lib\groovy-docgenerator-2.5.9.jar;%APP_HOME%\lib\groovy-cli-picocli-2.5.9.jar;%APP_HOME%\lib\groovy-datetime-2.5.9.jar;%APP_HOME%\lib\groovy-jmx-2.5.9.jar;%APP_HOME%\lib\groovy-json-2.5.9.jar;%APP_HOME%\lib\groovy-jsr223-2.5.9.jar;%APP_HOME%\lib\groovy-macro-2.5.9.jar;%APP_HOME%\lib\groovy-nio-2.5.9.jar;%APP_HOME%\lib\groovy-servlet-2.5.9.jar;%APP_HOME%\lib\groovy-sql-2.5.9.jar;%APP_HOME%\lib\groovy-swing-2.5.9.jar;%APP_HOME%\lib\groovy-templates-2.5.9.jar;%APP_HOME%\lib\groovy-test-2.5.9.jar;%APP_HOME%\lib\groovy-test-junit5-2.5.9.jar;%APP_HOME%\lib\groovy-testng-2.5.9.jar;%APP_HOME%\lib\groovy-xml-2.5.9.jar;%APP_HOME%\lib\groovy-2.5.9.jar;%APP_HOME%\lib\hibernate-core-5.4.13.Final.jar;%APP_HOME%\lib\hibernate-commons-annotations-5.1.0.Final.jar;%APP_HOME%\lib\jboss-logging-3.3.2.Final.jar;%APP_HOME%\lib\dom4j-2.1.1.jar;%APP_HOME%\lib\javax.persistence-api-2.2.jar;%APP_HOME%\lib\byte-buddy-1.10.7.jar;%APP_HOME%\lib\jboss-transaction-api_1.2_spec-1.1.1.Final.jar;%APP_HOME%\lib\failureaccess-1.0.1.jar;%APP_HOME%\lib\listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar;%APP_HOME%\lib\jsr305-3.0.2.jar;%APP_HOME%\lib\checker-qual-2.10.0.jar;%APP_HOME%\lib\error_prone_annotations-2.3.4.jar;%APP_HOME%\lib\j2objc-annotations-1.3.jar;%APP_HOME%\lib\protobuf-java-3.6.1.jar;%APP_HOME%\lib\ant-junit-1.9.13.jar;%APP_HOME%\lib\ant-1.9.13.jar;%APP_HOME%\lib\ant-launcher-1.9.13.jar;%APP_HOME%\lib\ant-antlr-1.9.13.jar;%APP_HOME%\lib\commons-cli-1.4.jar;%APP_HOME%\lib\picocli-4.0.1.jar;%APP_HOME%\lib\qdox-1.12.1.jar;%APP_HOME%\lib\jline-2.14.6.jar;%APP_HOME%\lib\junit-4.12.jar;%APP_HOME%\lib\junit-platform-launcher-1.4.0.jar;%APP_HOME%\lib\junit-jupiter-engine-5.4.0.jar;%APP_HOME%\lib\testng-6.13.1.jar;%APP_HOME%\lib\javassist-3.24.0-GA.jar;%APP_HOME%\lib\antlr-2.7.7.jar;%APP_HOME%\lib\jandex-2.1.1.Final.jar;%APP_HOME%\lib\classmate-1.5.1.jar;%APP_HOME%\lib\jaxb-runtime-2.3.1.jar;%APP_HOME%\lib\jaxb-api-2.3.1.jar;%APP_HOME%\lib\javax.activation-api-1.2.0.jar;%APP_HOME%\lib\hamcrest-core-1.3.jar;%APP_HOME%\lib\junit-platform-engine-1.4.0.jar;%APP_HOME%\lib\junit-jupiter-api-5.4.0.jar;%APP_HOME%\lib\junit-platform-commons-1.4.0.jar;%APP_HOME%\lib\apiguardian-api-1.0.0.jar;%APP_HOME%\lib\jcommander-1.72.jar;%APP_HOME%\lib\txw2-2.3.1.jar;%APP_HOME%\lib\istack-commons-runtime-3.0.7.jar;%APP_HOME%\lib\stax-ex-1.8.jar;%APP_HOME%\lib\FastInfoset-1.2.15.jar;%APP_HOME%\lib\opentest4j-1.1.1.jar

@rem Execute advancedjava_szi
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %ADVANCEDJAVA_SZI_OPTS%  -classpath "%CLASSPATH%" database.initialize_database %CMD_LINE_ARGS%

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable ADVANCEDJAVA_SZI_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%ADVANCEDJAVA_SZI_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
