
var gulp = require('gulp');
var del = require('del');
var shell = require('gulp-shell');
var livereload = require('gulp-livereload');
var watch = require('gulp-watch');
var sass = require('gulp-sass');
var minifycss = require('gulp-minify-css');
var postcss = require('gulp-postcss');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('autoprefixer');

// Browsers to target when prefixing CSS.
var COMPATIBILITY = ['last 2 versions', 'ie >= 9'];

// File paths to various assets are defined here.
var PATHS = {
  templates: [
      'apps/administrator/main/templates/**/*',
      'apps/website/templates/**/*',
      'templates/**/*',
  ],
  sass_admin: {
    targets: [
      'apps/administrator/main/static/main/sass/**/*'
    ],
    source: 'apps/administrator/main/static/main/sass/*.scss',
    dest: 'apps/administrator/main/static/main/'
  },
  sass_website: {
    targets: [
      'apps/website/static/website/sass/**/*'
    ],
    source: 'apps/website/static/website/sass/*.scss',
    dest: 'apps/website/static/website/'
  },
  prod_css_admin: 'apps/administrator/main/static/main/',
  prod_css_website:'apps/website/static/website/'
};

//DJANGO TASK
// Django Runserver
gulp.task('server',
    shell.task(['python manage.py runserver'])
);

// Django Migrate
gulp.task('migrate',
    shell.task(['python manage.py migrate'])
);

// Django collectstatic
gulp.task('collect',
    shell.task(['python manage.py collectstatic --noinput -i sass -i main.css.map'])
);

// Django create default superuser
gulp.task('superuser',
    shell.task(['python manage.py createsuperuser --email vinibiso@gmail.com --username admin'], {interactive:true})
);

// Clean Static
gulp.task('clean', function() {
    return del([
        'static/**/*',
    ]);
});

// CSS TASKS //

function makeAutoprefixer(path) {
  return gulp.src(path+'main.css')
    .pipe(sourcemaps.init())
    .pipe(postcss([ autoprefixer({ browsers: COMPATIBILITY }) ]))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(path));
}

function make_autoprefixer_admin() {
  return makeAutoprefixer(PATHS.prod_css_admin);
}

function make_autoprefixer_site() {
  return makeAutoprefixer(PATHS.prod_css_website);
}

// Autoprefixer Website
gulp.task('autoprefixer-admin', function () {
  return make_autoprefixer_admin();
});

// Autoprefixer Website
gulp.task('autoprefixer-site', function () {
  return make_autoprefixer_site();
});

// Calling Autoprefixer
gulp.task('autoprefixer', ['autoprefixer-site','autoprefixer-admin']);

// SAAS TASKS
gulp.task('sass-watch',function() {
  gulp.watch(PATHS.sass_admin.targets).on('change', function() {
      return gulp.src(PATHS.sass_admin.source)
          .pipe(sass())
          .pipe(gulp.dest(PATHS.sass_admin.dest))
          .pipe(minifycss())
          .pipe(gulp.dest(PATHS.sass_admin.dest))
          .pipe(livereload());
  });
  gulp.watch(PATHS.sass_website.targets).on('change', function() {
      return gulp.src(PATHS.sass_website.source)
          .pipe(sass())
          .pipe(gulp.dest(PATHS.sass_website.dest))
          .pipe(minifycss())
          .pipe(gulp.dest(PATHS.sass_website.dest))
          .pipe(livereload());
  });
});

// GENERIC TASKS
//Live reload
gulp.task('live-reload',function() {
  livereload.listen();
  gulp.watch(PATHS.templates).on('change', livereload.changed);
});

// Clean Static Dir and Collect after to refresh deploy
gulp.task('deploy', ['autoprefixer','clean','collect']);

// Set default taks to gulp server
gulp.task('default', ['server', 'live-reload', 'sass-watch'], function() {});
