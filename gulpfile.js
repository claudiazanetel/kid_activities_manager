var gulp = require('gulp');
var bower = require('gulp-bower');
var cleanCSS = require('gulp-clean-css');
var minify = require('gulp-minify');
var concat = require('gulp-concat');  
var rename = require('gulp-rename');

//Default task
gulp.task('default', ['bower', 'minify-css','minify-js']);  

gulp.task('bower', function() {
 	return bower('./static/dist/components')
});

gulp.task('minify-css', function() {
  	return gulp.src([
  		'./static/css/style.css'
  	])
	.pipe(concat('site.css'))
    .pipe(gulp.dest('./static/dist/css'))
    .pipe(rename('site-min.css'))
    .pipe(cleanCSS())
    .pipe(gulp.dest('./static/dist/css'));
});

gulp.task('minify-js', function() {
  	return gulp.src([
  		'./static/dist/components/jquery/dist/jquery.js',
  		'./static/dist/components/bootstrap/dist/js/bootstrap.js',
  		'./static/js/javascript.js'
	])
    .pipe(concat('site.js'))
    .pipe(gulp.dest('./static/dist/js'))
    //.pipe(rename('site.js'))
    .pipe(minify())
    .pipe(gulp.dest('./static/dist/js'))
});