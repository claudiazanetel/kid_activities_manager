var gulp = require('gulp');
var bower = require('gulp-bower');
var cleanCSS = require('gulp-clean-css');
var minify = require('gulp-minify');
var concat = require('gulp-concat');  
var rename = require('gulp-rename');
var del = require('del');

//Default task
gulp.task('default', ['clean']);  

/*
* downloads front-end dependencies
*/
gulp.task('bower', function() {
    return bower('./tmp/components')
});

/*
* minifies the site css
*/
gulp.task('minify-site-css', function() {
    return gulp.src([
        './assets/css/style.css'
    ])
    .pipe(cleanCSS())
    .pipe(gulp.dest('./tmp/css'));
});

/*
* concatenates the minified site css with the dependecies (bootstrap, ...) 
*/
gulp.task('concat-css', ['bower', 'minify-site-css'], function() {
    return gulp.src([
        './tmp/components/bootstrap/dist/css/bootstrap.min.css',
        './tmp/css/style.css'
    ])
    .pipe(concat('site.min.css'))
    .pipe(gulp.dest('./static/css'))
});

/*
* copies images into the static folder
*/
gulp.task('copy-fonts', ['bower'], function() {
    return gulp.src(['./tmp/components/bootstrap/dist/fonts/**/**']).pipe(gulp.dest('./static/fonts'));
});

/*
* concatenates and minifies javascript files
*/
gulp.task('minify-js', ['bower'], function() {
    return gulp.src([
        './tmp/components/jquery/dist/jquery.js',
        './tmp/components/bootstrap/dist/js/bootstrap.js',
        './assets/js/javascript.js'
    ])
    .pipe(concat('site.js'))
    .pipe(gulp.dest('./tmp/js'))
    .pipe(minify({ext: ".min.js"}))
    .pipe(gulp.dest('./static/js'))
});

/*
* copies images into the static folder
*/
gulp.task('copy-images', function() {
    return gulp.src(['./assets/image/**/*']).pipe(gulp.dest('./static/image'));
});

/*
* cleans temporary files
*/
gulp.task('clean', ['concat-css', 'minify-js', 'copy-images', 'copy-fonts'], function() {
    return del([
        './tmp'
    ]);
});