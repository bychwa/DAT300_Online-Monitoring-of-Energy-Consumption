<?php

class LoginController extends BaseController {


	public function index()
	{
		return View::make('login');
	}
	public function logout()
	{
		Auth::logout();	
		return Redirect::back();
	}

	public function do_login()
	{
		if(Auth::attempt(Input::all())){
			return Redirect::to('dashboard');
		}else{
			return Redirect::back()->with('message','login failed!');
		}
	}

}
