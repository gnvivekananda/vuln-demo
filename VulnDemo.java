import java.io.*;
import java.security.MessageDigest;

public class VulnDemo {

    public static String weakHash(String password) throws Exception {
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(password.getBytes());
        return new String(md.digest());
    }

    public static Object unsafeDeserialize(byte[] data) throws Exception {
        ByteArrayInputStream bis = new ByteArrayInputStream(data);
        ObjectInputStream in = new ObjectInputStream(bis);
        return in.readObject();
    }

    static String dbUser = "admin";
    static String dbPass = "password123";

    public static void main(String[] args) {
        System.out.println("Vulnerable Java Demo");
    }
}
