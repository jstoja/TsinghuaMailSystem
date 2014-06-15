(function(){
	var app = angular.module("thumail", []);

	app.controller("MailboxController", ['$http', function($http){
		var mailbox = this;
		mailbox.userNumber = 0;
		mailbox.mails = [];
		mailbox.currentMail = {};
		mailbox.listStatus = 'All';
		mailbox.user = {};

		this.getUser = function() {
			$http.get('/user/' + String(mailbox.userNumber)).success(function(data) {
				mailbox.user = data;
				console.log(data);
			});
		};

		this.getMails = function(userid) {
			$http.get('/mail/user/' + String(mailbox.userNumber)).success(function(data){
				mailbox.mails = data;
				mailbox.currentMail = data[0];
			});
		};

		this.updateUser = function() {
			mailbox.getUser();
			mailbox.getMails();
		};

		this.getUser();
		this.getMails();

		this.show = function(st) {
			mailbox.listStatus = st;
		};

		this.getSelectedMails = function() {
			if (mailbox.listStatus === 'All') {
				return (mailbox.mails);
			} else if (mailbox.listStatus === 'Received') {
				return mailbox.getXMails(function(mail, username) {
					return (mail.receiver === username);
				});
			} else if (mailbox.listStatus === 'Sent') {
				return mailbox.getXMails(function(mail, username) {
					return (mail.sender === username);
				});
			}
		};

		this.getXMails = function(filter) {
			var mails = [];
			for (var i = 0; i < mailbox.mails.length; i++) {
				if (filter(mailbox.mails[i], mailbox.user.name)) {
					mails.push(mailbox.mails[i]);
				}
			};
			return (mails);
		}

		this.printInfoTitle = function(mail) {
			if (mailbox.listStatus === 'All') {
				if (mail.sender === mailbox.user.name) {
					return ("Receiver: " + mail.receiver);
				} else {
					return ("Sender: " + mail.sender);
				}
			} else if (mailbox.listStatus === 'Received') {
				return ("Sender: " + mail.sender);
			} else if (mailbox.listStatus === 'Sent') {
				return ("Receiver: " + mail.receiver);
			}

		};
	}]);
})();
