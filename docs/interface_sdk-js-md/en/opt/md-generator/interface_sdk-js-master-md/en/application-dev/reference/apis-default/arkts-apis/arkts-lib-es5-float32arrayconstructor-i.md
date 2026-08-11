# Float32ArrayConstructor

## [[Construct]]

```TypeScript
new(length: number): Float32Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Float32Array |

## [[Construct]]

```TypeScript
new(array: ArrayLike<number> | ArrayBufferLike): Float32Array
```

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | [ArrayLike&lt;number&gt; \](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md) | [ArrayBufferLike](../../apis-arkts/arkts-apis/arkts-arkts-arraybufferlike-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Float32Array |

## [[Construct]]

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Float32Array
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
| Float32Array |

## from

```TypeScript
from(arrayLike: ArrayLike<number>): Float32Array
```

Creates an array from an array-like or iterable object.

<!--Device-Float32ArrayConstructor-from(arrayLike: ArrayLike<number>): Float32Array--><!--Device-Float32ArrayConstructor-from(arrayLike: ArrayLike<number>): Float32Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike&lt;number&gt;](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Float32Array |

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Float32Array
```

Creates an array from an array-like or iterable object.

<!--Device-Float32ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Float32Array--><!--Device-Float32ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Float32Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike&lt;T&gt;](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md) | Yes |
| mapfn | (v: T, k: number) =&gt; number | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Float32Array |

## of

```TypeScript
of(...items: number[]): Float32Array
```

Returns a new array from a set of elements.

<!--Device-Float32ArrayConstructor-of(...items: number[]): Float32Array--><!--Device-Float32ArrayConstructor-of(...items: number[]): Float32Array-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Float32Array |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

<!--Device-Float32ArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-Float32ArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: Float32Array
```

**Type:** Float32Array
