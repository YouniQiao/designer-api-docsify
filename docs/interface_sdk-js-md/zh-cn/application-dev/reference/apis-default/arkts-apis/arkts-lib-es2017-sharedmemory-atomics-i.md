# Atomics

**ArkTS模式：** 仅支持ArkTS-Dyn

## add

```TypeScript
add(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Adds a value to the value at the given position in the array, returning the original value.Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-add(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-add(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |
| value | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## and

```TypeScript
and(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Stores the bitwise AND of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-and(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-and(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |
| value | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## compareExchange

```TypeScript
compareExchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, expectedValue: number, replacementValue: number): number
```

Replaces the value at the given position in the array if the original value equals the given expected value, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-compareExchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, expectedValue: number, replacementValue: number): number--><!--Device-Atomics-compareExchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, expectedValue: number, replacementValue: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |
| expectedValue | number | 是 |  |
| replacementValue | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## exchange

```TypeScript
exchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Replaces the value at the given position in the array, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-exchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-exchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |
| value | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## isLockFree

```TypeScript
isLockFree(size: number): boolean
```

Returns a value indicating whether high-performance algorithms can use atomic operations(`true`) or must use locks (`false`) for the given number of bytes-per-element of a typed array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-isLockFree(size: number): boolean--><!--Device-Atomics-isLockFree(size: number): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## load

```TypeScript
load(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number): number
```

Returns the value at the given position in the array. Until this atomic operation completes,any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-load(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number): number--><!--Device-Atomics-load(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## notify

```TypeScript
notify(typedArray: Int32Array, index: number, count?: number): number
```

Wakes up sleeping agents that are waiting on the given index of the array, returning the number of agents that were awoken.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-notify(typedArray: Int32Array, index: number, count?: number): number--><!--Device-Atomics-notify(typedArray: Int32Array, index: number, count?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int32Array | 是 |  |
| index | number | 是 |  |
| count | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## or

```TypeScript
or(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Stores the bitwise OR of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-or(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-or(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |
| value | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## store

```TypeScript
store(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Stores a value at the given position in the array, returning the new value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-store(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-store(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |
| value | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## sub

```TypeScript
sub(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Subtracts a value from the value at the given position in the array, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-sub(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-sub(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |
| value | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## wait

```TypeScript
wait(typedArray: Int32Array, index: number, value: number, timeout?: number): "ok" | "not-equal" | "timed-out"
```

If the value at the given position in the array is equal to the provided value, the current agent is put to sleep causing execution to suspend until the timeout expires (returning`"timed-out"`) or until the agent is awoken (returning `"ok"`); otherwise, returns`"not-equal"`.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-wait(typedArray: Int32Array, index: number, value: number, timeout?: number): "ok" | "not-equal" | "timed-out"--><!--Device-Atomics-wait(typedArray: Int32Array, index: number, value: number, timeout?: number): "ok" | "not-equal" | "timed-out"-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int32Array | 是 |  |
| index | number | 是 |  |
| value | number | 是 |  |
| timeout | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| "ok" |  |

## xor

```TypeScript
xor(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Stores the bitwise XOR of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-xor(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-xor(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | 是 |  |
| index | number | 是 |  |
| value | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "Atomics"
```

**类型：** "Atomics"

**ArkTS模式：** 仅支持ArkTS-Dyn

