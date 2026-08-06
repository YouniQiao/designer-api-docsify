# Atomics

**ArkTS mode:** ArkTS-Dyn only

## add

```TypeScript
add(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Adds a value to the value at the given position in the array, returning the original value.Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-add(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-add(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |
| value | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## and

```TypeScript
and(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Stores the bitwise AND of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-and(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-and(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |
| value | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## compareExchange

```TypeScript
compareExchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, expectedValue: number, replacementValue: number): number
```

Replaces the value at the given position in the array if the original value equals the given expected value, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-compareExchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, expectedValue: number, replacementValue: number): number--><!--Device-Atomics-compareExchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, expectedValue: number, replacementValue: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |
| expectedValue | number | Yes |  |
| replacementValue | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## exchange

```TypeScript
exchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Replaces the value at the given position in the array, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-exchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-exchange(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |
| value | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## isLockFree

```TypeScript
isLockFree(size: number): boolean
```

Returns a value indicating whether high-performance algorithms can use atomic operations(\_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_) or must use locks (\_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_) for the given number of bytes-per-element of a typed array.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-isLockFree(size: number): boolean--><!--Device-Atomics-isLockFree(size: number): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## load

```TypeScript
load(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number): number
```

Returns the value at the given position in the array. Until this atomic operation completes,any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-load(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number): number--><!--Device-Atomics-load(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## notify

```TypeScript
notify(typedArray: Int32Array, index: number, count?: number): number
```

Wakes up sleeping agents that are waiting on the given index of the array, returning the number of agents that were awoken.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-notify(typedArray: Int32Array, index: number, count?: number): number--><!--Device-Atomics-notify(typedArray: Int32Array, index: number, count?: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int32Array | Yes |  |
| index | number | Yes |  |
| count | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## or

```TypeScript
or(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Stores the bitwise OR of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-or(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-or(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |
| value | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## store

```TypeScript
store(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Stores a value at the given position in the array, returning the new value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-store(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-store(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |
| value | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## sub

```TypeScript
sub(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Subtracts a value from the value at the given position in the array, returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-sub(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-sub(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |
| value | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## wait

```TypeScript
wait(typedArray: Int32Array, index: number, value: number, timeout?: number): "ok" | "not-equal" | "timed-out"
```

If the value at the given position in the array is equal to the provided value, the current agent is put to sleep causing execution to suspend until the timeout expires (returning\_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_) or until the agent is awoken (returning \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_); otherwise, returns\_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-wait(typedArray: Int32Array, index: number, value: number, timeout?: number): "ok" | "not-equal" | "timed-out"--><!--Device-Atomics-wait(typedArray: Int32Array, index: number, value: number, timeout?: number): "ok" | "not-equal" | "timed-out"-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int32Array | Yes |  |
| index | number | Yes |  |
| value | number | Yes |  |
| timeout | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| "ok" |  |

## xor

```TypeScript
xor(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number
```

Stores the bitwise XOR of a value with the value at the given position in the array,returning the original value. Until this atomic operation completes, any other read or write operation against the array will block.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Atomics-xor(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number--><!--Device-Atomics-xor(typedArray: Int8Array | Uint8Array | Int16Array | Uint16Array | Int32Array | Uint32Array, index: number, value: number): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typedArray | Int8Array \| Uint8Array \| Int16Array \| Uint16Array \| Int32Array \| Uint32Array | Yes |  |
| index | number | Yes |  |
| value | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| number |  |

## [Symbol.toStringTag]

```TypeScript
readonly [Symbol.toStringTag]: "Atomics"
```

**Type:** "Atomics"

**ArkTS mode:** ArkTS-Dyn only

