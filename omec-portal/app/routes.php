<?php



Route::get('/', function()
{
	return View::make('hello');
});

Route::get('/login',['uses'=>'LoginController@index']);
Route::post('/login',['uses'=>'LoginController@do_login']);
Route::get('/logout',['uses'=>'LoginController@logout']);

Route::get('/dashboard',['before'=>'auth','uses'=>'DashboardController@index']);
Route::get('/usage',['before'=>'auth','uses'=>'DashboardController@usage']);
Route::get('/setup',['before'=>'auth','uses'=>'DashboardController@setup']);