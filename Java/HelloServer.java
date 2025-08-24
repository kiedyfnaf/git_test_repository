// Networking
import java.net.ServerSocket;
import java.net.Socket;

// I/O streams & readers/writers
import java.io.InputStream;
import java.io.OutputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.IOException;

// Utility classes
import java.util.List;
import java.util.ArrayList;

// Concurrency (if you spin up threads yourself)
import java.lang.Thread;

public class HelloServer {
    public static void main(String[] args) {
        final int PORT = 9000;
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server listening on port " + PORT + "...");
            try (Socket client = serverSocket.accept();
                 PrintWriter out = new PrintWriter(client.getOutputStream());
                 BufferedReader in = BufferedReader(new InputStreamReader(client.getInputStream()))) {
                    System.out.println("Client connected: " + client.getRemoteSocketAddress());
                    out.println("Hello from server!");
                    String recieved = in.readLine();
                    System.out.println("Client says: " + recieved);
                 }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}