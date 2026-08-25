# Vector

Vector is a linear data structure that is implemented based on arrays. When the memory of a vector is used up, a larger contiguous memory area is automatically allocated, all the elements are copied to the new memory area, and the current memory area is reclaimed. Vector can be used to efficiently access elements. Both Vector and [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md) are implemented based on arrays, but Vector provides more interfaces for operating the arrays. Both of them can dynamically adjust the capacity. Vector doubles the capacity each time, whereas ArrayList increases the capacity by 50%. **Recommended use case**: Use Vector when the data volume is large. This topic uses the following to identify the use of generics:  
- T: Type

> **NOTE：**&gt;
> - The APIs provided by this module are deprecated since API version 9. You are advised to use
> [@ohos.util.ArrayList](arkts-arkts-util-arraylist-arraylist-c.md).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { Vector } from 'kits/@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

returns an ES6 iterator.Each item of the iterator is a Javascript Object

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-default/arkts-apis/arkts-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

## add

```TypeScript
add(element: T): boolean
```

Adds an element at the end of this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## clear

```TypeScript
clear(): void
```

Clears all elements in this Vector and sets its length to **0**.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

## clone

```TypeScript
clone(): Vector<T>
```

Clones this Vector and returns a copy. The modification to the copy does not affect the original instance.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Vector](arkts-arkts-util-vector-vector-c.md)&lt;T&gt; |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **Vector** instance.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

## convertToArray

```TypeScript
convertToArray(): Array<T>
```

Converts this Vector into an array.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;T & gt; |

## copyToArray

```TypeScript
copyToArray(array: Array<T>): void
```

Copies elements in this Vector into an array to overwrite elements of the same position indexes.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | Array & lt;T & gt; | Yes |

## forEach

```TypeScript
forEach(callbackFn: (value: T, index?: number, vector?: Vector<T>) => void, thisArg?: Object): void
```

Uses a callback to traverse the elements in this Vector and obtain their position indexes.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, vector?: Vector & lt;T & gt;) = & gt; void | Yes |
| thisArg | Object | No |

## get

```TypeScript
get(index: number): T
```

Obtains an element at the specified position in this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

## getCapacity

```TypeScript
getCapacity(): number
```

Obtains the capacity of this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getFirstElement

```TypeScript
getFirstElement(): T
```

Obtains the first element in this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

## getIndexFrom

```TypeScript
getIndexFrom(element: T, index: number): number
```

Searches for an element forward from the specified position index and returns the position index of the element.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getIndexOf

```TypeScript
getIndexOf(element: T): number
```

Obtains the index of the first occurrence of the specified element in this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLastElement

```TypeScript
getLastElement(): T
```

Obtains the last element in this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

## getLastIndexFrom

```TypeScript
getLastIndexFrom(element: T, index: number): number
```

Searches for an element backward from the specified position index and returns the position index of the element.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## getLastIndexOf

```TypeScript
getLastIndexOf(element: T): number
```

Obtains the index of the last occurrence of the specified element in this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |

## has

```TypeScript
has(element: T): boolean
```

Checks whether this Vector has the specified element.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## increaseCapacityTo

```TypeScript
increaseCapacityTo(newCapacity: number): void
```

Increases the capacity of this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newCapacity | number | Yes |

## insert

```TypeScript
insert(element: T, index: number): void
```

Inserts an element within the length range and moves its subsequent elements rightwards.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |
| index | number | Yes |

## isEmpty

```TypeScript
isEmpty(): boolean
```

Checks whether this Vector is empty (contains no elements).

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## remove

```TypeScript
remove(element: T): boolean
```

Removes the first occurrence of the specified element from this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## removeByIndex

```TypeScript
removeByIndex(index: number): T
```

Searches for an element based on its index, removes the element after returning it, and moves its subsequent elements leftwards.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

## removeByRange

```TypeScript
removeByRange(fromIndex: number, toIndex: number): void
```

Removes from this Vector all of the elements within a range, including the element at the start position but not that at the end position.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fromIndex | number | Yes |
| toIndex | number | Yes |

## replaceAllElements

```TypeScript
replaceAllElements(callbackFn: (value: T, index?: number, vector?: Vector<T>) => T, thisArg?: Object): void
```

Replaces all elements in this Vector with new elements, and returns the new ones.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, index?: number, vector?: Vector & lt;T & gt;) = & gt; T | Yes |
| thisArg | Object | No |

## set

```TypeScript
set(index: number, element: T): T
```

Replaces an element at the specified position in this Vector with a given element.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |
| element | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

## setLength

```TypeScript
setLength(newSize: number): void
```

Sets a new length for this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newSize | number | Yes |

## sort

```TypeScript
sort(comparator?: (firstValue: T, secondValue: T) => number): void
```

Sorts elements in this Vector.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| comparator | (firstValue: T, secondValue: T) = & gt; number | No |

## subVector

```TypeScript
subVector(fromIndex: number, toIndex: number): Vector<T>
```

Obtains elements within a range in this Vector, including the element at the start position but not that at the end position, and returns these elements as a new **Vector** instance.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fromIndex | number | Yes |
| toIndex | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Vector](arkts-arkts-util-vector-vector-c.md)&lt;T&gt; |

## toString

```TypeScript
toString(): string
```

Uses commas (,) to concatenate elements in this Vector into a string.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## trimToCurrentLength

```TypeScript
trimToCurrentLength(): void
```

Trims the capacity of this Vector into its current length.

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang

## length

```TypeScript
length: number
```

Number of elements in a Vector.

**Type:** number

**Since:** 8

**Deprecated since:** 9

**System capability:** SystemCapability.Utils.Lang
