@extends('templates.master')

@section('document_styles')
	<link rel="stylesheet" href="css/style.css">
  	<script src="js/jquery.js"></script>
		  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
	  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	  <!--[if lt IE 9]>
		<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
		<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	  <![endif]-->
@stop
@section('document_scripts')
	<!-- Plugins -->
    <script src="js/plugins.min.js"></script>

    
    <!-- Loaded only in index.html for demographic vector map-->
    <script src="js/jvectormap.js"></script>
    
    <!-- App Scripts -->
    <script src="js/scripts.js"></script>
  
@stop

@section('dashboard_footer')
	<div class="container margin-top">
				    <div class="footer">
					<a href="index.html" class="brand">
						<i class="md md-multitrack-audio"></i> Blueprint
					</a>
					<ul>
						<li><a href="#">Contact us</a></li>
						<li><a href="#">Support</a></li>
					</ul>
				</div>
  </div>
    <div class="overlay-disabled"></div>
@stop

@section('dashboard_header')
	<nav class="navbar navbar-default navbar-fixed-top">
	<div class="container">
		<!-- Brand and toggle get grouped for better mobile display -->
		<div class="navbar-header">
			<button type="button" class="navbar-toggle visible-xs collapsed pull-left"  data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
				<i class="md md-menu"></i>
			</button>
			<a class="navbar-brand" href="">EMAC Dashboard</a>
			<button type="button" class="navbar-toggle pull-right" id="showRightPush">
				<i class="md md-more-vert"></i>
			</button>
		</div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li><a href="setup">Setup</a></li>
				<li><a href="usage">Usage</a></li>
				<li class="active"><a href="">Settings</a></li>
            </ul>
							<ul class="nav navbar-nav navbar-right hidden-xs">
								<li class="active dropdown">
									<button class="btn btn-default navbar-btn btn-rounded"  data-toggle="dropdown">
										<i class="md md-notifications"></i>
									</button>
									<div class="dropdown-menu dropdown-caret dropdown-caret-right  width-300">
										<div class="dropdown-padding dropdown-headline">
											<div class="media dropdown-head">
												<div class="media-body media-middle">
													<h4 class="">Notifications <small class="bold text-muted">(3 new)</small></h4>
												</div>
												<div class="media-right media-middle">
													<a href="#" class="text-muted"><i class="md md-list"></i></a>
												</div>
											</div>
										</div>
										<div class="dropdown-padding">
											<div class="notification-block body-bg">
													<span class="notification-icon orange">
														<i class="md md-comment"></i>
													</span>
													<span class="notification-content">
														Andrew replied to <a href="#">"How do I use Grunt?"</a>
													</span>
													<small>2 min ago</small>
											</div>
											<div class="notification-block body-bg">
													<span class="notification-icon green">
														<i class="md md-today"></i>
													</span>
													<span class="notification-content">
														Event <a href="#">SEO Conference</a> started
													</span>
													<small>2 min ago</small>

											</div>
											<div class="notification-block body-bg">

													<span class="notification-icon primary">
														<i class="md md-timelapse"></i>
													</span>
													<span class="notification-content">
														2h 40min left to <a href="#">General Board Meeting</a>.
													</span>
													<small>2 min ago</small>

											</div>
										</div>
										<div class="dropdown-padding text-center">
											<a href="#">View all</a>
										</div>
									</div>
								</li>
								<li class="dropdown">
									<button class="btn btn-default-light navbar-btn btn-rounded"  data-toggle="dropdown">
										<i class="md md-language"></i>
									</button>
									<ul class="dropdown-menu dropdown-caret dropdown-caret-right dropdown-menu-auto">
										<li><a href="#">English</a></li>
										<li><a href="#">Swedish</a></li>
										<li><a href="#">Swahili</a></li>
										<li><a href="#">Zambia</a></li>
									</ul>
								</li>
								<li class="dropdown">
									<button class="btn btn-default-light navbar-btn btn-rounded"  data-toggle="dropdown">
										<i class="md md-person"></i>
									</button>
									<ul class="dropdown-menu dropdown-caret dropdown-caret-right dropdown-menu-auto">
										<li><a href="#">Profile</a></li>
										<li><a href="logout">logout</a></li>
									</ul>
								</li>
								
							</ul>
						</div>
					</div>
				</nav>
				    <div class="sidebar right-side" id="sidebar-right">
					<!-- Wrapper Reqired by Nicescroll -->
					<div class="nicescroll">
						<div class="wrapper">
							<div class="block-primary">
								<div class="media">
									<div class="media-left media-middle">
										<a href="#">
											<img src="images/guy.jpg" alt="person" class="img-circle border-white" width="60"/>
										</a>
									</div>
									<div class="media-body media-middle">
										<a href="account.html" class="h4">Andrew Brain</a>
										<a href="login.html" class="logout pull-right"><i class="md md-exit-to-app"></i></a>
									</div>
								</div>
							</div>
							<ul class="nav nav-sidebar" id="sidebar-menu">
								<li><a href="account.html"><i class="md md-person-outline"></i> Account</a></li>
								<li><a href="email.html"><i class="md md-email"></i> Emails</a></li>
								<li><a href="#"><i class="md md-attach-money"></i> Payments</a></li>
								<li><a href="#"><i class="md md-settings"></i> Settings</a></li>
								<li><a href="login.html"><i class="md md-exit-to-app"></i> Logout</a></li>
							</ul>
						</div>
					</div>
				</div>
@stop
@section('body_contents')
	
	@yield('dashboard_header')
	@yield('dashboard_body')
	@yield('dashboard_footer')
@stop