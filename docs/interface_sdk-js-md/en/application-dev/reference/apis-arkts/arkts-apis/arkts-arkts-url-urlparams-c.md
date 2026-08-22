# URLParams

The URLParams interface defines some practical methods to process URL query strings.

**Since:** 23

<!--Device-url-class URLParams--><!--Device-url-class URLParams-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { url } from '@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[string, string]>
```

Obtains an ES6 iterator. Each item of the iterator is a JavaScript array, and the first and second fields ofeach array are the key and value respectively.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URLParams-$_iterator(): IterableIterator<[string, string]>--><!--Device-URLParams-$_iterator(): IterableIterator<[string, string]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[string, string]&gt; | Returns an ES6 iterator. Each item of the iterator is a JavaScript Array. The first item of Array is name, and the second item of Array is value. |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[string, string]>
```

Obtains an ES6 iterator. Each item of the iterator is a JavaScript array, and the first and second fields ofeach array are the key and value respectively.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-[Symbol.iterator](): IterableIterator<[string, string]>--><!--Device-URLParams-[Symbol.iterator](): IterableIterator<[string, string]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[string, string]&gt; | Returns an ES6 iterator. Each item of the iterator is a JavaScript Array. The first item of Array is name, and the second item of Array is value. |

**Examples**

```TypeScript
const paramsObject = new url.URLParams('fod=bay&edg=bap');
let iter = paramsObject[Symbol.iterator]();
for (let pair of iter) {
  console.info(pair[0] + ', ' + pair[1]);
}
// fod, bay
// edg, bap
```

```TypeScript
const paramsObject = new url.URLSearchParams('fod=bay&edg=bap');
let pairs = paramsObject[Symbol.iterator]();
for (let pair of pairs) {
  console.info(pair[0] + ', ' + pair[1]);
}
// fod, bay
// edg, bap
```

## append

```TypeScript
append(name: string, value: string): void
```

Appends a key-value pair into the query string.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-append(name: string, value: string): void--><!--Device-URLParams-append(name: string, value: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Key of the key-value pair to append. |
| value | string | Yes | Value of the key-value pair to append. |

**Examples**

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.append('fod', '3');
```

```TypeScript
let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
paramsObject.append('fod', '3');
```

## constructor

```TypeScript
constructor(init?: string[][] | Record<string, string> | string | URLParams)
```

A constructor used to create a URLParams instance.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-constructor(init?: string[][] | Record<string, string> | string | URLParams)--><!--Device-URLParams-constructor(init?: string[][] | Record<string, string> | string | URLParams)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| init | string[][] \| Record&lt;string, string&gt; \| string \| [URLParams](arkts-arkts-url-urlparams-c.md) | No | Input parameter objects, which include the following: - string[][]: two-dimensional string array. - Record&lt;string, string&gt;: list of objects. - string: string. - URLParams: object. The default value is null. |

**Examples**

```TypeScript
// Construct a URLParams object in string[][] mode.
let objectParams = new url.URLParams([ ['user1', 'abc1'], ['query2', 'first2'], ['query3', 'second3'] ]);
// Construct a URLParams object in Record<string, string> mode.
let objectParams1 = new url.URLParams({"fod" : '1' , "bard" : '2'});
// Construct a URLParams object in string mode.
let objectParams2 = new url.URLParams('?fod=1&bard=2');
// Construct a URLParams object using the search property of the url object.
let urlObject = url.URL.parseURL('https://developer.mozilla.org/?fod=1&bard=2');
let objectParams3 = new url.URLParams(urlObject.search);
// Construct a URLParams object using the params property of the url object.
let urlObject1 = url.URL.parseURL('https://developer.mozilla.org/?fod=1&bard=2');
let objectParams4 = urlObject1.params;
```

```TypeScript
let mm = 'https://username:password@host:8080';
let a = new url.URL("/", mm); // Output 'https://username:password@host:8080/';
let b = new url.URL(mm); // Output 'https://username:password@host:8080/';
new url.URL('path/path1', b); // Output 'https://username:password@host:8080/path/path1';
let c = new url.URL('/path/path1', b);  // Output 'https://username:password@host:8080/path/path1'; 
new url.URL('/path/path1', c); // Output 'https://username:password@host:8080/path/path1';
new url.URL('/path/path1', a); // Output 'https://username:password@host:8080/path/path1';
new url.URL('/path/path1', "https://www.exampleUrl/fr-FR/toot"); // Output https://www.exampleUrl/path/path1
new url.URL('/path/path1', ''); // Raises a TypeError exception as '' is not a valid URL
new url.URL('/path/path1'); // Raises a TypeError exception as '/path/path1' is not a valid URL
new url.URL('https://www.example.com', ); // Output https://www.example.com/
new url.URL('https://www.example.com', b); // Output https://www.example.com/
```

```TypeScript
let objectParams = new url.URLSearchParams([ ['user1', 'abc1'], ['query2', 'first2'], ['query3', 'second3'] ]);
let objectParams1 = new url.URLSearchParams({"fod" : '1' , "bard" : '2'});
let objectParams2 = new url.URLSearchParams('?fod=1&bard=2');
let urlObject = new url.URL('https://developer.mozilla.org/?fod=1&bard=2');
let params = new url.URLSearchParams(urlObject.search);
```

## constructor

```TypeScript
constructor(init?: [string, string][] | Record<string, string> | string | URLParams)
```

A parameterized constructor used to create an URLParams instance. As the input parameter of the constructor function, init supports four types. The input parameter is a character string two-dimensional array. The input parameter is the object list. The input parameter is a character string. The input parameter is the URLParams object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URLParams-constructor(init?: [string, string][] | Record<string, string> | string | URLParams)--><!--Device-URLParams-constructor(init?: [string, string][] | Record<string, string> | string | URLParams)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| init | [string, string][] \| Record&lt;string, string&gt; \| string \| [URLParams](arkts-arkts-url-urlparams-c.md) | No | init init |

**Examples**

See [constructor](#constructor)

## delete

```TypeScript
delete(name: string): void
```

Deletes key-value pairs of the specified key.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-delete(name: string): void--><!--Device-URLParams-delete(name: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Key of the key-value pairs to delete. |

**Examples**

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.delete('fod');
```

```TypeScript
let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
paramsObject.delete('fod');
```

## entries

```TypeScript
entries(): IterableIterator<[string, string]>
```

Obtains an ES6 iterator. Each item of the iterator is a JavaScript array, and the first and second fields of each array are the key and value respectively.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-entries(): IterableIterator<[string, string]>--><!--Device-URLParams-entries(): IterableIterator<[string, string]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;[string, string]&gt; | Returns an iterator for ES6. |

**Examples**

```TypeScript
let paramsObject = new url.URLParams("keyName1=valueName1&keyName2=valueName2");
let pair = paramsObject.entries();
for (let item of pair) {
    console.info(item[0] + '=' + item[1]);
}
// keyName1=valueName1
// keyName2=valueName2
```

```TypeScript
let searchParamsObject = new url.URLSearchParams("keyName1=valueName1&keyName2=valueName2");
let iter = searchParamsObject.entries();
for (let pair of iter) {
  console.info(pair[0]+ ', '+ pair[1]);
}
// keyName1, valueName1
// keyName2, valueName2
```

## forEach

```TypeScript
forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void
```

Callback functions are used to traverse key-value pairs on the URLParams instance object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void--><!--Device-URLParams-forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value: string, key: string, searchParams: URLParams) =&gt; void | Yes | callbackFn value Current traversal key value, key Indicates the name of the key that is traversed. |
| thisArg | Object | No | thisArg to be used as this value for when callbackFn is called |

**Examples**

```TypeScript
const myURLObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
myURLObject.params.forEach((value, name, searchParams) => {
    console.info(name, value, myURLObject.params === searchParams);
});
```

```TypeScript
const myURLObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
myURLObject.searchParams.forEach((value, name, searchParams) => {
    console.info(name, value, myURLObject.searchParams === searchParams);
});
```

## forEach

```TypeScript
forEach(callbackFn: UrlCbFn): void
```

Iterates over a collection (e.g., URLs) and executes a callback function for each element.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URLParams-forEach(callbackFn: UrlCbFn): void--><!--Device-URLParams-forEach(callbackFn: UrlCbFn): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [UrlCbFn](arkts-arkts-url-urlcbfn-t.md) | Yes | A callback function to execute for each element. |

**Examples**

See [forEach](#foreach)

## get

```TypeScript
get(name: string): string | null
```

Obtains the value of the first key-value pair based on the specified key.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-get(name: string): string | null--><!--Device-URLParams-get(name: string): string | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Key specified to obtain the value. |

**Return value:**

| Type | Description |
| --- | --- |
| string \| null | Returns the first value found by name. If no value is found, null is returned. |

**Examples**

```TypeScript
let paramsObject = new url.URLParams('name=Jonathan&age=18');
let name = paramsObject.get("name"); // is the string "Jonathan"
let age = paramsObject.get("age"); // is the string "18"
let getObj = paramsObject.get("abc"); // undefined
```

```TypeScript
let paramsObject = new url.URLSearchParams('name=Jonathan&age=18');
let name = paramsObject.get("name"); // is the string "Jonathan"
let age = paramsObject.get("age"); // is the string '18'
let getObj = paramsObject.get("abc"); // undefined
```

## get

```TypeScript
get(name: string): string | undefined
```

Obtains the value of the first key-value pair based on the specified key.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URLParams-get(name: string): string | undefined--><!--Device-URLParams-get(name: string): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Key specified to obtain the value. |

**Return value:**

| Type | Description |
| --- | --- |
| string \| undefined | Returns the first value found by name. If no value is found, undefined is returned. |

**Examples**

See [get](#get)

## getAll

```TypeScript
getAll(name: string): string[]
```

Obtains all the values based on the specified key.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-getAll(name: string): string[]--><!--Device-URLParams-getAll(name: string): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Target key. |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | string[] Returns all key-value pairs with the specified name. |

**Examples**

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLParams(urlObject.search.slice(1));
params.append('fod', '3'); // Add a second value for the fod parameter.
console.info(params.getAll('fod').toString()) // Output ["1","3"].
```

```TypeScript
let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLSearchParams(urlObject.search.slice(1));
params.append('fod', '3'); // Add a second value for the fod parameter.
console.info(params.getAll('fod').toString()) // Output ["1","3"].
```

## has

```TypeScript
has(name: string): boolean
```

Checks whether a key has a value.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-has(name: string): boolean--><!--Device-URLParams-has(name: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Key specified to search for its value. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns a Boolean value that indicates whether a found |

**Examples**

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
let result = paramsObject.has('bard');
```

```TypeScript
let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
paramsObject.has('bard') === true;
```

## keys

```TypeScript
keys(): IterableIterator<string>
```

Obtains an ES6 iterator that contains the keys of all the key-value pairs.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-keys(): IterableIterator<string>--><!--Device-URLParams-keys(): IterableIterator<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;string&gt; | Returns an ES6 Iterator over the names of each name-value pair. |

**Examples**

```TypeScript
let paramsObject = new url.URLParams("key1=value1&key2=value2");
let keys = paramsObject.keys();
for (let key of keys) {
  console.info(key);
}
// key1
// key2
```

```TypeScript
let searchParamsObject = new url.URLSearchParams("key1=value1&key2=value2");
let keys = searchParamsObject.keys();
for (let key of keys) {
  console.info(key);
}
// key1
// key2
```

## set

```TypeScript
set(name: string, value: string): void
```

Sets the value for a key. If key-value pairs matching the specified key exist, the value of the first key- value pair will be set to the specified value and other key-value pairs will be deleted. Otherwise, the key-value pair will be appended to the query string.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-set(name: string, value: string): void--><!--Device-URLParams-set(name: string, value: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Key of the value to set. |
| value | string | Yes | Value to set. |

**Examples**

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.set('baz', '3'); // Add a third parameter.
```

```TypeScript
let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLSearchParams(urlObject.search.slice(1));
paramsObject.set('baz', '3'); // Add a third parameter.
```

## sort

```TypeScript
sort(): void
```

Sorts all key-value pairs contained in this object based on the Unicode code points of the keys and returns undefined. This method uses a stable sorting algorithm, that is, the relative order between key-value pairs with equal keys is retained.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-sort(): void--><!--Device-URLParams-sort(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Examples**

```TypeScript
let paramsObject = new url.URLParams("c=3&a=9&b=4&d=2"); // Create a test URLParams object
paramsObject.sort(); // Sort the key/value pairs
console.info(paramsObject.toString()); // Display the sorted query string // Output a=9&b=4&c=3&d=2
```

```TypeScript
let searchParamsObject = new url.URLSearchParams("c=3&a=9&b=4&d=2"); // Create a test URLSearchParams object
searchParamsObject.sort(); // Sort the key/value pairs
console.info(searchParamsObject.toString()); // Display the sorted query string // Output a=9&b=4&c=3&d=2
```

## toString

```TypeScript
toString(): string
```

Obtains search parameters that are serialized as a string and, if necessary, percent-encodes the characters in the string.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-toString(): string--><!--Device-URLParams-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns a search parameter serialized as a string, percent-encoded if necessary. |

**Examples**

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLParams(urlObject.search.slice(1));
params.append('fod', '3');
console.info(params.toString()); // Output 'fod=1&bard=2&fod=3'
```

```TypeScript
const urlObject = url.URL.parseURL('https://username:password@host:8080/directory/file?query=pppppp#qwer=da');
let result = urlObject.toString(); // Output 'https://username:password@host:8080/directory/file?query=pppppp#qwer=da'
```

```TypeScript
let urlObject = new url.URL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLSearchParams(urlObject.search.slice(1));
params.append('fod', '3');
console.info(params.toString()); // Output 'fod=1&bard=2&fod=3'
```

## values

```TypeScript
values(): IterableIterator<string>
```

Obtains an ES6 iterator that contains the values of all the key-value pairs.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-values(): IterableIterator<string>--><!--Device-URLParams-values(): IterableIterator<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| IterableIterator&lt;string&gt; | Returns an ES6 Iterator over the values of each name-value pair. |

**Examples**

```TypeScript
let paramsObject = new url.URLParams("key1=value1&key2=value2");
let values = paramsObject.values();
for (let value of values) {
  console.info(value);
}
// value1
// value2
```

```TypeScript
let searchParams = new url.URLSearchParams("key1=value1&key2=value2");
let values = searchParams.values();
for (let value of values) {
  console.info(value);
}
// value1
// value2
```

