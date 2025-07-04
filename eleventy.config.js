import fs from "fs";

import { DateTime } from "luxon";

import { feedPlugin } from "@11ty/eleventy-plugin-rss";
import eleventyNavigationPlugin from "@11ty/eleventy-navigation";
import  DateGitLastUpdated  from "./node_modules/@11ty/eleventy/src/Util/DateGitLastUpdated.js"

export default async function(eleventyConfig) {

    eleventyConfig.addPassthroughCopy("img");
    eleventyConfig.addPassthroughCopy("css");
    eleventyConfig.addPassthroughCopy("js");


    //Plugin addition/configuration
        eleventyConfig.addPlugin(eleventyNavigationPlugin);
        eleventyConfig.addPlugin(feedPlugin,{
            collection: {
                name: "posts"
            }
        });

  //Adding filters
      function filterTagList(tags) {
        return (tags || []).filter(tag => ["all", "nav", "post", "posts"].indexOf(tag) === -1);
    }

    eleventyConfig.addFilter("filterTagList", filterTagList)

  
eleventyConfig.addFilter("isArabic", function(path){
    return path.includes("ar/");
})

    eleventyConfig.addFilter("readableDate", (dateObj, lang = 'en') => {
        return lang === 'en' ? DateTime.fromJSDate(dateObj, { zone: 'utc' }).toFormat("dd LLL yyyy") : new Intl.DateTimeFormat(lang).format(DateTime.fromJSDate(dateObj, { zone: 'utc' }))
    });

    // https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-date-string
    eleventyConfig.addFilter('htmlDateString', (dateObj) => {
        return DateTime.fromJSDate(dateObj, { zone: 'utc' }).toFormat('yyyy-LL-dd');
    });

    eleventyConfig.addFilter('underscoreToHypen', function(path){
        return path.replaceAll("_","-")
    })

    eleventyConfig.addAsyncFilter('getFileLastMoified',  async function(path){
          const  lastMod = await  DateGitLastUpdated(path);
          return (lastMod? lastMod : new Date());

        /*const stats  = fs.statSync(path);
             return new Date(stats.mtime)
    */
    })


 eleventyConfig.setServerOptions({
    
        port: 8080,
        open: false,
        notify: false,
        ui: false,
        ghostMode: false,
        showAllHosts: true
        
    
        // Opt-out of the DevServer snippet
        // snippet: false,
      })

    return {
                templateFormats: [
            "md",
            "njk",
            "html",
            "liquid"
        ],

        // Pre-process *.md files with: (default: `liquid`)
        markdownTemplateEngine: "njk",

        // Pre-process *.html files with: (default: `liquid`)
        htmlTemplateEngine: "njk",

        // -----------------------------------------------------------------
        // If your site deploys to a subdirectory, change `pathPrefix`.
        // Don’t worry about leading and trailing slashes, we normalize these.

        // If you don’t have a subdirectory, use "" or "/" (they do the same thing)
        // This is only used for link URLs (it does not affect your file structure)
        // Best paired with the `url` filter: https://www.11ty.dev/docs/filters/url/

        // You can also pass this in on the command line using `--pathprefix`

        // Optional (default is shown)
        pathPrefix: "/",

    // Configure Eleventy
        dir: {
            input: ".",
            includes: "_includes",
            data: "_data",
            output: "_site"
        }
    }
};
