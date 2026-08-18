# Uint8ClampedArrayConstructor

**Since:** -1

<!--Device-unnamed-interface Uint8ClampedArrayConstructor--><!--Device-unnamed-interface Uint8ClampedArrayConstructor-End-->

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
new(length: number): Uint8ClampedArray
```

**Since:** -1

<!--Device-Uint8ClampedArrayConstructor-new(length: number): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-new(length: number): Uint8ClampedArray-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-na-lib-es5-uint8clampedarray-i.md) |

## constructor

```TypeScript
new(array: ArrayLike<number> | ArrayBufferLike): Uint8ClampedArray
```

**Since:** -1

<!--Device-Uint8ClampedArrayConstructor-new(array: ArrayLike<number> | ArrayBufferLike): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-new(array: ArrayLike<number> | ArrayBufferLike): Uint8ClampedArray-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| array | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;number&gt; \| [ArrayBufferLike](arkts-na-arraybufferlike-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-na-lib-es5-uint8clampedarray-i.md) |

## constructor

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Uint8ClampedArray
```

**Since:** -1

<!--Device-Uint8ClampedArrayConstructor-new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Uint8ClampedArray-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | [ArrayBufferLike](arkts-na-arraybufferlike-t.md) | Yes |
| byteOffset | number | No |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-na-lib-es5-uint8clampedarray-i.md) |

## from

```TypeScript
from(arrayLike: ArrayLike<number>): Uint8ClampedArray
```

Creates an array from an array-like or iterable object.

**Since:** -1

<!--Device-Uint8ClampedArrayConstructor-from(arrayLike: ArrayLike<number>): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-from(arrayLike: ArrayLike<number>): Uint8ClampedArray-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-na-lib-es5-uint8clampedarray-i.md) |

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint8ClampedArray
```

Creates an array from an array-like or iterable object.

**Since:** -1

<!--Device-Uint8ClampedArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint8ClampedArray-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arrayLike | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |
| mapfn | (v: T, k: number) = & gt; number | Yes |
| thisArg | any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-na-lib-es5-uint8clampedarray-i.md) |

## of

```TypeScript
of(...items: number[]): Uint8ClampedArray
```

Returns a new array from a set of elements.

**Since:** -1

<!--Device-Uint8ClampedArrayConstructor-of(...items: number[]): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-of(...items: number[]): Uint8ClampedArray-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | number[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Uint8ClampedArray](arkts-na-lib-es5-uint8clampedarray-i.md) |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

**Since:** -1

<!--Device-Uint8ClampedArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-Uint8ClampedArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: Uint8ClampedArray
```

**Type:** [Uint8ClampedArray](arkts-na-lib-es5-uint8clampedarray-i.md)

**Since:** -1

<!--Device-Uint8ClampedArrayConstructor-readonly prototype: Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-readonly prototype: Uint8ClampedArray-End-->
