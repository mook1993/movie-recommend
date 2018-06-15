package com.example.phm_1.movie;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    RadioGroup rg;
    RadioButton rb;
    EditText similar;
    EditText director;
    EditText actor;
    EditText etc;

    public static final String sIP = "192.168.0.12";
    public static final int sPORT = 5001;
    public SendData mSendData = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        rg = findViewById(R.id.radio_group);
        similar = findViewById(R.id.edit_similar);
        director = findViewById(R.id.edit_director);
        actor = findViewById(R.id.edit_actor);
        etc = findViewById(R.id.edit_etc);

        Button button = findViewById(R.id.btn_submit);
        button.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        Log.d("LOG", "in onClick");
        int radio_id = rg.getCheckedRadioButtonId();
        rb = findViewById(radio_id);
        mSendData = new SendData();
        mSendData.start();
    }

    /*서버에 요청해서 받은 값 RecommendActivy로 넘겨줌*/
    class SendData extends Thread {
        public void run() {
            try {
                DatagramSocket socket = new DatagramSocket();
                InetAddress serverAddr = InetAddress.getByName(sIP);
                byte[] send_buf = (rb.getText().toString() + " " + etc.getText().toString()).getBytes();
                DatagramPacket send_packet = new DatagramPacket(send_buf, send_buf.length, serverAddr, sPORT);
                socket.send(send_packet);

                byte[] receive_buf = new byte[1000];
                DatagramPacket recive_packet = new DatagramPacket(receive_buf, receive_buf.length, serverAddr, sPORT);
                socket.receive(recive_packet);
                String msg = new String(recive_packet.getData());

                Intent intent = new Intent(MainActivity.this, RecommendActivity.class);
                intent.putExtra("intent_msg", msg);
                startActivity(intent);
            } catch (Exception e) {
            }
        }
    }
}
