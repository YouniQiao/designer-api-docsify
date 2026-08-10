# Set

**ArkTS模式：** 仅支持ArkTS-Dyn

## add

```TypeScript
add(value: T): this
```

Appends a new element with a specified value to the end of the Set.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-add(value: T): this--><!--Device-Set-add(value: T): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## clear

```TypeScript
clear(): void
```

**ArkTS模式：** 仅支持ArkTS-Dyn

## delete

```TypeScript
delete(value: T): boolean
```

Removes a specified value from the Set.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-delete(value: T): boolean--><!--Device-Set-delete(value: T): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## forEach

```TypeScript
forEach(callbackfn: (value: T, value2: T, set: Set<T>) => void, thisArg?: any): void
```

Executes a provided function once per each value in the Set object, in insertion order.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-forEach(callbackfn: (value: T, value2: T, set: Set<T>) => void, thisArg?: any): void--><!--Device-Set-forEach(callbackfn: (value: T, value2: T, set: Set<T>) => void, thisArg?: any): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: T, value2: T, set: Set&lt;T&gt;) =&gt; void | 是 |  |
| thisArg | any | 否 |  |

## has

```TypeScript
has(value: T): boolean
```

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-has(value: T): boolean--><!--Device-Set-has(value: T): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | T | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## size

```TypeScript
readonly size: number
```

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Set-readonly size: number--><!--Device-Set-readonly size: number-End-->

