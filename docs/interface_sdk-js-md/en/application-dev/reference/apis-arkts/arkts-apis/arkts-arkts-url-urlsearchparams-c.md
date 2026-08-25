# URLSearchParams

The URLSearchParams interface defines some practical methods to process URL query strings.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [URLParams](arkts-arkts-url-urlparams-c.md)

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { url } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<[string, string]>
```

Returns an iterator allowing to go through all key/value pairs contained in this object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** iterator]

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[string, string]&gt; |

## append

```TypeScript
append(name: string, value: string): void
```

Appends a specified key/value pair as a new search parameter.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** append

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | string | Yes |

## constructor

```TypeScript
constructor(init?: string[][] | Record<string, string> | string | URLSearchParams)
```

A parameterized constructor used to create an URLSearchParams instance. As the input parameter of the constructor function, init supports four types. The input parameter is a character string two-dimensional array. The input parameter is the object list. The input parameter is a character string. The input parameter is the URLSearchParams object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** constructor

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| init | string[][] \| Record & lt;string, string & gt; \ | string \| URLSearchParams | No |

## delete

```TypeScript
delete(name: string): void
```

Deletes the given search parameter and its associated value,from the list of all search parameters.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** delete

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

## entries

```TypeScript
entries(): IterableIterator<[string, string]>
```

Returns an ES6 iterator. Each item of the iterator is a JavaScript Array. The first item of Array is name, and the second item of Array is value.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** entries

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;[string, string]&gt; |

## forEach

```TypeScript
forEach(callbackFn: (value: string, key: string, searchParams: URLSearchParams) => void, thisArg?: Object): void
```

Callback functions are used to traverse key-value pairs on the URLSearchParams instance object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** forEach

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: string, key: string, searchParams: URLSearchParams) = & gt; void | Yes |
| thisArg | Object | No |

## get

```TypeScript
get(name: string): string | null
```

Returns the first value associated to the given search parameter.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** get

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string \| null |

## getAll

```TypeScript
getAll(name: string): string[]
```

Returns all key-value pairs associated with a given search parameter as an array.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** getAll

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string[] |

## has

```TypeScript
has(name: string): boolean
```

Returns a Boolean that indicates whether a parameter with the specified name exists.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** has

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## keys

```TypeScript
keys(): IterableIterator<string>
```

Returns an iterator allowing to go through all keys contained in this object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** keys

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;string&gt; |

## set

```TypeScript
set(name: string, value: string): void
```

Sets the value associated with a given search parameter to the given value. If there were several matching values, this method deletes the others. If the search parameter doesn't exist, this method creates it.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** set

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | string | Yes |

## sort

```TypeScript
sort(): void
```

Sort all key/value pairs contained in this object in place and return undefined.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** sort

**System capability:** SystemCapability.Utils.Lang

## toString

```TypeScript
toString(): string
```

Returns a query string suitable for use in a URL.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** toString

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## values

```TypeScript
values(): IterableIterator<string>
```

Returns an iterator allowing to go through all values contained in this object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** values

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;string&gt; |
