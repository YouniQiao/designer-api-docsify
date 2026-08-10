# Array

**ArkTS模式：** 仅支持ArkTS-Dyn

## flat

```TypeScript
flat<A, D extends number = 1>(
        this: A,
        depth?: D
    ): FlatArray<A, D>[]
```

Returns a new array with all sub-array elements concatenated into it recursively up to the specified depth.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-flat<A, D extends number = 1>(        this: A,        depth?: D    ): FlatArray<A, D>[]--><!--Device-Array-flat<A, D extends number = 1>(        this: A,        depth?: D    ): FlatArray<A, D>[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | A | 是 |  |
| depth | D | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FlatArray&lt;A, D&gt;[] |  |

## flatMap

```TypeScript
flatMap<U, This = undefined> (
        callback: (this: This, value: T, index: number, array: T[]) => U | ReadonlyArray<U>,
        thisArg?: This
    ): U[]
```

Calls a defined callback function on each element of an array. Then, flattens the result into a new array.This is identical to a map followed by flat with depth 1.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-flatMap<U, This = undefined> (        callback: (this: This, value: T, index: number, array: T[]) => U | ReadonlyArray<U>,        thisArg?: This    ): U[]--><!--Device-Array-flatMap<U, This = undefined> (        callback: (this: This, value: T, index: number, array: T[]) => U | ReadonlyArray<U>,        thisArg?: This    ): U[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (this: This, value: T, index: number, array: T[]) =&gt; U \| ReadonlyArray&lt;U&gt; | 是 |  |
| thisArg | This | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| U[] |  |

