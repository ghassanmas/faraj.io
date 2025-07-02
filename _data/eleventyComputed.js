import metadataEn from "./metadata.json" with {type: "json"};
import metadataAr from "./metadataAr.json" with {type: "json"};
export default {
i18n: {
        pageAr: (data)=> data.page.url.replace('/en','/ar'),
        pageEn: (data)=> data.page.url.replace('/ar','/en')
    },
 metadata:{

 lang:(data) => (data.page.url.includes('/ar')? 'ar' : 'en'),
 title: (data) => (data.page.url.includes('/ar')? metadataAr.title : metadataEn.title)
}
 
}