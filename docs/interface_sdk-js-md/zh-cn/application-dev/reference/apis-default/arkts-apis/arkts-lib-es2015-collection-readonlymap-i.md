# ReadonlyMap

**ArkTS模式：** 仅支持ArkTS-Dyn

## forEach

```TypeScript
forEach(callbackfn: (value: V, key: K, map: ReadonlyMap<K, V>) => void, thisArg?: any): void
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (value: V, key: K, map: ReadonlyMap&lt;K, V&gt;) =&gt; void | 是 |  |
| thisArg | any | 否 |  |

## get

```TypeScript
get(key: K): V | undefined
```

**ArkTS模式：** 仅支持ArkTS-Dyn

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

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 |  |

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

