var gulp = require('gulp');
var bower = require('gulp-bower');


//Default task
gulp.task('default', ['bower']);  

gulp.task('bower', function() {
 return bower('./static/components')
});