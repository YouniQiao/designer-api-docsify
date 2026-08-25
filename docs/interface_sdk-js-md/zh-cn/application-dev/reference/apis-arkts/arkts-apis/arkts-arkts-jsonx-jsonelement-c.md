# JsonElement

表示JSON元素的核心类，可保存任意合法的JSON值。 同时提供严格与宽松两套API，以类型安全的方式访问JSON值。 该类保持一个不变式：同一时刻只能设置一种类型的值。 尝试设置多个值将导致JsonTypeError。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## $_get

```TypeScript
$_get(index: int): JsonElement
```

按索引从数组中获取JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## $_get

```TypeScript
$_get(key: string): JsonElement
```

按键从对象中获取JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[string, JsonElement]>
```

当jsonType为JsonType.JsonObject时，遍历对象属性的迭代器。 类型错误时抛出`JsonTypeError`。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[string, JsonElement]&gt; |

## asArray

```TypeScript
asArray(): Array<JsonElement>
```

从该元素中获取数组值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; |

## asBigInt

```TypeScript
asBigInt(): bigint
```

从该元素中获取bigint值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| bigint |

## asBoolean

```TypeScript
asBoolean(): boolean
```

从该元素中获取boolean值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean |

## asDouble

```TypeScript
asDouble(): double
```

从该元素中获取double值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| double |

## asInteger

```TypeScript
asInteger(): int
```

从该元素中获取整数值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int |

## asLong

```TypeScript
asLong(): long
```

从该元素中获取long值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long |

## asNull

```TypeScript
asNull(): null
```

从该元素中获取null值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| null |

## asString

```TypeScript
asString(): string
```

从该元素中获取字符串值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |

## constructor

```TypeScript
constructor()
```

默认的无参构造函数。 创建值为undefined的JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(other: JsonElement)
```

拷贝构造函数（深拷贝）。 通过复制另一个JSON元素的值创建新的JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 是 |

## constructor

```TypeScript
constructor(elements: Record<string, JsonElement>)
```

根据键值结构创建新的JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [elements](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Record&lt;string, [JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 |

## createArray

```TypeScript
static createArray(elements: Array<JsonElement>): JsonElement
```

创建包含JSON元素数组的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [elements](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createBigInt

```TypeScript
static createBigInt(value: bigint): JsonElement
```

创建包含bigint值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createBoolean

```TypeScript
static createBoolean(value: boolean): JsonElement
```

创建包含boolean值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createDouble

```TypeScript
static createDouble(value: double): JsonElement
```

创建包含double值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createInteger

```TypeScript
static createInteger(value: int): JsonElement
```

创建包含整数值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createLong

```TypeScript
static createLong(value: long): JsonElement
```

创建包含long值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | long | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createNull

```TypeScript
static createNull(): JsonElement
```

创建包含null值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createObject

```TypeScript
static createObject(map: Map<string, JsonElement>): JsonElement
```

创建包含键值对对象的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| map | Map&lt;string, [JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createString

```TypeScript
static createString(value: string): JsonElement
```

创建包含字符串值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createUndefined

```TypeScript
static createUndefined(): JsonElement
```

创建包含undefined值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## getArray

```TypeScript
getArray(key: string): Array<JsonElement>
```

按键从对象中获取JSON元素，并确保其为数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; |

## getBigInt

```TypeScript
getBigInt(key: string): bigint
```

按键从对象中获取bigint值，并确保其为bigint类型。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| bigint |

## getBoolean

```TypeScript
getBoolean(key: string): boolean
```

按键从对象中获取boolean值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## getDouble

```TypeScript
getDouble(key: string): double
```

按键从对象中获取double值，并确保其为double类型。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| double |

## getElement

```TypeScript
getElement(key: string): JsonElement
```

按键从对象中获取JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## getInteger

```TypeScript
getInteger(key: string): int
```

按键从对象中获取整数值，并确保其为整数。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## getLong

```TypeScript
getLong(key: string): long
```

按键从对象中获取long值，并确保其为long类型。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## getNull

```TypeScript
getNull(key: string): null
```

按键从对象中获取null值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| null |

## getString

```TypeScript
getString(key: string): string
```

按键从对象中获取字符串值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## removeElement

```TypeScript
removeElement(key: string): boolean
```

按键从对象中移除JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## setArray

```TypeScript
setArray(value: Array<JsonElement>): void
```

将当前JsonElement设置为数组值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 |

## setBigInt

```TypeScript
setBigInt(value: bigint): void
```

将当前JsonElement设置为bigint值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | bigint | 是 |

## setBoolean

```TypeScript
setBoolean(value: boolean): void
```

将当前JsonElement设置为boolean值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## setDouble

```TypeScript
setDouble(value: double): void
```

将当前JsonElement设置为double值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | double | 是 |

## setElement

```TypeScript
setElement(key: string, value: JsonElement): void
```

按键在对象中设置JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| value | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 是 |

## setInteger

```TypeScript
setInteger(value: int): void
```

将当前JsonElement设置为整数值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int | 是 |

## setLong

```TypeScript
setLong(value: long): void
```

将当前JsonElement设置为long值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | long | 是 |

## setNull

```TypeScript
setNull(): void
```

将当前JsonElement设置为null值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## setString

```TypeScript
setString(value: string): void
```

将当前JsonElement设置为字符串值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |

## setUndefined

```TypeScript
setUndefined(): void
```

将当前JsonElement设置为undefined值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## tryAsArray

```TypeScript
tryAsArray(): Array<JsonElement> | undefined
```

尝试从该元素中获取数组值。 如果该值不是数组，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; \| undefined |

## tryAsBigInt

```TypeScript
tryAsBigInt(): bigint | undefined
```

尝试从该元素中获取bigint值。 如果该值不是bigint值，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| bigint \| undefined |

## tryAsBoolean

```TypeScript
tryAsBoolean(): boolean | undefined
```

尝试从该元素中获取boolean值。 如果该值不是boolean值，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| boolean \| undefined |

## tryAsDouble

```TypeScript
tryAsDouble(): double | undefined
```

尝试从该元素中获取double值。 如果该值不是double值，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| double \| undefined |

## tryAsInteger

```TypeScript
tryAsInteger(): int | undefined
```

尝试从该元素中获取整数值。 如果该值不是整数，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| int \| undefined |

## tryAsLong

```TypeScript
tryAsLong(): long | undefined
```

尝试从该元素中获取long值。 如果该值不是long值，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| long \| undefined |

## tryAsNull

```TypeScript
tryAsNull(): null | undefined
```

尝试从该元素中获取null值。 如果该值不是null，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| null \| undefined |

## tryAsString

```TypeScript
tryAsString(): string | undefined
```

尝试从该元素中获取字符串值。 如果该值不是字符串，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string \| undefined |

## tryGetArray

```TypeScript
tryGetArray(key: string): Array<JsonElement>
```

尝试按键从对象中获取JSON元素，并确保其为数组。 如果未找到该键，或该值不是数组，则返回空数组。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; |

## tryGetBigInt

```TypeScript
tryGetBigInt(key: string, fallback: bigint = 0n): bigint
```

尝试按键从对象中获取bigint值。 如果未找到该键，或该值不是bigint值，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| fallback | bigint | 是 |

**返回值：**

| 类型 |
| --- |
| bigint |

## tryGetBoolean

```TypeScript
tryGetBoolean(key: string, fallback: boolean = false): boolean
```

尝试按键从对象中获取boolean值。 如果未找到该键，或该值不是boolean值，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| fallback | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## tryGetDouble

```TypeScript
tryGetDouble(key: string, fallback?: double): double | undefined
```

尝试按键从对象中获取double值，并确保其为double类型。 如果未找到该键，或该值不是double值，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| fallback | double | 否 |

**返回值：**

| 类型 |
| --- |
| double \| undefined |

## tryGetElement

```TypeScript
tryGetElement(key: string): JsonElement | undefined
```

尝试按键从对象中获取JSON元素。 如果未找到该键，或该元素不是对象，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) \| undefined |

## tryGetInteger

```TypeScript
tryGetInteger(key: string, fallback: int = 0): int
```

尝试按键从对象中获取整数值。 如果未找到该键，或该值不是整数，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| fallback | int | 是 |

**返回值：**

| 类型 |
| --- |
| int |

## tryGetLong

```TypeScript
tryGetLong(key: string, fallback: long = 0): long
```

尝试按键从对象中获取long值。 如果未找到该键，或该值不是long值，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| fallback | long | 是 |

**返回值：**

| 类型 |
| --- |
| long |

## tryGetNull

```TypeScript
tryGetNull(key: string): null | undefined
```

尝试按键从对象中获取null值。 如果未找到该键，或该值不是null，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| null \| undefined |

## tryGetString

```TypeScript
tryGetString(key: string, fallback: string = ""): string
```

尝试按键从对象中获取字符串值。 如果未找到该键，或该值不是字符串，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| fallback | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## jsonKey

```TypeScript
get jsonKey(): string
```

获取与该JSON元素关联的键。

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

## jsonType

```TypeScript
get jsonType(): JsonType
```

获取该JSON元素的类型。

**类型：** [JsonType](arkts-arkts-jsonx-jsontype-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang
