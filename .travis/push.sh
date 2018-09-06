
setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_files() {
  git add linux/*.*
  git add macOS/*.*
  git add windows/*.*
  git add README.md
  git commit --message "[ci skip] Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote remove origin
  git remote add origin https://${GH_TOKEN}@github.com/hackesta/atom-icons.git
  git push --quiet origin HEAD:master > /dev/null 2>&1
}

setup_git
commit_files
upload_files
