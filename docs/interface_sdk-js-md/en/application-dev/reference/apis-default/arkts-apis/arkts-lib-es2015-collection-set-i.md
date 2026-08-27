# Set

## Modules to Import

```TypeScript
```

## add

```TypeScript
add(value: T): this
```

Appends a new element with a specified value to the end of the Set.

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

## delete

```TypeScript
delete(value: T): boolean
```

Removes a specified value from the Set.

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

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: T, value2: T, set: Set&lt;T&gt;) =&gt; void | Yes |  |
| thisArg | any | No |  |

## has

```TypeScript
has(value: T): boolean
```

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
