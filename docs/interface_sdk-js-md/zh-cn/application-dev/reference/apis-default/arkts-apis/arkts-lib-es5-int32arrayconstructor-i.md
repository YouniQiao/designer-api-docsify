# Int32ArrayConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## [[Construct]]

```TypeScript
new(length: number): Int32Array
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int32Array |  |

## [[Construct]]

```TypeScript
new(array: ArrayLike<number> | ArrayBufferLike): Int32Array
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| array | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;number&gt; \| ArrayBufferLike | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int32Array |  |

## [[Construct]]

```TypeScript
new(buffer: ArrayBufferLike, byteOffset?: number, length?: number): Int32Array
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buffer | [ArrayBufferLike](../../apis-arkts/arkts-apis/arkts-arkts-arraybufferlike-t.md) | 是 |  |
| byteOffset | number | 否 |  |
| length | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int32Array |  |

## from

```TypeScript
from(arrayLike: ArrayLike<number>): Int32Array
```

Creates an array from an array-like or iterable object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Int32ArrayConstructor-from(arrayLike: ArrayLike<number>): Int32Array--><!--Device-Int32ArrayConstructor-from(arrayLike: ArrayLike<number>): Int32Array-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;number&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int32Array |  |

## from

```TypeScript
from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int32Array
```

Creates an array from an array-like or iterable object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Int32ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int32Array--><!--Device-Int32ArrayConstructor-from<T>(arrayLike: ArrayLike<T>, mapfn: (v: T, k: number) => number, thisArg?: any): Int32Array-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arrayLike | [ArrayLike](../../apis-arkts/arkts-apis/arkts-arkts-arraylike-i.md)&lt;T&gt; | 是 |  |
| mapfn | (v: T, k: number) =&gt; number | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int32Array |  |

## of

```TypeScript
of(...items: number[]): Int32Array
```

Returns a new array from a set of elements.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Int32ArrayConstructor-of(...items: number[]): Int32Array--><!--Device-Int32ArrayConstructor-of(...items: number[]): Int32Array-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| items | number[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Int32Array |  |

## BYTES_PER_ELEMENT

```TypeScript
readonly BYTES_PER_ELEMENT: number
```

The size in bytes of each element in the array.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Int32ArrayConstructor-readonly BYTES_PER_ELEMENT: number--><!--Device-Int32ArrayConstructor-readonly BYTES_PER_ELEMENT: number-End-->

## prototype

```TypeScript
readonly prototype: Int32Array
```

**类型：** Int32Array

**ArkTS模式：** 仅支持ArkTS-Dyn

