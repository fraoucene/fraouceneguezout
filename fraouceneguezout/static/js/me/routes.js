'use strict';


app.config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/resume');
    $stateProvider.
        state('about', {
            url: '/about',
            templateUrl: 'partials/about.html',
            controller: 'AboutController'
        }).
        state('blog', {
            url: '/blog',
            templateUrl: 'partials/blog.html',
            controller: 'BlogController'
        }).
        state('question', {
            url: '/question',
            templateUrl: 'partials/question.html',
            controller: 'QuestionController'
        }).
        state('resume', {
            url: '/resume',
            templateUrl: 'partials/resume.html',
            controller: 'ResumeController'
        });
        
});
