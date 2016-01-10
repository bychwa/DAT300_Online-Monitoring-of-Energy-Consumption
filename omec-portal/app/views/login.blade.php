@extends('templates.login_template')

@section('document_title')
	<title>EMAC-Login</title>
@stop

@section('login_body')
<div class="container-fluid">      
	<div id="main">
	    <div class="row">
	    <div class="col-md-4 col-md-offset-4">
	        <div class="login">

	            <div class="logo" href="#"><i class="md md-lg md-multitrack-audio"></i> OMEC Login</div>
	            <div class="panel panel-default panel-shadow">
	                <form action="" method="post">
	                    <div class="panel-body">
	                        <div class="form-group">
	                            <label for="">Username</label>
	                            <input type="text" class="form-control" name="username" placeholder="Enter username">
	                        </div>
	                        <div class="form-group margin-none">
	                            <div class="media">
	                                <div class="media-body media-middle">
	                                    <label>Password</label>
	                                </div>
	                                <div class="media-right media-middle">
	                                    <a href="#" class="small pull-right">Forgot?</a>
	                                </div>
	                            </div>
	                            <input type="password" class="form-control" name="password" placeholder="Password">
	                        </div>
	                    </div>
	                    <div class="form-group text-center">
	                        <button type="submit" class="btn btn-primary">Login <i class="md md-lock-open"></i></button>
	                    </div>
	                </form>
	            </div>
	            <div class="text-center">
	                <p class="text-muted">or login with</p>
	                <a href="#" class="btn btn-default btn-rounded"><i class="fa fa-facebook fa-fw"></i></a>
	                <a href="#" class="btn btn-default btn-rounded"><i class="fa fa-twitter fa-fw"></i></a>
	                <a href="#" class="btn btn-default btn-rounded"><i class="fa fa-google-plus fa-fw"></i></a>
	            </div>
	        </div>
	    </div>
	</div>
	</div>


	  </div>


@stop