var gulp = require('gulp');
var bower = require('gulp-bower');
var cleanCSS = require('gulp-clean-css');


//Default task
gulp.task('default', ['bower', 'minify-css']);  

gulp.task('bower', function() {
 return bower('./static/dist/components')
});

gulp.task('minify-css', function() {
  return gulp.src('./static/css/style.css')
    .pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest('./static/dist/css'));
});