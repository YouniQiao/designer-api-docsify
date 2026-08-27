# Map

## Modules to Import

```TypeScript
```

## clear

```TypeScript
clear(): void
```

## delete

```TypeScript
delete(key: K): boolean
```

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## forEach

```TypeScript
forEach(callbackfn: (value: V, key: K, map: Map<K, V>) => void, thisArg?: any): void
```

Executes a provided function once per each key/value pair in the Map, in insertion order.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: V, key: K, map: Map&lt;K, V&gt;) =&gt; void | Yes |  |
| thisArg | any | No |  |

## get

```TypeScript
get(key: K): V | undefined
```

Returns a specified element from the Map object. If the value that is associated to the provided key is an object, then you will get a reference to that object and any change made to that object will effectively modify it inside the Map.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## has

```TypeScript
has(key: K): boolean
```

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## set

```TypeScript
set(key: K, value: V): this
```

Adds a new element with a specified key and value to the Map. If an element with the same key already exists, the element will be updated.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes |  |
| value | V | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## size

```TypeScript
readonly size: number
```

**Type:** number
