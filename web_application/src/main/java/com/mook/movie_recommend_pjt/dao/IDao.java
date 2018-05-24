package com.mook.movie_recommend_pjt.dao;

import java.util.ArrayList;

import com.mook.movie_recommend_pjt.dto.ContentDto;

public interface IDao {
	
	public ArrayList<ContentDto> listDao();
	public void writeDao(String mWriter, String mContent);
	public ContentDto viewDao(String strID);
	public void deleteDao(String bId);
	
}
