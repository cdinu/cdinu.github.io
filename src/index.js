const fs = require('fs');
const path = require('path');
const marked = require('marked');
const handlebars = require('handlebars');

const defaults = {
  title: 'Cristian Dinu',
  description: 'Cristian Dinu\'s official page. Short bio and some of the latest noteworthy happenings',
  outputDir: path.join(__dirname, '..'),
  style: fs.readFileSync(path.join(__dirname, 'style.css')).toString(),
  baseUrl: 'https://cristiandinu.org',
}

layout = handlebars.compile(
  fs.readFileSync(
    path.join(__dirname, 'layout.hbs')
  ).toString()
);

const renderer = new marked.Renderer();

renderer.link = ( href = '', title, text ) => href.indexOf('http') === 0
  ? `<a target="_blank" href="${href}" title="open in new tab" rel="noopener">${text}</a>`
  : `<a href="${href}">${text}</a>`;


const build = () => {
  const pagesDir = path.join(__dirname, '..', 'pages');
  const pages = fs.readdirSync(pagesDir);
  pages.forEach(page => {
    const config = require(path.join(pagesDir, page, 'config.json'));

    const body = fs
      .readdirSync(path.join(pagesDir, page))
      .filter(fileName => fileName.match(/\.md$/i))
      .sort()
      .map(fileName => fs.readFileSync(path.join(pagesDir, page, fileName)).toString())
      .map(fileContents => marked(fileContents, { renderer }))
      .join('\n');

    const canonical = page == 'index' ? defaults.baseUrl : `${defaults.baseUrl}/${page}.html`
    const output = layout({ ...defaults, ...config, canonical, body });

    fs.writeFile(
      path.join(defaults.outputDir, `${page}.html`),
      output,
      ()=> console.log(`Generated ${page}.`)
    );
  });
}

console.log(`Using ${defaults.outputDir} to output your files`);
build();