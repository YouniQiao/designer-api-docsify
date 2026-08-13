# Set

A non-linear data structure. > **NOTE：**> > - This module can be imported only to ArkTS files (with the file name extension .ets). > This section uses the following to identify the use of generics: - T: type, which can be any of the [sendable data types](../../../arkts-utils/arkts-sendable.md#sendable-data-types). **Decorator**: \@Sendable

**Since:** 12

**Deprecated since:** -1

<!--Device-collections-class Set--><!--Device-collections-class Set-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { collections } from '@kit.ArkTS';
```

## [Symbol.iterator]

```TypeScript
[Symbol.iterator](): IterableIterator<T>
```

Returns an iterator, each item of which is a JavaScript object. NOTE: This API cannot be used in .ets files.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-[Symbol.iterator](): IterableIterator<T>--><!--Device-Set-[Symbol.iterator](): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |

## add

```TypeScript
add(value: T): Set<T>
```

Checks whether a value exists in this ArkTS set, and if not, adds the value to the set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-add(value: T): Set<T>--><!--Device-Set-add(value: T): Set<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Set & lt;T & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## clear

```TypeScript
clear(): void
```

Removes all elements from this ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-clear(): void--><!--Device-Set-clear(): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## constructor

```TypeScript
constructor(values?: readonly T[] | null)
```

A constructor used to create an ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-constructor(values?: readonly T[] | null)--><!--Device-Set-constructor(values?: readonly T[] | null)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [values](#values) | readonly T[] \| null | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## constructor

```TypeScript
constructor(iterable: Iterable<T>)
```

A constructor used to create an ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-constructor(iterable: Iterable<T>)--><!--Device-Set-constructor(iterable: Iterable<T>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| iterable | Iterable & lt;T & gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200012](../errorcode-utils.md#10200012-constructor-calling-failure) |

## delete

```TypeScript
delete(value: T): boolean
```

Deletes an element from this ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-delete(value: T): boolean--><!--Device-Set-delete(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## entries

```TypeScript
entries(): IterableIterator<[T, T]>
```

Returns a set iterator object that contains the key-value pair of each element in this ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-entries(): IterableIterator<[T, T]>--><!--Device-Set-entries(): IterableIterator<[T, T]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;[T, T]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## forEach

```TypeScript
forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void
```

Calls a callback function for each key-value pair in this ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void--><!--Device-Set-forEach(callbackFn: (value: T, value2: T, set: Set<T>) => void): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callbackFn | (value: T, value2: T, set: Set & lt;T & gt;) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## has

```TypeScript
has(value: T): boolean
```

Checks whether a value exists in this ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-has(value: T): boolean--><!--Device-Set-has(value: T): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## keys

```TypeScript
keys(): IterableIterator<T>
```

Returns a set iterator object that contains the key of each element in this ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-keys(): IterableIterator<T>--><!--Device-Set-keys(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## values

```TypeScript
values(): IterableIterator<T>
```

Returns a set iterator object that contains the value of each element in this ArkTS set.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-values(): IterableIterator<T>--><!--Device-Set-values(): IterableIterator<T>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [IterableIterator](../../apis-na/arkts-apis/arkts-na-lib-es2015-iterable-iterableiterator-i.md)&lt;T&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10200011](../errorcode-utils.md#10200011-passed-thisobject-is-not-an-instance-of-the-containers-class) |
| [10200201](../errorcode-utils.md#10200201-concurrent-modification-error) |

## size

```TypeScript
readonly size: number
```

Number of elements in a set.

**Type:** number

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Set-readonly size: number--><!--Device-Set-readonly size: number-End-->

**System capability:** SystemCapability.Utils.Lang
