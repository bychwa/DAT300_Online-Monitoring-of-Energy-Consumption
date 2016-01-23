angular.module('app.controllers', ['highcharts-ng'])
  
.controller('dashboardCtrl', function($scope,$http,$interval,Readings) {
		
		$scope.series=[];
		Readings.all().then(function(data){
			for(var j=0; j < data.length; j++){
				var s_data=[];
				for (var i = 0; i < data[j][2].length; i++) {
					var power=data[j][2][i][0]; var time=data[j][2][i][1];
					s_data.push([time, Math.round(power)]);
				}
				serie={ name : data[j][1]+" ("+data[j][0]+")" , data : s_data };
				$scope.series.push(serie);
			}
			
		});

		$scope.chartConfig = {
									options:{
										chart:{ type:"line"}
									},
								    title: {
						                text: 'Energy Comsumption Chart'
						            },
						            subtitle: {
						                text: 'Accumulated power comsumption for all sockets today!'
						            },
						            yAxis:{
						            	title:{
						                    text: "Power ( Watts )"
						                },
						                maxZoom: 0.1
						            },
						            xAxis: {
						                gapGridLineWidth: 0,
						                type : 'datetime',
						                title:{
						                    text: "Time"
						                }
						            },

					            series : $scope.series
	       					}

		$scope.change_chart_type=function(type){
			$scope.chartConfig.options.chart.type=type;
		}
		$scope.add_points=function(){
			// $scope.chartConfig.series[0].data.push([(new Date()).getTime()+ 30 *1000,Math.round(Math.random() * 100)]);
		}

		$scope.check_for_new_data=function(){
			
			Readings.all().then(function(data){
				
				if(data.length == $scope.series.length){
					for(var j=0; j < data.length; j++){
						if($scope.series[j].data.length != data[j][2].length){
							if($scope.series[j].data.length < data[j][2].length){
								for(var k=$scope.series[j].data.length; k < data[j][2].length; k++){
									var power=data[j][2][k][0]; var time=data[j][2][k][1];
									$scope.series[j].data.push([time, Math.round(power)]);
								}
							}else{
								for(var k=data[j][2].length; k < $scope.series[j].data.length; k++){
									power=data[j][2][k][0]; time=data[j][2][k][1];
									$scope.series[j].data.push([time, Math.round(power)]);
								}
							}
							
						}
					       
					}

				}				

			});
		}
		
		var promise = $interval($scope.check_for_new_data, 2000);
    
	    // Cancel interval on page changes
	    $scope.$on('$destroy', function(){
	        if (angular.isDefined(promise)) {
	            $interval.cancel(promise);
	            promise = undefined;
	        }
	    });
})
   
.controller('addSocketCtrl', function($scope,$rootScope,Socket) {
	
	Socket.all().then(function(sockets){
		$rootScope.sockets=sockets;
		console.log(sockets);
	});
	
	$scope.set_status=function(socket){

		Socket.set_status(socket).then(function(response){
			console.log('status changed',response);
		});
	}
	$scope.delete_socket=function(index,socket){
		$scope.sockets.splice(index, 1);

		Socket.remove(socket).then(function(response){
			console.log('socket deleted',response);
		});

	}
	$scope.add_socket=function(soc){
		soc.active=false;
		$rootScope.sockets.push(soc);

		Socket.add(soc).then(function(data){
			console.log("socket added!");
		});		
	}
})
   
.controller('settingsCtrl', function($scope,$rootScope,Socket) {
	
	Socket.all().then(function(sockets){
		$rootScope.sockets=sockets;
		console.log(sockets);
	});

	$scope.set_status=function(socket){

		Socket.set_status(socket).then(function(response){
			console.log('status changed',response);
		});
	}
	$scope.add_notification=function(socket){

		Socket.update(socket).then(function(response){
			console.log('socket changed',response);
		});
	}
	$scope.add_threshold=function(socket){

		Socket.update(socket).then(function(response){
			console.log('socket changed',response);
		});
	}
})
    