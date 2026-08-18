# ReadonlyMap

**Since:** -1

<!--Device-unnamed-interface ReadonlyMap--><!--Device-unnamed-interface ReadonlyMap-End-->

## Modules to Import

```TypeScript
```

## forEach

```TypeScript
forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void, thisArg?: any): void
```

**Since:** -1

<!--Device-ReadonlyMap-forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void, thisArg?: any): void--><!--Device-ReadonlyMap-forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void, thisArg?: any): void-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callbackfn | (value: V, key: K, map: ReadonlyMap&lt;K, V&gt;) =&gt; void | Yes |  |
| thisArg | any | No |  |

## get

```TypeScript
get(key: K): V | undefined
```

**Since:** -1

<!--Device-ReadonlyMap-get(key: K): V | undefined--><!--Device-ReadonlyMap-get(key: K): V | undefined-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| V |  |

## has

```TypeScript
has(key: K): boolean
```

**Since:** -1

<!--Device-ReadonlyMap-has(key: K): boolean--><!--Device-ReadonlyMap-has(key: K): boolean-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | K | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## size

```TypeScript
readonly size: number
```

**Type:** number

**Since:** -1

<!--Device-ReadonlyMap-readonly size: number--><!--Device-ReadonlyMap-readonly size: number-End-->

