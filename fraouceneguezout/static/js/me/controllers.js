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
        var about = {}
        about.title ={
            fr: response.results[0]["title_fr"],
            en:response.results[0]["title"]
        }
        about.content ={
            fr: response.results[0]["body_fr"],
            en:response.results[0]["body"]
        }
        $scope.about = about
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
        var data = []
        _.each(response.results, function(experience){
            var item = {}
            item.discription ={
                fr: experience["description_fr"],
                en: experience["description"]
            }
            item.title ={
                fr: experience["title_fr"],
                en: experience["title"]
            }
            item.detail ={
                fr: experience["detail_fr"],
                en: experience["detail"]
            }
            item.company = experience.company
            item.duration = experience.duration
            item.tools = experience.tools
            item.location = experience.location
            item.lien = experience.lien
            item.start_on = experience.start_on
            item.end_on = experience.end_on
            item.messageshow = {en:"Show more", fr:"Plus"}
            item.messagehide = {en:"Show less", fr:"moins"} 
            data.push(item)
        })
        $scope.data.experiences = data
    });

    // Get content for the education section
    $http.get('/api/resume/education/').success(function(response) {
        //$scope.data.education = response;
         var data = []
        _.each(response.results, function(etude){
            var item = {}
            item.discription ={
                fr: etude["description_fr"],
                en: etude["description"]
            }
            item.title ={
                fr: etude["title_fr"],
                en: etude["title"]
            }
            item.detail ={
                fr: etude["detail_fr"],
                en: etude["detail"]
            }
            item.school = etude.school
            item.duration = etude.duration
            item.tools = etude.tools
            item.location = etude.location
            item.lien = etude.lien
            item.start_on = etude.start_on
            item.end_on = etude.end_on
            item.messageshow = {en:"Show more", fr:"Plus"}
            item.messagehide = {en:"Show less", fr:"moins"} 
            data.push(item)
        })
        $scope.data.education = data
    });
    $scope.language = "en"
    $scope.languagess = []
        $scope.languagess.french = {
            fr : "Français",
            en : "French"
        }
        $scope.languagess.english = {
            fr : "Anglais",
            en : "English"
        }
    
    // Get configuration for titles 
    $http.get('/api/resume/titles/').success(function(response) {
        var data = {}
        _.each(response.results, function(titre){
            var item = {}
            item.label =  {fr:titre['label_fr'],en:titre['label_en'] }
            item.subtitle = {fr:titre['subtitle_fr'],en:titre['subtitle_en'] }
            data[titre.title] =item
        })
        data['info'] ={
            nom :{fr:'Nom',en:'Name'},
            location :{fr:'Adresse',en:'Location'},
            year :{fr:'ans',en:'years'},   
        }
        $scope.titles = data
    });
});
