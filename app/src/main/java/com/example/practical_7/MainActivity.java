package com.example.practical_7;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.ActionMode;
import android.view.ContextMenu;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;
public class MainActivity extends AppCompatActivity {
    TextView text1, text2;
    private ActionMode actionMode;
    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        text1 = findViewById(R.id.t1);
        text2 = findViewById(R.id.t2);
        registerForContextMenu(text1);
        text2.setOnLongClickListener(new View.OnLongClickListener() {
            public boolean onLongClick(View view) {
                if (actionMode != null)
                    return false;
                actionMode =MainActivity.this.startActionMode(actionModeCallback);
                view.setSelected(true);
                return true;
            }
        });
    }
    public ActionMode.Callback actionModeCallback=new ActionMode.Callback() {
        @Override
        public boolean onCreateActionMode(ActionMode mode, Menu menu){
            getMenuInflater().inflate(R.menu.menu3,menu);
            return true;
        }
        @Override
        public boolean onPrepareActionMode(ActionMode mode, Menu menu) {
            return false;
        }
        @Override
        public boolean onActionItemClicked(ActionMode mode, MenuItem item) {
            switch (item.getItemId())
            {
                case R.id.item7:
                    Toast.makeText(MainActivity.this,"Edit CAB selected",Toast.LENGTH_LONG);
                    mode.finish();
                    return true;
                case R.id.item8:
                    Toast.makeText(MainActivity.this,"Share CAB selected",Toast.LENGTH_LONG);
                    mode.finish();
                    return true;
                default:
                    return false;
            }
        }
        @Override
        public void onDestroyActionMode(ActionMode mode)
        {
            actionMode= null;
        }
    };

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo)
    {
        super.onCreateContextMenu(menu, v, menuInfo);
        getMenuInflater().inflate(R.menu.menu2, menu);
    }

    @Override
    public boolean onContextItemSelected(@NonNull MenuItem item)
    {
        switch (item.getItemId())
        {
            case R.id.item4:
                Toast.makeText(this, "Edit Context menu Selected", Toast.LENGTH_LONG);
                return true;
            case R.id.item5:
                Toast.makeText(this, "Share Context menu Selected", Toast.LENGTH_LONG);
                return true;
            case R.id.item6:
                Toast.makeText(this, "Delete Context menu Selected", Toast.LENGTH_LONG);
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        super.onCreateOptionsMenu(menu);
        getMenuInflater().inflate(R.menu.menu1, menu);
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item)
    {
        switch (item.getItemId())
        {
            case R.id.item1:
                Toast.makeText(this, "Search Option menu Selected", Toast.LENGTH_LONG);
                return true;
            case R.id.item2:
                Toast.makeText(this, "Cart Option menu Selected", Toast.LENGTH_LONG);
                return true;
            case R.id.item3:
                Toast.makeText(this, "Settings Option menu Selected", Toast.LENGTH_LONG);
                return true;
            default:
                return super.onContextItemSelected(item);
        }
    }
}