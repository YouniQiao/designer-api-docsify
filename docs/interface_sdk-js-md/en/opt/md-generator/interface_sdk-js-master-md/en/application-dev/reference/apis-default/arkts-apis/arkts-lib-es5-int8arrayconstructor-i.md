# Int8ArrayConstructor

## [[Construct]]

```TypeScript
new(length: number): Int8Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## [[Construct]]

```TypeScript
new(array: ArrayLike<number> | ArrayBufferLike): Int8Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | [ArrayLike&lt;number&gt; \](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md) | [ArrayBufferLike](../../apis-arkts/arkts-apis/arkts-arkts-arraybufferlike-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## [[Construct]]

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Int8Array
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
| Int8Array |

## from

```TypeScript
from(arrayLike: ArrayLike<number>): Int8Array
```

Creates an array from an array-like or iterable object.

<!--Device-Int8ArrayConstructor-from(arrayLike: ArrayLike<number>): Int8Array--><!--Device-Int8ArrayConstructor-from(arrayLike: ArrayLike<number>): Int8Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike&lt;number&gt;](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int8Array
```

Creates an array from an array-like or iterable object.

<!--Device-Int8ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int8Array--><!--Device-Int8ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int8Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike&lt;T&gt;](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md) | Yes |
| mapfn | (v: T, k: number) =&gt; number | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## of

```TypeScript
of(...items: number[]): Int8Array
```

Returns a new array from a set of elements.

<!--Device-Int8ArrayConstructor-of(...items: number[]): Int8Array--><!--Device-Int8ArrayConstructor-of(...items: number[]): Int8Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Int8Array |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

<!--Device-Int8ArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-Int8ArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: Int8Array
```

**Type:** Int8Array
