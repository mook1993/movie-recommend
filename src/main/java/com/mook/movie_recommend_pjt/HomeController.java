package com.mook.movie_recommend_pjt;

import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;

import javax.servlet.http.HttpServletRequest;

import org.apache.ibatis.session.SqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import com.mook.movie_recommend_pjt.dao.IDao;

/**
 * Handles requests for the application home page.
 */
@Controller
public class HomeController {
	
	private static final Logger logger = LoggerFactory.getLogger(HomeController.class);
		
//	SqlSession�꽭�뀡 媛앹껜 �깮�꽦
	@Autowired // �꽑�뼵怨� �룞�떆�뿉 �뒪�봽留� �꽕�젙�뙆�씪�뿉 �젙�쓽�븳 媛믪쑝濡� 珥덇린�솕
	private SqlSession sqlSession;
	
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String home(Locale locale, Model model) {
		logger.info("Welcome home! The client locale is {}.", locale);
		 
		Date date = new Date();
		DateFormat dateFormat = DateFormat.getDateTimeInstance(DateFormat.LONG, DateFormat.LONG, locale);
		
		String formattedDate = dateFormat.format(date);
		
		model.addAttribute("serverTime", formattedDate );
		
		return "home";
	}
	
//	(�닚�꽌3) 留ㅽ븨 xml�뙆�씪�뿉 留욊쾶�걫 而⑦듃濡ㅻ윭 �닔�젙
	@RequestMapping("/list")
	public String list(Model model) {
		IDao dao=sqlSession.getMapper(IDao.class);	//留ㅽ띁 xml�뙆�씪�쓣 IDao�겢�옒�뒪 ���엯�쑝濡� 諛섑솚
		model.addAttribute("list",dao.listDao());
		return "/list";
	}
	
	@RequestMapping("/writeForm")
	public String writeForm() {
		
		return "/writeForm";
	}
	
	@RequestMapping("/write")
	public String write(HttpServletRequest request, Model model) {
		IDao dao=sqlSession.getMapper(IDao.class);
		dao.writeDao(request.getParameter("mWriter"), request.getParameter("mContent"));
		return "redirect:list";
	}
	
	@RequestMapping("/view")
	public String view() {
		return "/view";
	}
	
	@RequestMapping("/delete")
	public String delete(HttpServletRequest request, Model model) {
		IDao dao=sqlSession.getMapper(IDao.class);
		dao.deleteDao(request.getParameter("mId"));
		return "redirect:list";
	}
	
}
