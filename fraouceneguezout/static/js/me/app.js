'use strict';


var app = angular.module('MainApp', [
    'ui.bootstrap',
    'ui.router',
    'angular-svg-round-progress',
    'ngSanitize'
]);

app.config(function($interpolateProvider, roundProgressConfig) {

    // Use square brackets instead of curly brackets
    //$interpolateProvider.startSymbol('[[');
    //$interpolateProvider.endSymbol(']]');

    //  Global customization for angular-svg-round-progress
    _.assign(roundProgressConfig, {
        max: 100,
        color: 'rgb(138, 231, 38)',
        bgcolor: '#DCDCCC',
        radius: '40',
        stroke: '6',
        rounded: 'true'
    });
});
