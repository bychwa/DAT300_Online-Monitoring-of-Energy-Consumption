<?php

class DashboardController extends BaseController {


	public function index()
	{
		return View::make('dashboard');
	}
	public function usage()
	{
		return View::make('usage');
	}
	public function setup()
	{
		return View::make('setup');
	}

	

}
