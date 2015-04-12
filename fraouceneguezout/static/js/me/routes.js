'use strict';


app.config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/resume');
    $stateProvider.
        state('resume', {
            url: '/resume',
            templateUrl: 'partials/resume.html',
            controller: 'ResumeController'
        });
        
});
