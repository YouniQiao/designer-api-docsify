# Set

**Since:** -1

<!--Device-unnamed-interface Set--><!--Device-unnamed-interface Set-End-->

## Modules to Import

```TypeScript
```

## add

```TypeScript
add(value: T): this
```

Appends a new element with a specified value to the end of the Set.

**Since:** -1

<!--Device-Set-add(value: T): this--><!--Device-Set-add(value: T): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## clear

```TypeScript
clear(): void
```

**Since:** -1

<!--Device-Set-clear(): void--><!--Device-Set-clear(): void-End-->

## delete

```TypeScript
delete(value: T): boolean
```

Removes a specified value from the Set.

**Since:** -1

<!--Device-Set-delete(value: T): boolean--><!--Device-Set-delete(value: T): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## forEach

```TypeScript
forEach(callbackfn: (value: T, value2: T, set: Set<T>) => void, thisArg?: any): void
```

Executes a provided function once per each value in the Set object, in insertion order.

**Since:** -1

<!--Device-Set-forEach(callbackfn: (value: T, value2: T, set: Set<T>) => void, thisArg?: any): void--><!--Device-Set-forEach(callbackfn: (value: T, value2: T, set: Set<T>) => void, thisArg?: any): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: T, value2: T, set: Set&lt;T&gt;) =&gt; void | Yes |  |
| thisArg | any | No |  |

## has

```TypeScript
has(value: T): boolean
```

**Since:** -1

<!--Device-Set-has(value: T): boolean--><!--Device-Set-has(value: T): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## size

```TypeScript
readonly size: number
```

**Type:** number

**Since:** -1

<!--Device-Set-readonly size: number--><!--Device-Set-readonly size: number-End-->

