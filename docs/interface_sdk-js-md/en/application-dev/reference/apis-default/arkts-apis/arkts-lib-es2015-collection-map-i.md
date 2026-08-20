# Map

**Since:** -1

<!--Device-unnamed-interface Map--><!--Device-unnamed-interface Map-End-->

## Modules to Import

```TypeScript
```

## clear

```TypeScript
clear(): void
```

**Since:** -1

<!--Device-Map-clear(): void--><!--Device-Map-clear(): void-End-->

## delete

```TypeScript
delete(key: K): boolean
```

**Since:** -1

<!--Device-Map-delete(key: K): boolean--><!--Device-Map-delete(key: K): boolean-End-->

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

**Since:** -1

<!--Device-Map-forEach(callbackfn: (value: V, key: K, map: Map<K, V>) => void, thisArg?: any): void--><!--Device-Map-forEach(callbackfn: (value: V, key: K, map: Map<K, V>) => void, thisArg?: any): void-End-->

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

**Since:** -1

<!--Device-Map-get(key: K): V | undefined--><!--Device-Map-get(key: K): V | undefined-End-->

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

**Since:** -1

<!--Device-Map-has(key: K): boolean--><!--Device-Map-has(key: K): boolean-End-->

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

**Since:** -1

<!--Device-Map-set(key: K, value: V): this--><!--Device-Map-set(key: K, value: V): this-End-->

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

**Since:** -1

<!--Device-Map-readonly size: number--><!--Device-Map-readonly size: number-End-->

