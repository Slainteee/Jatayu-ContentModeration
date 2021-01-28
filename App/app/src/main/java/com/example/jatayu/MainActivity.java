package com.example.jatayu;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.app.Activity;
import android.app.ProgressDialog;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.cloudinary.android.MediaManager;
import com.cloudinary.android.callback.ErrorInfo;
import com.cloudinary.android.callback.UploadCallback;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Level;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    LinearLayout textLayout,imageLayout,videoLayout;
    CardView sendImageCard,sendTextCard,sendVideoCard;
    EditText text;
    Button saveText,saveImage,chooseImage,chooseVideo,saveVideo;
    TextView videoText;
    ImageView image;
    ProgressDialog progressDialog;
    String selectedImagePath;

    int i1=0;

    private static final int PERMISSION_CODE = 1;
    private static final int PICK_IMAGE = 1,PICK_VIDEO=2;
    String filePath;
    Map config = new HashMap();
    private void configCloudinary() {
        config.put("cloud_name", "drlf6gntz");
        config.put("api_key", "894749617857176");
        config.put("api_secret", "Qp-ckIp4k_xIresVZF7Gms0WrPY");
        config.put("resource_type", "auto");
        MediaManager.init(MainActivity.this, config);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getSupportActionBar().hide();

        progressDialog = new ProgressDialog(MainActivity.this);

        progressDialog.setMessage("Loading");
        progressDialog.setProgressStyle(ProgressDialog.STYLE_SPINNER);


        textLayout=findViewById(R.id.textlayout);
        text=findViewById(R.id.text);
        saveText=findViewById(R.id.savetext);

        sendImageCard=findViewById(R.id.sendImageCard);
        sendTextCard=findViewById(R.id.senTextCard);
        sendVideoCard=findViewById(R.id.sendVideoCard);

        imageLayout=findViewById(R.id.imageLayout);
        image=findViewById(R.id.image);
        chooseImage=findViewById(R.id.chooseImage);
        saveImage=findViewById(R.id.saveImage);

        videoLayout=findViewById(R.id.videoLayout);
        chooseVideo=findViewById(R.id.chooseVideo);
        saveVideo=findViewById(R.id.saveVideo);
        videoText=findViewById(R.id.videoText);

        configCloudinary();

        sendTextCard.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textLayout.setVisibility(View.VISIBLE);
                imageLayout.setVisibility(View.GONE);
                videoLayout.setVisibility(View.GONE);
            }
        });

        sendImageCard.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textLayout.setVisibility(View.GONE);
                imageLayout.setVisibility(View.VISIBLE);
                videoLayout.setVisibility(View.GONE);
            }
        });

        sendVideoCard.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textLayout.setVisibility(View.GONE);
                imageLayout.setVisibility(View.GONE);
                videoLayout.setVisibility(View.VISIBLE);
            }
        });

        saveText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String s=text.getText().toString();
                checkText(s);
            }
        });

        chooseImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                i1=1;
                requestPermission();
            }
        });
        chooseVideo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                i1=2;
                requestPermission();
            }
        });

        saveImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                uploadToCloudinary(filePath,1);
            }
        });

        saveVideo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                uploadToCloudinary(selectedImagePath,2);
            }
        });



    }

    void checkText(String text){
        progressDialog.show();

        JSONObject object = new JSONObject();

        try {
            object.put("text",text);
            object.put("type","text");
        } catch (JSONException e) {
            e.printStackTrace();
        }



        final OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        MediaType mediaType = MediaType.parse("application/json");
        RequestBody body = RequestBody.create(mediaType, object.toString());
        final Request request = new Request.Builder()
                .url("https://jatayuhost3.herokuapp.com/")
                .method("POST", body)
                .addHeader("Content-Type", "application/json")
                .build();
        final okhttp3.Response response2;

        AsyncTask<Void, Void, String> asyncTask =
                new AsyncTask<Void, Void, String>() {
                    @Override
                    protected String doInBackground(Void... params) {
                        try {
                            String m;
                            okhttp3.Response response = client.newCall(request).execute();



                            progressDialog.dismiss();

                            if (!response.isSuccessful()) {
                                //  Toast.makeText(MainActivity.this, "Error", Toast.LENGTH_LONG).show();
                                return String.valueOf(response.code());
                            } else {
                                //  Toast.makeText(MainActivity.this, "Text is " + response.body(), Toast.LENGTH_LONG).show();
                                return response.body().string();
                            }

                        } catch (Exception e) {
                            e.printStackTrace();
                            return e.toString();


                        }
                    }

                    @Override
                    protected void onPostExecute(String s) {
                        super.onPostExecute(s);

                        if (s.equals("200") || s.equals("201")) {


                        }
                        else
                        {
                            Toast.makeText(MainActivity.this,"Text is "+s, Toast.LENGTH_LONG).show();
                        }
                    }
                };

        if (asyncTask.execute().equals("1")) {}


    }

    void checkText2(String url){
        progressDialog.show();

        JSONObject object = new JSONObject();

        try {
            object.put("image",url);
            object.put("type","image");
        } catch (JSONException e) {
            e.printStackTrace();
        }



        final OkHttpClient client = new OkHttpClient().newBuilder()
                .build();
        MediaType mediaType = MediaType.parse("application/json");
        RequestBody body = RequestBody.create(mediaType, object.toString());
        final Request request = new Request.Builder()
                .url("https://jatayuhost3.herokuapp.com/")
                .method("POST", body)
                .addHeader("Content-Type", "application/json")
                .build();
        final okhttp3.Response response2;

        AsyncTask<Void, Void, String> asyncTask =
                new AsyncTask<Void, Void, String>() {
                    @Override
                    protected String doInBackground(Void... params) {
                        try {
                            String m;
                            okhttp3.Response response = client.newCall(request).execute();



                            progressDialog.dismiss();

                            if (!response.isSuccessful()) {
                                //  Toast.makeText(MainActivity.this, "Error", Toast.LENGTH_LONG).show();
                                return String.valueOf(response.code());
                            } else {
                                //  Toast.makeText(MainActivity.this, "Text is " + response.body(), Toast.LENGTH_LONG).show();
                                return response.body().string();
                            }

                        } catch (Exception e) {
                            e.printStackTrace();
                            return e.toString();


                        }
                    }

                    @Override
                    protected void onPostExecute(String s) {
                        super.onPostExecute(s);

                        if (s.equals("200") || s.equals("201")) {


                        }
                        else
                        {
                            Toast.makeText(MainActivity.this,"Image is "+s, Toast.LENGTH_LONG).show();
                        }
                    }
                };

        if (asyncTask.execute().equals("1")) {}


    }


    private void uploadToCloudinary(String filePath,final int i) {

        MediaManager.get().upload(filePath).callback(new UploadCallback() {
            @Override
            public void onStart(String requestId) {
                progressDialog.show();

            }
            @Override
            public void onProgress(String requestId, long bytes, long totalBytes) {

            }
            @Override
            public void onSuccess(String requestId, Map resultData) {
                progressDialog.dismiss();


                if(i==1) {
                    checkText2(resultData.get("url").toString());
                }
                else if(i==2){
                    Toast.makeText(MainActivity.this,"Done "+resultData.get("url").toString(),Toast.LENGTH_LONG).show();
                }

            }
            @Override
            public void onError(String requestId, ErrorInfo error) {
                Toast.makeText(MainActivity.this,"Done "+error.getDescription(),Toast.LENGTH_LONG).show();
            }
            @Override
            public void onReschedule(String requestId, ErrorInfo error) {

            }
        }).dispatch();
    }

    private void requestPermission(){
        if(ContextCompat.checkSelfPermission
                (MainActivity.this,
                        Manifest.permission.READ_EXTERNAL_STORAGE
                ) == PackageManager.PERMISSION_GRANTED
        ){
            accessTheGallery();
        } else {
            ActivityCompat.requestPermissions(
                    MainActivity.this,
                    new String[]{Manifest.permission.READ_EXTERNAL_STORAGE},
                    PERMISSION_CODE
            );
        }
    }
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if(requestCode== PERMISSION_CODE){
            if(grantResults.length>0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                accessTheGallery();
            }else {
                Toast.makeText(MainActivity.this, "permission denied", Toast.LENGTH_SHORT).show();
            }
        }
    }

    public void accessTheGallery(){
        Intent i = new Intent(
                Intent.ACTION_PICK,
                android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI
        );
        if(i1==1) {
            i.setType("image/");
            startActivityForResult(i, PICK_IMAGE);
        }
        else if(i1==2){
            i.setType("video/*");
            startActivityForResult(i, PICK_VIDEO);
        }
}
@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
 super.onActivityResult(requestCode, resultCode, data);
 //get the image’s file location
 filePath = getRealPathFromUri(data.getData(), MainActivity.this);
 if(requestCode==PICK_IMAGE && resultCode==RESULT_OK){
  try {
   //set picked image to the mProfile
   Bitmap bitmap = MediaStore.Images.Media.getBitmap(
    getContentResolver(),
    data.getData());
   image.setImageBitmap(bitmap);
  } catch (IOException e) {
   e.printStackTrace();
  }
 }

 if(requestCode==PICK_VIDEO && resultCode==RESULT_OK){

     Uri selectedImageUri = data.getData();

     // OI FILE Manager
     String filemanagerstring = selectedImageUri.getPath();

     // MEDIA GALLERY
     selectedImagePath = getPath(selectedImageUri);
     videoText.setText(selectedImagePath);


 }

}

    public String getPath(Uri uri) {
        String[] projection = { MediaStore.Video.Media.DATA };
        Cursor cursor = getContentResolver().query(uri, projection, null, null, null);
        if (cursor != null) {
            // HERE YOU WILL GET A NULLPOINTER IF CURSOR IS NULL
            // THIS CAN BE, IF YOU USED OI FILE MANAGER FOR PICKING THE MEDIA
            int column_index = cursor
                    .getColumnIndexOrThrow(MediaStore.Video.Media.DATA);
            cursor.moveToFirst();
            return cursor.getString(column_index);
        } else
            return null;
    }

private String getRealPathFromUri(Uri imageUri, Activity activity){
 Cursor cursor = activity.getContentResolver().query(imageUri, null,  null, null, null);
 if(cursor==null) {
  return imageUri.getPath();
 }else{
  cursor.moveToFirst();
  int idx =  cursor.getColumnIndex(MediaStore.Images.ImageColumns.DATA);
  return cursor.getString(idx);
 }
}

}
