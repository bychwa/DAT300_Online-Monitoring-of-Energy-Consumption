angular.module('app.services', [])
.factory('Socket', function($http,$q) {
  
  return {
    add: function(socket) {
        var deferred = $q.defer();

            $http.get('http://api.bawalab.com/omec/add_socket?mac='+socket.mac+"&name="+socket.name+"&active="+socket.active).then(
                      function(data){
                        deferred.resolve(data.data);
                    },
                    function(error){
                        deferred.reject(error);
                    });
        return deferred.promise;
    },
    remove: function(socket) {
        var deferred = $q.defer();

            $http.get('http://api.bawalab.com/omec/remove_socket?mac='+socket.mac).then(
                      function(data){
                        deferred.resolve(data.data);
                    },
                    function(error){
                        deferred.reject(error);
                    });
        return deferred.promise;
    },
    update: function(socket) {
        var deferred = $q.defer();

            $http.get('http://api.bawalab.com/omec/update_socket?mac='+socket.mac+"&name="+socket.name+"&active="+socket.active+"&threshold="+socket.threshold+"&email="+socket.email).then(
                      function(data){
                        deferred.resolve(data.data);
                    },
                    function(error){
                        deferred.reject(error);
                    });
        return deferred.promise;
    }, 
    all: function(code,player,card) {
        var deferred = $q.defer();
            $http.get('http://api.bawalab.com/omec/all_sockets').then(
                      function(data){
                        deferred.resolve(data.data);
                    },
                    function(error){
                        deferred.reject(error);
                    });
        return deferred.promise;
    }, 
    set_status: function(socket) {
        var deferred = $q.defer();
            $http.get('http://api.bawalab.com/omec/set_status?mac='+socket.mac+'&active='+socket.active).then(
                      function(data){
                        deferred.resolve(data.data);
                    },
                    function(error){
                        deferred.reject(error);
                    });
        return deferred.promise;
      }      
  };
})
.factory('Readings', function($http,$q) {
  
  return {
    all: function() {
        var deferred = $q.defer();
            $http.get('http://api.bawalab.com/omec/all_readings').then(
                      function(data){
                        deferred.resolve(data.data);
                    },
                    function(error){
                        deferred.reject(error);
                    });
        return deferred.promise;
    }      
  };
})
.factory('$localstorage', ['$window', function($window) {
  return {
    set: function(key, value) {
        $window.localStorage[key] = value;
    },
    get: function(key, defaultValue) {
      return $window.localStorage[key] || defaultValue;
    },
    setObject: function(key, value) {
      $window.localStorage[key] = JSON.stringify(value);
    },
    getObject: function(key) {
      return JSON.parse($window.localStorage[key] || '{}');
    }
  }
}]);
