package com.example.smarthomeapp.View;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintLayout;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.example.smarthomeapp.R;

public class LoginActivity extends AppCompatActivity {
    private ConstraintLayout btnLogin;
    private EditText etUser, etPass;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        btnLogin = findViewById(R.id.btn_login);
        etUser = findViewById(R.id.et_username);
        etPass = findViewById(R.id.et_password);

        btnLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String user = etUser.getText().toString();
                String pass = etPass.getText().toString();
                if(user == "" || pass == "")
                {
                    Toast.makeText(getApplicationContext(),"Vui lòng nhập đầy đủ thông tin!",Toast.LENGTH_SHORT).show();
                }
                else
                {
                    Login(user,pass);
                }
            }
        });
    }

    public void Login(String user,String pass){
     /*   FirebaseFirestore database = FirebaseFirestore.getInstance();
        database.collection("user")
                .whereEqualTo("username", user)
                .whereEqualTo("password", pass)
                .get()
                .addOnCompleteListener(task -> {
                    if(task.isSuccessful() && task.getResult() != null && task.getResult().getDocumentChanges().size()> 0){
                        Intent intent = new Intent(getApplicationContext(), MainActivity.class);
                        intent.addFlags(Intent.FLAG_ACTIVITY_MULTIPLE_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
                        startActivity(intent);
                    }else{
                        Toast.makeText(getApplicationContext(),"Tài khoản hoặc mật khẩu sai!",Toast.LENGTH_SHORT).show();
                    }
                });*/
        Intent intent = new Intent(getApplicationContext(), MainActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_MULTIPLE_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        startActivity(intent);
    }
}