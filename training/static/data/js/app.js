var athleteManager = angular.module('athleteManager', ['ngRoute', 'ngCookies', 'ngGrid']);

athleteManager.config(function ($routeProvider) {
  $routeProvider
    .when('/',
          {
            controller: 'ProfileSelectionController',
            templateUrl: '/static/data/htmlparts/ProfileSelection.html'
          })
    .when('/passport',
          {
            controller: 'PassportController',
            templateUrl: '/static/data/htmlparts/Passport.html'
          })
    .otherwise({ redirectTo: '/' });
  
});

toastr.options = {
 "positionClass": "toast-bottom-right",
  "fadeIn": 600,
  "fadeOut": 1000,
  "timeOut": 5000,
  "extendedTimeOut": 1000
}
