# Uint8ClampedArrayConstructor

**ArkTS mode:** ArkTS-Dyn only

## [[Construct]]

```TypeScript
new(length: number): Uint8ClampedArray
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## [[Construct]]

```TypeScript
new(array: ArrayLike<number> | ArrayBufferLike): Uint8ClampedArray
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;number&gt; \| ArrayBufferLike | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## [[Construct]]

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Uint8ClampedArray
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | [ArrayBufferLike](../../apis-arkts/arkts-apis/arkts-arkts-arraybufferlike-t.md) | Yes |  |
| byteOffset | number | No |  |
| length | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## from

```TypeScript
from(arrayLike: ArrayLike<number>): Uint8ClampedArray
```

Creates an array from an array-like or iterable object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Uint8ClampedArrayConstructor-from(arrayLike: ArrayLike<number>): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-from(arrayLike: ArrayLike<number>): Uint8ClampedArray-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;number&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint8ClampedArray
```

Creates an array from an array-like or iterable object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Uint8ClampedArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Uint8ClampedArray-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;T&gt; | Yes |  |
| mapfn | (v: T, k: number) =&gt; number | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## of

```TypeScript
of(...items: number[]): Uint8ClampedArray
```

Returns a new array from a set of elements.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Uint8ClampedArrayConstructor-of(...items: number[]): Uint8ClampedArray--><!--Device-Uint8ClampedArrayConstructor-of(...items: number[]): Uint8ClampedArray-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | number[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md) |  |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Uint8ClampedArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-Uint8ClampedArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: Uint8ClampedArray
```

**Type:** [Uint8ClampedArray](../../apis-arkts/arkts-apis/arkts-arkts-typeduarrays-uint8clampedarray-c.md)

**ArkTS mode:** ArkTS-Dyn only

