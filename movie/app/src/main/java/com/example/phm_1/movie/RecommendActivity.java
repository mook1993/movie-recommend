package com.example.phm_1.movie;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

public class RecommendActivity extends AppCompatActivity {
    TextView txtView=null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommend);
        String msg = getIntent().getStringExtra("intent_msg");
        txtView=(TextView) findViewById(R.id.recommend_movie);
        txtView.setText(msg);
    }
}
