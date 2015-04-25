'use strict';


app.directive('mePopover', function() {
    return function(scope, element) {
      element.popover();
   }
});

app.directive('meTooltip', function() {
    return function(scope, element) {
      element.tooltip();
   }
});

app.directive('experience', function($http) {
    return {
        restrict: 'E',
        scope: {
        	title: '@',
        	company: '@',
        	duration: '@',
            start: '@',
            end: '@',
        	description: '@',
        	tools: '@',
            detail: '@',
        	location: '@',
        	lien: '@',
            messageshow:'@',
            messagehide:'@',
        },
        replace:true,
        templateUrl: '/partials/experiences.template.html',
        controller: function($scope) {
            $scope.getNbrMonth = function(start, end) {
                
            if(end !=null){
                var start = new Date(start)
                var end = new Date(end)
                var years = end.getFullYear()-start.getFullYear()
                if(end.getMonth()<start.getMonth()){
                    years = years-1
                    if (years > 1)
                        years = years+" years and "
                    if (years==1)
                        years = years+" year and "
                    else
                        years = " "
                    return years+ Math.abs(end.getMonth()-start.getMonth())+" months"
                }
            }
            else{
                // var start = new Date(start)
                // var now =  new Date(Date.now())
                // console.log(start.getMonth())
                // return "since"+ Math.abs(now.getMonth()-start.getMonth())
                return ""
            }
        
    }
        	$http.get('/api/resume/experiences/').success(function(response) {	
           // console.log(response.results[0].start_on)	
            
    	   });

        }
    };
});