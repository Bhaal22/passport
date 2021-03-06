var ProfileSelectionController = function ($scope, $http) {
  $scope.profiles = [];
  $scope.profileuri = "/training/api/v1/profile";

  var dataToSend = {
    content: $scope.profiles
  };

  $http.get($scope.profileuri, {
    headers: { 'Content-Type': 'application/json' }})
    .success(function (data) {
      var t = toastr.info('Getting Profiles succeeded');
      toastr.info(data.objects.length);
      $scope.profiles = data.objects;
      $scope.profile = $scope.profiles[0];
    }).error(function (data) {
    });

  


};

athleteManager.controller('ProfileSelectionController', ['$scope', '$http', ProfileSelectionController]);
