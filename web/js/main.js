(function(){
	var app = angular.module("thumail", []);

	app.controller("MailboxController", ['$http', function($http){
		var mailbox = this;
		mailbox.mails = [];
		mailbox.currentMail = {};

		$http.get('/data/mini-last.json').success(function(data){
			mailbox.mails = data;
			mailbox.currentMail = data[0];
		});
	}]);
})();
