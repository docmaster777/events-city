'use strict';

const gulp = require('gulp');
const less = require('gulp-less');
const LessAutoprefix = require('less-plugin-autoprefix');
const autoprefix = new LessAutoprefix({ browsers: ['last 2 versions'] });
 


function styles() {
    return gulp.src('less/**/*.less')
    .pipe(less({
      plugins: [autoprefix]
    }))
    .pipe(gulp.dest('./../src/static/css/'));
 }
 
 function build(){
     gulp.watch('less/**/*.less', styles)
 }
 
 gulp.task('default', build)