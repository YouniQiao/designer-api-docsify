# Atomics

**ArkTS模式：** 仅支持ArkTS-Dyn

## add

```TypeScript
add(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint
```

Adds a value to the value at the given position in the array, returning the original value.Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-add(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint--><!--Device-Atomics-add(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |
| value | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## and

```TypeScript
and(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint
```

Stores the bitwise AND of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-and(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint--><!--Device-Atomics-and(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |
| value | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## compareExchange

```TypeScript
compareExchange(typedArray: BigInt64Array | BigUint64Array, index: number, expectedValue: bigint, replacementValue: bigint): bigint
```

Replaces the value at the given position in the array if the original value equals the given expected value, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-compareExchange(typedArray: BigInt64Array | BigUint64Array, index: number, expectedValue: bigint, replacementValue: bigint): bigint--><!--Device-Atomics-compareExchange(typedArray: BigInt64Array | BigUint64Array, index: number, expectedValue: bigint, replacementValue: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |
| expectedValue | bigint | 是 |  |
| replacementValue | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## exchange

```TypeScript
exchange(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint
```

Replaces the value at the given position in the array, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-exchange(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint--><!--Device-Atomics-exchange(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |
| value | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## load

```TypeScript
load(typedArray: BigInt64Array | BigUint64Array, index: number): bigint
```

Returns the value at the given position in the array. Until this atomic operation completes,any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-load(typedArray: BigInt64Array | BigUint64Array, index: number): bigint--><!--Device-Atomics-load(typedArray: BigInt64Array | BigUint64Array, index: number): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## notify

```TypeScript
notify(typedArray: BigInt64Array, index: number, count?: number): number
```

Wakes up sleeping agents that are waiting on the given index of the array, returning the number of agents that were awoken.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-notify(typedArray: BigInt64Array, index: number, count?: number): number--><!--Device-Atomics-notify(typedArray: BigInt64Array, index: number, count?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) | 是 |  |
| index | number | 是 |  |
| count | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## or

```TypeScript
or(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint
```

Stores the bitwise OR of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-or(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint--><!--Device-Atomics-or(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |
| value | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## store

```TypeScript
store(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint
```

Stores a value at the given position in the array, returning the new value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-store(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint--><!--Device-Atomics-store(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |
| value | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## sub

```TypeScript
sub(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint
```

Subtracts a value from the value at the given position in the array, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-sub(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint--><!--Device-Atomics-sub(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |
| value | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

## wait

```TypeScript
wait(typedArray: BigInt64Array, index: number, value: bigint, timeout?: number): "ok" | "not-equal" | "timed-out"
```

If the value at the given position in the array is equal to the provided value, the current agent is put to sleep causing execution to suspend until the timeout expires (returning`"timed-out"`) or until the agent is awoken (returning `"ok"`); otherwise, returns`"not-equal"`.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-wait(typedArray: BigInt64Array, index: number, value: bigint, timeout?: number): "ok" | "not-equal" | "timed-out"--><!--Device-Atomics-wait(typedArray: BigInt64Array, index: number, value: bigint, timeout?: number): "ok" | "not-equal" | "timed-out"-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) | 是 |  |
| index | number | 是 |  |
| value | bigint | 是 |  |
| timeout | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| "ok" |  |

## xor

```TypeScript
xor(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint
```

Stores the bitwise XOR of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Atomics-xor(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint--><!--Device-Atomics-xor(typedArray: BigInt64Array | BigUint64Array, index: number, value: bigint): bigint-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| typedArray | [BigInt64Array](arkts-lib-es2020-bigint-bigint64array-i.md) \| BigUint64Array | 是 |  |
| index | number | 是 |  |
| value | bigint | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint |  |

