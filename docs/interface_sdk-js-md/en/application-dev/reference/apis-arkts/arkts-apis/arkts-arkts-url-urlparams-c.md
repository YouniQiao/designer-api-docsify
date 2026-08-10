# URLParams

URLParams是一个用于解析、构造和操作URL参数的实用类。该类提供了统一的接口来处理URL查询参数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-url-class URLParams--><!--Device-url-class URLParams-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { url } from 'kits/@kit.ArkTS';
```

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[string, string]>
```

返回一个ES6的迭代器，迭代器的每一项都是一个JavaScript Array。Array的第一项是name，Array的第二项是value。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URLParams-$_iterator(): IterableIterator<[string, string]>--><!--Device-URLParams-$_iterator(): IterableIterator<[string, string]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[string, string]&gt; | 返回一个ES6的迭代器。 |

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[string, string]>
```

获取一个ES6迭代器。迭代器的每一项都是一个JavaScript数组，数组的第一项和第二项分别是键和值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-[Symbol.iterator](): IterableIterator<[string, string]>--><!--Device-URLParams-[Symbol.iterator](): IterableIterator<[string, string]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[string, string]&gt; | 返回一个ES6迭代器。迭代器的每一项都是一个JavaScript Array。 Array的第一项是name，第二项是value。 |

## Examples

```TypeScript
const paramsObject = new url.URLParams('fod=bay&edg=bap');
let iter = paramsObject[Symbol.iterator]();
for (let pair of iter) {
  console.info(pair[0] + ', ' + pair[1]);
}
// fod, bay
// edg, bap
```

## append

```TypeScript
append(name: string, value: string): void
```

将新的键值对插入到查询字符串。与[set](arkts-arkts-url-urlparams-c.md#set)方法不同，append不会替换已存在的键名对应的值，而是追加一个新的键值对，允许同一键名存在多个值。如需替换已有键值，请使用set方法。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-append(name: string, value: string): void--><!--Device-URLParams-append(name: string, value: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 需要插入搜索参数的键名。 |
| value | string | Yes | 需要插入搜索参数的值。 |

## Examples

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.append('fod', '3');
```

## constructor

```TypeScript
constructor(init?: string[][] | Record<string, string> | string | URLParams)
```

ArkTS-Sta: constructor(init?: [string, string][] | Record&lt;string, string&gt; | string | URLParams)

URLParams的构造函数，用于创建URL参数对象，适用于需要解析、构造或操作URL查询参数的场景。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-constructor(init?: string[][] | Record<string, string> | string | URLParams)--><!--Device-URLParams-constructor(init?: string[][] | Record<string, string> | string | URLParams)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| init | string[][] \| Record&lt;string, string&gt; \| string \| URLParams | No | 入参对象。 &lt;br/&gt;- string[][]：字符串二维数组。 &lt;br/&gt;- Record&lt;string, string&gt;：对象列表。 &lt;br/&gt;- string：URL查询参数字符串。 &lt;br/&gt;- URLParams：URLParams实例对象。 &lt;br/&gt;- 默认值：null。 |

## Examples

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

## constructor

```TypeScript
constructor(init?: [string, string][] | Record<string, string> | string | URLParams)
```

用于创建URLParams实例的参数化构造函数。作为构造函数的输入参数，init支持四种类型。输入参数是字符串二维数组。输入参数是对象列表。输入参数是字符串。输入参数是URLParams对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URLParams-constructor(init?: [string, string][] | Record<string, string> | string | URLParams)--><!--Device-URLParams-constructor(init?: [string, string][] | Record<string, string> | string | URLParams)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| init | [string, string][] \| Record&lt;string, string&gt; \| string \| URLParams | No | init init |

## delete

```TypeScript
delete(name: string): void
```

删除指定名称的所有键值对。如果指定名称不存在，则不做任何操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-delete(name: string): void--><!--Device-URLParams-delete(name: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 需要删除的键值名称。 |

## Examples

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.delete('fod');
```

## entries

```TypeScript
entries(): IterableIterator<[string, string]>
```

返回一个ES6的迭代器，迭代器的每一项都是一个Array。Array的第一项是name，Array的第二项是value。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-entries(): IterableIterator<[string, string]>--><!--Device-URLParams-entries(): IterableIterator<[string, string]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[string, string]&gt; | 返回一个ES6的迭代器。 |

## Examples

```TypeScript
let paramsObject = new url.URLParams("keyName1=valueName1&keyName2=valueName2");
let pair = paramsObject.entries();
for (let item of pair) {
    console.info(item[0] + '=' + item[1]);
}
// keyName1=valueName1
// keyName2=valueName2
```

## forEach

```TypeScript
forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void
```

通过回调函数来遍历URLParams实例对象上的键值对。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void--><!--Device-URLParams-forEach(callbackFn: (value: string, key: string, searchParams: URLParams) => void, thisArg?: Object): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | (value: string, key: string, searchParams: URLParams) =&gt; void | Yes | 回调函数。 |
| thisArg | Object | No | callbackFn被调用时用作this值，默认值是本对象。 |

## Examples

```TypeScript
const myURLObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
myURLObject.params.forEach((value, name, searchParams) => {
    console.info(name, value, myURLObject.params === searchParams);
});
```

## forEach

```TypeScript
forEach(callbackFn: UrlCbFn): void
```

通过回调函数来遍历URLSearchParams实例对象上的键值对。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URLParams-forEach(callbackFn: UrlCbFn): void--><!--Device-URLParams-forEach(callbackFn: UrlCbFn): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackFn | [UrlCbFn](arkts-arkts-url-urlcbfn-t.md) | Yes | 回调函数。 |

## get

```TypeScript
get(name: string): string | null
```

获取指定名称对应的第一个值。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-get(name: string): string | null--><!--Device-URLParams-get(name: string): string | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 指定键值对的名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回第一个值，如果没找到，返回 null。 |

## Examples

```TypeScript
let paramsObject = new url.URLParams('name=Jonathan&age=18');
let name = paramsObject.get("name"); // is the string "Jonathan"
let age = paramsObject.get("age"); // is the string "18"
let getObj = paramsObject.get("abc"); // undefined
```

## get

```TypeScript
get(name: string): string | undefined
```

根据指定的键获取第一个键值对的值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-URLParams-get(name: string): string | undefined--><!--Device-URLParams-get(name: string): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 指定用于获取值的键。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回按名称找到的第一个值。 如果未找到值，则返回undefined。 |

## getAll

```TypeScript
getAll(name: string): string[]
```

获取指定名称的所有键对应值的集合。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-getAll(name: string): string[]--><!--Device-URLParams-getAll(name: string): string[]-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 指定的键值名称。 |

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 返回指定名称的所有键对应值的集合。 |

## Examples

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLParams(urlObject.search.slice(1));
params.append('fod', '3'); // Add a second value for the fod parameter.
console.info(params.getAll('fod').toString()) // Output ["1","3"].
```

## has

```TypeScript
has(name: string): boolean
```

判断一个指定的键名对应的值是否存在。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-has(name: string): boolean--><!--Device-URLParams-has(name: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 要查找的参数的键名。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否存在相对应的key值，存在返回true，否则返回false。 |

## Examples

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
let result = paramsObject.has('bard');
```

## keys

```TypeScript
keys(): IterableIterator<string>
```

返回一个包含所有键值对的name的ES6迭代器。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-keys(): IterableIterator<string>--><!--Device-URLParams-keys(): IterableIterator<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;string&gt; | 返回一个包含所有键值对的name的ES6迭代器。 |

## Examples

```TypeScript
let paramsObject = new url.URLParams("key1=value1&key2=value2");
let keys = paramsObject.keys();
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

将与name关联的URLSearchParams对象中的值设置为value。

如果存在名称为name的键值对，请将第一个键值对的值设置为value并删除所有其他值。如果不是，则将键值对附加到查询字符串。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-set(name: string, value: string): void--><!--Device-URLParams-set(name: string, value: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 将要设置的参数的键值名。 |
| value | string | Yes | 所要设置的参数值。 |

## Examples

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let paramsObject = new url.URLParams(urlObject.search.slice(1));
paramsObject.set('baz', '3'); // Add a third parameter.
```

## sort

```TypeScript
sort(): void
```

对包含在此对象中的所有键值对进行排序。排序顺序是根据键的Unicode代码点。该方法使用稳定的排序算法（保留具有相等键的键值对之间的相对顺序）。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-sort(): void--><!--Device-URLParams-sort(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
let paramsObject = new url.URLParams("c=3&a=9&b=4&d=2"); // Create a test URLParams object
paramsObject.sort(); // Sort the key/value pairs
console.info(paramsObject.toString()); // Display the sorted query string // Output a=9&b=4&c=3&d=2
```

## toString

```TypeScript
toString(): string
```

返回序列化为字符串的搜索参数，必要时对字符进行百分比编码。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-toString(): string--><!--Device-URLParams-toString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回序列化为字符串的搜索参数，必要时对字符进行百分比编码。 |

## Examples

```TypeScript
let urlObject = url.URL.parseURL('https://developer.exampleUrl/?fod=1&bard=2');
let params = new url.URLParams(urlObject.search.slice(1));
params.append('fod', '3');
console.info(params.toString()); // Output 'fod=1&bard=2&fod=3'
```

## values

```TypeScript
values(): IterableIterator<string>
```

返回一个包含所有键值对的value的ES6迭代器。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-URLParams-values(): IterableIterator<string>--><!--Device-URLParams-values(): IterableIterator<string>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;string&gt; | 返回一个包含所有键值对的value的ES6迭代器。 |

## Examples

```TypeScript
let paramsObject = new url.URLParams("key1=value1&key2=value2");
let values = paramsObject.values();
for (let value of values) {
  console.info(value);
}
// value1
// value2
```

