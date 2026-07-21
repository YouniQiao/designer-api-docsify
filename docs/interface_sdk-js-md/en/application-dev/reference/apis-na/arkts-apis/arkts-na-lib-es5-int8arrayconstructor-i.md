# Int8ArrayConstructor

<!--Device-unnamed-interface Int8ArrayConstructor--><!--Device-unnamed-interface Int8ArrayConstructor-End-->

## constructor

```TypeScript
new(length: number): Int8Array
```

<!--Device-Int8ArrayConstructor-new(length: number): Int8Array--><!--Device-Int8ArrayConstructor-new(length: number): Int8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Int8Array |  |

## constructor

```TypeScript
new(array: ArrayLike<number> | ArrayBufferLike): Int8Array
```

<!--Device-Int8ArrayConstructor-new(array: ArrayLike<number> | ArrayBufferLike): Int8Array--><!--Device-Int8ArrayConstructor-new(array: ArrayLike<number> | ArrayBufferLike): Int8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;number&gt; \| ArrayBufferLike | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Int8Array |  |

## constructor

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Int8Array
```

<!--Device-Int8ArrayConstructor-new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Int8Array--><!--Device-Int8ArrayConstructor-new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Int8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | [ArrayBufferLike](arkts-na-arraybufferlike-t.md) | Yes |  |
| byteOffset | number | No |  |
| length | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Int8Array |  |

## from

```TypeScript
from(arrayLike: ArrayLike<number>): Int8Array
```

Creates an array from an array-like or iterable object.

<!--Device-Int8ArrayConstructor-from(arrayLike: ArrayLike<number>): Int8Array--><!--Device-Int8ArrayConstructor-from(arrayLike: ArrayLike<number>): Int8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;number&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Int8Array |  |

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int8Array
```

Creates an array from an array-like or iterable object.

<!--Device-Int8ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int8Array--><!--Device-Int8ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-na-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |  |
| mapfn | (v: T, k: number) =&gt; number | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Int8Array |  |

## of

```TypeScript
of(...items: number[]): Int8Array
```

Returns a new array from a set of elements.

<!--Device-Int8ArrayConstructor-of(...items: number[]): Int8Array--><!--Device-Int8ArrayConstructor-of(...items: number[]): Int8Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | number[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Int8Array |  |

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

<!--Device-Int8ArrayConstructor-readonly prototype: Int8Array--><!--Device-Int8ArrayConstructor-readonly prototype: Int8Array-End-->

