angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  $stateProvider
    .state('tabsController.dashboard', {
      url: '/dashboard',
      views: {
        'tab1': {
          templateUrl: 'templates/dashboard.html',
          controller: 'dashboardCtrl'
        }
      }
    })

    .state('tabsController.addSocket', {
      url: '/addSocket',
      views: {
        'tab2': {
          templateUrl: 'templates/addSocket.html',
          controller: 'addSocketCtrl'
        }
      }
    })
    .state('tabsController.settings', {
      url: '/settings',
      views: {
        'tab3': {
          templateUrl: 'templates/settings.html',
          controller: 'settingsCtrl'
        }
      }
    })
        
      
    
      
    .state('tabsController', {
      url: '/Main',
      abstract:true,
      templateUrl: 'templates/tabsController.html'
    })
      
    ;

  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/Main/dashboard');

});