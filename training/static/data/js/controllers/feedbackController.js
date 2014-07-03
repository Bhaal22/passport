var FeedbackController = function ($scope) {
    $scope.mail = {};
    
    $scope.openFeedbackDialog = function () {
      var t = toastr.info('Processing Audit Report file...');
    };

      /*
        var d = $dialog.dialog($scope.opts);
        d.open().then(function (result) {
            if (result) {
                var promise = mailingService.sendMail(result);
                promise.then(function (message) {
                    toastr.success(EMAIL_SENT_SUCCESS);
                }, function (errorMessage) {
                    toastr.error('The mail could not be sent. [Error details: ' + errorMessage + ']');
                });
            } else {
                $log.info('Action Cancelled');
            }
        }, function (error) {
            $log.error(error);
        });
        */
};

athleteManager.controller('FeedbackController', FeedbackController);
