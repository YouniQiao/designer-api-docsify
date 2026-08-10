# ReadonlyArray

**ArkTS模式：** 仅支持ArkTS-Dyn

## find

```TypeScript
find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined
```

Returns the value of the first element in the array where predicate is true, and undefined otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ReadonlyArray-find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined--><!--Device-ReadonlyArray-find<S extends T>(predicate: (this: void, value: T, index: number, obj: readonly T[]) => value is S, thisArg?: any): S | undefined-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (this: void, value: T, index: number, obj: readonly T[]) =&gt; value is S | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| S |  |

## find

```TypeScript
find(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): T | undefined
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, obj: readonly T[]) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T |  |

## findIndex

```TypeScript
findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number
```

Returns the index of the first element in the array where predicate is true, and -1otherwise.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number--><!--Device-ReadonlyArray-findIndex(predicate: (value: T, index: number, obj: readonly T[]) => unknown, thisArg?: any): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicate | (value: T, index: number, obj: readonly T[]) =&gt; unknown | 是 |  |
| thisArg | any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

