# Array

**ArkTS模式：** 仅支持ArkTS-Dyn

## copyWithin

```TypeScript
copyWithin(target: number, start: number, end?: number): this
```

Returns the this object after copying a section of the array identified by start and end to the same array starting at position target

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-copyWithin(target: number, start: number, end?: number): this--><!--Device-Array-copyWithin(target: number, start: number, end?: number): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | number | 是 |  |
| start | number | 是 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## fill

```TypeScript
fill(value: T, start?: number, end?: number): this
```

Changes all array elements from `start` to `end` index to a static `value` and returns the modified array

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-fill(value: T, start?: number, end?: number): this--><!--Device-Array-fill(value: T, start?: number, end?: number): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 |  |
| start | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## find

```TypeScript
find<S extends T>(predicate: (this: void, value: T, index: number, obj: T[]) => value is S, thisArg?: any): S | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-find<S extends T>(predicate: (this: void, value: T, index: number, obj: T[]) => value is S, thisArg?: any): S | undefined--><!--Device-Array-find<S extends T>(predicate: (this: void, value: T, index: number, obj: T[]) => value is S, thisArg?: any): S | undefined-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (this: void, value: T, index: number, obj: T[]) =&gt; value is S | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| S |  |

## find

```TypeScript
find(predicate: (value: T, index: number, obj: T[]) => unknown, thisArg?: any): T | undefined
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, obj: T[]) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: number, obj: T[]) => unknown, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Array-findIndex(predicate: (value: T, index: number, obj: T[]) => unknown, thisArg?: any): number--><!--Device-Array-findIndex(predicate: (value: T, index: number, obj: T[]) => unknown, thisArg?: any): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, obj: T[]) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

