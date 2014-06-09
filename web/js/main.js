(function(){
	var app = angular.module("thumail", []);

	app.controller("MailboxController", ['$http', function($http){
		var mailbox = this;
		mailbox.mails = [];
		mailbox.currentMail = {};
		mailbox.urls = ['/data/1.json', '/data/2.json'];


		this.getMails = function(url) {
			$http.get(url).success(function(data){
				mailbox.mails = data;
				mailbox.currentMail = data[0];
			});
		};

		this.getMails("/data/1.json");
	}]);
})();
