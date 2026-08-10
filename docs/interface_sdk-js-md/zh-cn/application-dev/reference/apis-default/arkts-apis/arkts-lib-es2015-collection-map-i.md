# Map

**ArkTS模式：** 仅支持ArkTS-Dyn

## clear

```TypeScript
clear(): void
```

**ArkTS模式：** 仅支持ArkTS-Dyn

## delete

```TypeScript
delete(key: K): boolean
```

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Map-delete(key: K): boolean--><!--Device-Map-delete(key: K): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## forEach

```TypeScript
forEach(callbackfn: (value: V, key: K, map: Map<K, V>) => void, thisArg?: any): void
```

Executes a provided function once per each key/value pair in the Map, in insertion order.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Map-forEach(callbackfn: (value: V, key: K, map: Map<K, V>) => void, thisArg?: any): void--><!--Device-Map-forEach(callbackfn: (value: V, key: K, map: Map<K, V>) => void, thisArg?: any): void-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: V, key: K, map: Map&lt;K, V&gt;) =&gt; void | 是 |  |
| thisArg | any | 否 |  |

## get

```TypeScript
get(key: K): V | undefined
```

Returns a specified element from the Map object. If the value that is associated to the provided key is an object, then you will get a reference to that object and any change made to that object will effectively modify it inside the Map.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Map-get(key: K): V | undefined--><!--Device-Map-get(key: K): V | undefined-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V |  |

## has

```TypeScript
has(key: K): boolean
```

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Map-has(key: K): boolean--><!--Device-Map-has(key: K): boolean-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean |  |

## set

```TypeScript
set(key: K, value: V): this
```

Adds a new element with a specified key and value to the Map. If an element with the same key already exists, the element will be updated.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Map-set(key: K, value: V): this--><!--Device-Map-set(key: K, value: V): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 |  |
| value | V | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| this |  |

## size

```TypeScript
readonly size: number
```

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Map-readonly size: number--><!--Device-Map-readonly size: number-End-->

