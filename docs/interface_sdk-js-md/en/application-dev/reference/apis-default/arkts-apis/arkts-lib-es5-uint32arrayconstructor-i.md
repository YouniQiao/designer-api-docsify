# Uint32ArrayConstructor

**ArkTS mode:** ArkTS-Dyn only

## [[Construct]]

```TypeScript
new(length: number): Uint32Array
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint32Array |  |

## [[Construct]]

```TypeScript
new(array: ArrayLike<number> | ArrayBufferLike): Uint32Array
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | [ArrayLike](arkts-lib-es5-arraylike-i.md)&lt;number&gt; \| [ArrayBufferLike](arkts-arraybufferlike-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint32Array |  |

## [[Construct]]

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Uint32Array
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | [ArrayBufferLike](arkts-arraybufferlike-t.md) | Yes |  |
| byteOffset | number | No |  |
| length | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint32Array |  |

## from

```TypeScript
from(arrayLike: ArrayLike<number>): Uint32Array
```

Creates an array from an array-like or iterable object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Uint32ArrayConstructor-from(arrayLike: ArrayLike<number>): Uint32Array--><!--Device-Uint32ArrayConstructor-from(arrayLike: ArrayLike<number>): Uint32Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-lib-es5-arraylike-i.md)&lt;number&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint32Array |  |

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint32Array
```

Creates an array from an array-like or iterable object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Uint32ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint32Array--><!--Device-Uint32ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint32Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](arkts-lib-es5-arraylike-i.md)&lt;T&gt; | Yes |  |
| mapfn | (v: T, k: number) =&gt; number | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint32Array |  |

## of

```TypeScript
of(...items: number[]): Uint32Array
```

Returns a new array from a set of elements.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Uint32ArrayConstructor-of(...items: number[]): Uint32Array--><!--Device-Uint32ArrayConstructor-of(...items: number[]): Uint32Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | number[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| Uint32Array |  |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Uint32ArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-Uint32ArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: Uint32Array
```

**Type:** Uint32Array

**ArkTS mode:** ArkTS-Dyn only

