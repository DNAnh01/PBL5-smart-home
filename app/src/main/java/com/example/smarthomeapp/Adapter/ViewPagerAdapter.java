package com.example.smarthomeapp.Adapter;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;

import com.example.smarthomeapp.View.MainFragment;
import com.example.smarthomeapp.View.NotificationFragment;

public class ViewPagerAdapter extends FragmentPagerAdapter {

    public ViewPagerAdapter(@NonNull FragmentManager fm, int behavior) {
        super(fm, behavior);
    }

    @NonNull
    @Override
    public Fragment getItem(int position) {
        switch (position) {
            case 0:
                return new MainFragment();
            case 1:
                return new NotificationFragment();
            default:
                return new MainFragment();
        }
    }

    @Override
    public int getCount() {
        return 2;
    }
}
