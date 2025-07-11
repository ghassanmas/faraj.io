export default {
  async fetch(request) {
// shall run for www.faraj.io
  // Now this worker handle both www and root and redirct accordingly doubled checked with below
  // curl https://www.faraj.io -L -I
  // Resolved by just assinging the same woreker to the www.faraj.io route

// After 100K requests (irrelavnt for now) cloudflare will not redirect;
// Todo: still need to do apprioate 404 page as default index.njk still serfved for all other urls
// Todo: automate the change to this file so that will be deployed `faraj-homepage-lang` worker in cloudfalre
// Todo: double check if this works well in other browsers or "Accept-Header" doesn't exist
 // Works correctly with curl https://faraj.io  -L -H "Accept-Language: ar"
// Todo: Relate to previous long term SEO strategy
// Todo: how much latecny does this worker add to response?
  // Google AI response search said 8milliesecond (so okay)
    try{
    const isArabic = request.headers.get('Accept-Language').startsWith('ar');
    const destinationURL = isArabic ? "https://faraj.io/ar/" : "https://faraj.io/en/";
    const statusCode = 301;
    return Response.redirect(destinationURL, statusCode);
    }
    catch {
      // For whatsover reason is there any error go En
      return Response.redirect("https://faraj.io/en/", 301);

    }
  },
};
