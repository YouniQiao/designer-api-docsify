# BigInt64ArrayConstructor

**ArkTS mode:** ArkTS-Dyn only

## [[Construct]]

```TypeScript
new(length?: number): BigInt64Array
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## [[Construct]]

```TypeScript
new(array: Iterable<bigint>): BigInt64Array
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| array | Iterable&lt;bigint&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## [[Construct]]

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): BigInt64Array
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
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## from

```TypeScript
from(arrayLike: ArrayLike<bigint>): BigInt64Array
```

Creates an array from an array-like or iterable object.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-BigInt64ArrayConstructor-from(arrayLike: ArrayLike<bigint>): BigInt64Array--><!--Device-BigInt64ArrayConstructor-from(arrayLike: ArrayLike<bigint>): BigInt64Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;bigint&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## from

```TypeScript
from<U>(arrayLike: ArrayLike<U>, mapfn: (v: U, k: number) => bigint, thisArg?: any): BigInt64Array
```

**ArkTS mode:** ArkTS-Dyn only

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;U&gt; | Yes |  |
| mapfn | (v: U, k: number) =&gt; bigint | Yes |  |
| thisArg | any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## of

```TypeScript
of(...items: bigint[]): BigInt64Array
```

Returns a new array from a set of elements.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-BigInt64ArrayConstructor-of(...items: bigint[]): BigInt64Array--><!--Device-BigInt64ArrayConstructor-of(...items: bigint[]): BigInt64Array-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| items | bigint[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) |  |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**Type:** number

**ArkTS mode:** ArkTS-Dyn only

<!--Device-BigInt64ArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-BigInt64ArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: BigInt64Array
```

**Type:** [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md)

**ArkTS mode:** ArkTS-Dyn only

