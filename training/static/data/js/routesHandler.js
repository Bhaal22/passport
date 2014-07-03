athleteManager.run(function($rootScope, $http, $cookies) { 
  $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
})
