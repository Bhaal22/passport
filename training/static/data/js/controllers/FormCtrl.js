var FormCtrl = function ($scope, $http) {

  $scope.submit = function() 
  {
    var t = toastr.info('Submitting ...');
    toastr.info($scope.profile.resource_uri);
  }
};

athleteManager.controller('FormCtrl', ['$scope', '$http', FormCtrl]);
