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
  <script src="js/plugins.js"></script>

  <!-- App Scripts -->
  <script src="js/scripts.js"></script>
  
@stop

@section('body_contents')
	@yield('login_body')
@stop