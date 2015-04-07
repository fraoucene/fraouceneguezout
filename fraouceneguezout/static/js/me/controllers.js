'use strict';


app.controller('AboutController', function() {
});

app.controller('BlogController', function() {
});

app.controller('QuestionController', function() {
});


app.controller('ResumeController', function($scope, $http, $location, anchorSmoothScroll) {
    $scope.configuration = {};
    $scope.data = {};

    // Get configuration for titles and colors
    $http.get('/api/resume/configuration/').success(function(response) {
        $scope.configuration.titles = response.titles;
        $scope.configuration.colors = response.colors;
    });

    // Get content for the about section
    $http.get('/api/resume/about/').success(function(response) {
        $scope.data.about = response.results;
    });

    $scope.scrollto = function (eID){
    $scope.section=eID;
    // set the location.hash to the id of
    // the element you wish to scroll to.
    // call $anchorScroll()
    anchorSmoothScroll.scrollTo(eID); 
    };
    var monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    $scope.getFormatDate = function(date){
        if(date !=null){
            var date = new Date(date)
            var month = '' + (date.getMonth())
            var year = date.getFullYear()
            return monthNames[month]+"-"+year
        }
        else
            return "Current"
    }
    // Get content for the skills section
    $http.get('/api/resume/skills/').success(function(response) {
        //$scope.data.skills = _.groupBy(response, 'row').undefined[3];
        $scope.data.skills = response.results
        var skills = []
        var tools = []
        var languages = []
        var stars_on =[]
        var stars_off =[]
        _.each(response.results, function(skill){
            if (skill.row == 1) {
                skills.push(skill)
            }
            if(skill.row == 2) {
                tools.push(skill)
            }
            if(skill.row == 3) {
                languages.push(skill)
            }
            $scope.getNumber = function(num) {
                return new Array(num);   
            }
            var star_on =[]
            var star_off =[]
                for (var i = skill.grade - 1; i >= 0; i--) {
                    star_on.push(1)   
                };
                stars_on[skill.label]=star_on
                for (var i = (4- skill.grade); i >= 0; i--) {
                    star_off.push(1)   
                };
                stars_off[skill.label]=star_off
                
        })
        $scope.stars_off = stars_off;
        $scope.stars_on = stars_on;
        $scope.skills = skills;
        $scope.tools = tools;
        $scope.languages = languages;
        
    });



    // Get content for the experiences section
    $http.get('/api/resume/experiences/').success(function(response) {
        $scope.data.experiences = response;
    });

    // Get content for the education section
    $http.get('/api/resume/education/').success(function(response) {
        $scope.data.education = response;
    });
});
