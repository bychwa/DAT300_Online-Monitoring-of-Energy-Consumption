@extends('templates.dashboard_template')

@section('document_title')
	<title>OMEC-Dashboard</title>
@stop

@section('dashboard_body')
	
				<div id="notification" data-position="top-right" class="display-none">
				    You have a new message!
				</div>
				<div class="page-header heading-block-primary">
				    <div class="container">
				        <h2>Usage</h2>
				    </div>

				</div>
				<div class="container">
				    <div id="main">
				        
				<div class="media">
				    <div class="media-body clearfix-xs width-100">
				        <div class="panel panel-shadow">
				            <div class="panel-heading">
				                <div class="pull-right btn-group">
				                    <a href="#" class="btn btn-default btn-vertical">2014</a>
				                    <a href="#" class="btn btn-default btn-vertical"><i class="md md-today md-lg text-muted"></i></a>
				                </div>
				                <h4 class="headline">
				                    Stats
				                </h4>
				            </div>

				            <div class="ct-chart ct-chart-animated-line" style="height: 200px; padding-right:15px; overflow: hidden"></div>

				        </div>
				    </div>
				    <div class="media-right clearfix-xs">
				        <div class="panel bg-primary text-center width-300">
				            <div class="h3 margin-b-none">
				                January
				            </div>
				            <div class="h4 margin-t-none light">Total number of sales</div>
				            <div class="panel-body">
				                <i class="fa fa-calendar fa-4x"></i>
				                <div class="h1"> &dollar; 132,562</div>
				            </div>
				        </div>
				    </div>
				</div>
				<div class="row">
				    <div class="col-sm-6 col-md-4">
				        <div class="panel panel-default panel-shadow">
				            <div class="media">
				                <div class="media-left">
				                    <div class="panel-body">
				                        <div class="width-100">
				                            <h5 class="text-muted margin-none" id="graphWeek-y">Active Week</h5>

				                            <h2 class="margin-none" id="graphWeek-a">
				                                $129488
				                            </h2>
				                        </div>
				                    </div>
				                </div>
				                <div class="media-body">
				                    <div class="pull-right width-150">
				                        <div id="graphWeek" style="height: 100px; margin:-5px;"></div>
				                    </div>
				                </div>
				            </div>
				        </div>
				    </div>
				    <div class="col-sm-6 col-md-4">
				        <div class="panel panel-default panel-shadow">
				            <div class="media">
				                <div class="media-left">
				                    <div class="panel-body">
				                        <div class="width-100">
				                            <h5 class="text-muted margin-none" id="graphWeek2-y">2nd Week</h5>

				                            <h2 class="margin-none" id="graphWeek2-a">
				                                $129488
				                            </h2>
				                        </div>
				                    </div>
				                </div>
				                <div class="media-body">
				                    <div class="pull-right width-150">
				                        <div id="graphWeek2" style="height: 100px; margin:-5px;"></div>
				                    </div>
				                </div>
				            </div>
				        </div>
				    </div>
				    <div class="col-sm-6 col-md-4">
				        <div class="panel panel-grey panel-shadow">
				            <div class="media">
				                <div class="media-left">
				                    <div class="panel-body">
				                        <div class="width-100">
				                            <h5 class="margin-none" id="graphWeek3-y">3nd Week</h5>

				                            <h2 class="margin-none" id="graphWeek3-a">
				                                $129488
				                            </h2>
				                        </div>
				                    </div>
				                </div>
				                <div class="media-body">
				                    <div class="pull-right width-150">
				                        <div id="graphWeek3" style="height: 100px; margin:-5px;"></div>
				                    </div>
				                </div>
				            </div>
				        </div>
				    </div>
				</div>
				
				    </div>
				</div>

				  


@stop