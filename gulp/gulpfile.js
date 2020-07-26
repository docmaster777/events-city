var gulp = require('gulp');
var less = require('gulp-less');
var autoprefix = require('gulp-autoprefixer');

// gulp.task('styles', function () {
//     return gulp.src('less/**/*.less')
//         .pipe(less())
//         .pipe(autoprefix('last 10 version'))
//         .pipe(gulp.dest('./'))
// });

//Таск на стили CSS
function styles() {
   return gulp.src('less/**/*.less')
   .pipe(autoprefix('last 10 version'))
   .pipe(less())
   .pipe(gulp.dest('./../src/static/css/'))
}

function build(){
    gulp.watch('less/**/*.less', styles)
}

gulp.task('default', build)


