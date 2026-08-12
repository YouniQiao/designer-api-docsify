# BigUint64ArrayConstructor

## [[Construct]]

```TypeScript
new(length?: number): BigUint64Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigUint64Array](arkts-lib-es2020-bigint-biguint64array-i.md) |

## [[Construct]]

```TypeScript
new(array: Iterable<bigint>): BigUint64Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | Iterable & lt;bigint & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigUint64Array](arkts-lib-es2020-bigint-biguint64array-i.md) |

## [[Construct]]

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): BigUint64Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | [ArrayBufferLike](arkts-arraybufferlike-t.md) | Yes |
| byteOffset | number | No |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigUint64Array](arkts-lib-es2020-bigint-biguint64array-i.md) |

## from

```TypeScript
from(arrayLike: ArrayLike<bigint>): BigUint64Array
```

Creates an array from an array-like or iterable object.

<!--Device-BigUint64ArrayConstructor-from(arrayLike: ArrayLike<bigint>): BigUint64Array--><!--Device-BigUint64ArrayConstructor-from(arrayLike: ArrayLike<bigint>): BigUint64Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](arkts-lib-es5-arraylike-i.md)&lt;bigint&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigUint64Array](arkts-lib-es2020-bigint-biguint64array-i.md) |

## from

```TypeScript
from<U>(arrayLike: ArrayLike<U>, mapfn: (v: U, k: number) => bigint, thisArg?: any): BigUint64Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](arkts-lib-es5-arraylike-i.md)&lt;U&gt; | Yes |
| mapfn | (v: U, k: number) = & gt; bigint | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigUint64Array](arkts-lib-es2020-bigint-biguint64array-i.md) |

## of

```TypeScript
of(...items: bigint[]): BigUint64Array
```

Returns a new array from a set of elements.

<!--Device-BigUint64ArrayConstructor-of(...items: bigint[]): BigUint64Array--><!--Device-BigUint64ArrayConstructor-of(...items: bigint[]): BigUint64Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | bigint[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BigUint64Array](arkts-lib-es2020-bigint-biguint64array-i.md) |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

<!--Device-BigUint64ArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-BigUint64ArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: BigUint64Array
```

**Type:** [BigUint64Array](arkts-lib-es2020-bigint-biguint64array-i.md)
