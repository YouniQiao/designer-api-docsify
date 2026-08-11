# BigInt64ArrayConstructor

## [[Construct]]

```TypeScript
new(length?: number): BigInt64Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |

## [[Construct]]

```TypeScript
new(array: Iterable<bigint>): BigInt64Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | Iterable&lt;bigint&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |

## [[Construct]]

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): BigInt64Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | [ArrayBufferLike](../../apis-arkts/arkts-apis/arkts-arkts-arraybufferlike-t.md) | Yes |
| byteOffset | number | No |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |

## from

```TypeScript
from(arrayLike: ArrayLike<bigint>): BigInt64Array
```

Creates an array from an array-like or iterable object.

<!--Device-BigInt64ArrayConstructor-from(arrayLike: ArrayLike<bigint>): BigInt64Array--><!--Device-BigInt64ArrayConstructor-from(arrayLike: ArrayLike<bigint>): BigInt64Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike&lt;bigint&gt;](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |

## from

```TypeScript
from<U>(arrayLike: ArrayLike<U>, mapfn: (v: U, k: number) => bigint, thisArg?: any): BigInt64Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike&lt;U&gt;](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md) | Yes |
| mapfn | (v: U, k: number) =&gt; bigint | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |

## of

```TypeScript
of(...items: bigint[]): BigInt64Array
```

Returns a new array from a set of elements.

<!--Device-BigInt64ArrayConstructor-of(...items: bigint[]): BigInt64Array--><!--Device-BigInt64ArrayConstructor-of(...items: bigint[]): BigInt64Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | bigint[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

<!--Device-BigInt64ArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-BigInt64ArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: BigInt64Array
```

**Type:** [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md)
