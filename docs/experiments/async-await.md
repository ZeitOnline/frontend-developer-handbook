# Async Await

## Userstory
As a developer I'd like to use asynchronous functions within my javascript modules, to prevent unnecessary chaining of promises.

## What is async/await?
> An async function can contain an await expression, that pauses the execution of the function and waits for the passed Promise's resolution, and then resumes the async function's execution and returns the resolved value. You can think of a Promise in JavaScript as the equivalent of Java's Future or C# 's Task. [Source](https://blog.sessionstack.com/how-javascript-works-event-loop-and-the-rise-of-async-programming-5-ways-to-better-coding-with-2f077c4438b5?gi=92f3b9fc7172)

## But why though?
> Yes, you read that right. The V8 team made improvements that make async/await functions run faster than traditional promises in the JavaScript engine. 12.05.2019. [Source](https://itnext.io/javascripts-async-await-versus-promise-the-great-debate-6308cb2e10b3)

## Status Quo with the easyEmbeds as an example

```javascript=
posts.forEach( post => {
    [...]
    fetch( url )
        .then( ( response ) => {
            if ( !response.ok ) {
                throw new Error( 'Error requesting ' + url );
            }
            return response.json();
        })
        .then( ( data ) => {
            this.renderPost( data, params );
        })
        .catch( ( error ) => {
            zeit.log( 'social embed: ', error );
        });
});
```

## Code using async/await
```javascript=
posts.forEach( async post => {
    [...]
    try {
        const response = await( fetch( url ) );
        if (!response.ok) {
          throw new Error( `Error requesting ${url}` );
        }
        const json = await( response ).json();
        this.renderPost( json, params );
    } catch ( error ) {
        zeit.log( 'social embed: ', error );
    }
});
```

## Result
- Babel ensures automatically, that the code is compatible with all defined browsers.
- Filesize **before**: ~ 3KB
- Filesize **after**: ~ 10KB

## Todo:
- Check if there are any polyfills available
  - Size?
- What is babels default behaviour when async/await is used in multiple modules?
  - Where is babels additional code inserted?
