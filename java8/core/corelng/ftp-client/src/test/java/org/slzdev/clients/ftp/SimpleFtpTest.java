package org.slzdev.clients.ftp;

import it.sauronsoftware.ftp4j.*;
import lombok.extern.slf4j.Slf4j;
import org.junit.*;

import java.io.IOException;
import java.util.Base64;
import java.util.Properties;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;


@Slf4j
public class SimpleFtpTest {
    private FTPClient ftpClient;

    @Before
    public  void init() throws IOException, FTPIllegalReplyException, FTPException {
        if (this.ftpClient == null) {
            Properties properties = new Properties();
            properties.load(SimpleFtpTest.class.getResourceAsStream("/application.properties"));

            String username = (String) properties.get("ftp.username.test");
            String pwdB64 = (String) properties.get ("ftp.pwd.test");
            String pwd = new String(Base64.getDecoder().decode(pwdB64));
            String wcloudIp="192.168.1.2";
            int port = 21;
            ftpClient = new FTPClient();
            ftpClient.connect(wcloudIp,port);
            ftpClient.login(username,pwd);
        }
    }

    @After
    public void tearDown() throws FTPException, IOException, FTPIllegalReplyException {
        if (ftpClient.isConnected()) {
            ftpClient.disconnect(true);
        }
    }

    @Test
    public void givenCurrentDirListIt() throws FTPException, IOException, FTPIllegalReplyException, FTPAbortedException, FTPDataTransferException, FTPListParseException {
        String cdir = ftpClient.currentDirectory();
        log.info("ftp cur dir - {}",cdir);
        assertThat(cdir,is("/"));
        FTPFile[] flist = ftpClient.list();
        log.info("current dir - {}  file listing - {}",cdir, flist);
    }

    @Test
    public void givenSpecifiedDirListIt() throws FTPException, IOException, FTPIllegalReplyException, FTPAbortedException, FTPDataTransferException, FTPListParseException {
        String sdir = "/Public/sz/tdata";
        ftpClient.changeDirectory(sdir);
        String cdir = ftpClient.currentDirectory();
        assertThat(cdir, is(sdir));

        FTPFile[] flist = ftpClient.list();
        log.info("current dir - {}  file listing - {}",cdir, flist);
    }


    @Ignore
    @Test
    public void givenWcloudConnection() throws FTPException, IOException, FTPIllegalReplyException {
        String wcloudIp="192.168.1.2";
        int port = 21;
        String username="zimine";
        String pwd = "9lalala9";
        ftpClient.connect(wcloudIp,port);
        ftpClient.login(username,pwd);
    }

    @Test
    public void givenBase64Decode() {
        String originalS="9lalala9";
        String encodedS=Base64.getEncoder().encodeToString(originalS.getBytes());
        byte[] decodedBytes = Base64.getDecoder().decode(encodedS);
        String decodedS = new String(decodedBytes);
        log.info("encoded: - {} decoded - {}",encodedS, decodedS);
        assertThat(decodedS,is(originalS));
    }
}
