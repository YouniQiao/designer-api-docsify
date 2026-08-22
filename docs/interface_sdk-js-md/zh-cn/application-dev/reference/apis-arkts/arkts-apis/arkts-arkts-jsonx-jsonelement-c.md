# JsonElement

表示JSON元素的核心类，可保存任意合法的JSON值。 同时提供严格与宽松两套API，以类型安全的方式访问JSON值。 该类保持一个不变式：同一时刻只能设置一种类型的值。 尝试设置多个值将导致JsonTypeError。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

<!--Device-jsonx-export class JsonElement--><!--Device-jsonx-export class JsonElement-End-->

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

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-$_get(index: int): JsonElement--><!--Device-JsonElement-$_get(index: int): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | 待查找的索引。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 该索引关联的JSON元素。 |

## $_get

```TypeScript
$_get(key: string): JsonElement
```

按键从对象中获取JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-$_get(key: string): JsonElement--><!--Device-JsonElement-$_get(key: string): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 该键关联的JSON元素。 |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[string, JsonElement]>
```

当jsonType为JsonType.JsonObject时，遍历对象属性的迭代器。 类型错误时抛出`JsonTypeError`。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-$_iterator(): IterableIterator<[string, JsonElement]>--><!--Device-JsonElement-$_iterator(): IterableIterator<[string, JsonElement]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[string, JsonElement]&gt; | 遍历对象属性的迭代器。 |

## asArray

```TypeScript
asArray(): Array<JsonElement>
```

从该元素中获取数组值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asArray(): Array<JsonElement>--><!--Device-JsonElement-asArray(): Array<JsonElement>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 数组值。 |

## asBigInt

```TypeScript
asBigInt(): bigint
```

从该元素中获取bigint值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asBigInt(): bigint--><!--Device-JsonElement-asBigInt(): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | bigint值。 |

## asBoolean

```TypeScript
asBoolean(): boolean
```

从该元素中获取boolean值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asBoolean(): boolean--><!--Device-JsonElement-asBoolean(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | boolean值。 |

## asDouble

```TypeScript
asDouble(): double
```

从该元素中获取double值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asDouble(): double--><!--Device-JsonElement-asDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double值。 |

## asInteger

```TypeScript
asInteger(): int
```

从该元素中获取整数值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asInteger(): int--><!--Device-JsonElement-asInteger(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 整数值。 |

## asLong

```TypeScript
asLong(): long
```

从该元素中获取long值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asLong(): long--><!--Device-JsonElement-asLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long值。 |

## asNull

```TypeScript
asNull(): null
```

从该元素中获取null值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asNull(): null--><!--Device-JsonElement-asNull(): null-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| null | null值。 |

## asString

```TypeScript
asString(): string
```

从该元素中获取字符串值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asString(): string--><!--Device-JsonElement-asString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串值。 |

## constructor

```TypeScript
constructor()
```

默认的无参构造函数。 创建值为undefined的JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-constructor()--><!--Device-JsonElement-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(other: JsonElement)
```

拷贝构造函数（深拷贝）。 通过复制另一个JSON元素的值创建新的JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-constructor(other: JsonElement)--><!--Device-JsonElement-constructor(other: JsonElement)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 是 | 复制的源JSON元素。 |

## constructor

```TypeScript
constructor(elements: Record<string, JsonElement>)
```

根据键值结构创建新的JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-constructor(elements: Record<string, JsonElement>)--><!--Device-JsonElement-constructor(elements: Record<string, JsonElement>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [Record](arkts-arkts-map-record-c.md)&lt;string, [JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 | 用于创建的键值结构。 |

## createArray

```TypeScript
static createArray(elements: Array<JsonElement>): JsonElement
```

创建包含JSON元素数组的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createArray(elements: Array<JsonElement>): JsonElement--><!--Device-JsonElement-static createArray(elements: Array<JsonElement>): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 | 待存储的JSON元素数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含该数组的新JsonElement。 |

## createBigInt

```TypeScript
static createBigInt(value: bigint): JsonElement
```

创建包含bigint值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createBigInt(value: bigint): JsonElement--><!--Device-JsonElement-static createBigInt(value: bigint): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | 待存储的bigint值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含该bigint值的新JsonElement。 |

## createBoolean

```TypeScript
static createBoolean(value: boolean): JsonElement
```

创建包含boolean值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createBoolean(value: boolean): JsonElement--><!--Device-JsonElement-static createBoolean(value: boolean): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 待存储的boolean值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含该boolean值的新JsonElement。 |

## createDouble

```TypeScript
static createDouble(value: double): JsonElement
```

创建包含double值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createDouble(value: double): JsonElement--><!--Device-JsonElement-static createDouble(value: double): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待存储的double值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含该double值的新JsonElement。 |

## createInteger

```TypeScript
static createInteger(value: int): JsonElement
```

创建包含整数值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createInteger(value: int): JsonElement--><!--Device-JsonElement-static createInteger(value: int): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待存储的整数值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含该整数值的新JsonElement。 |

## createLong

```TypeScript
static createLong(value: long): JsonElement
```

创建包含long值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createLong(value: long): JsonElement--><!--Device-JsonElement-static createLong(value: long): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待存储的long值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含该long值的新JsonElement。 |

## createNull

```TypeScript
static createNull(): JsonElement
```

创建包含null值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createNull(): JsonElement--><!--Device-JsonElement-static createNull(): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含null的新JsonElement。 |

## createObject

```TypeScript
static createObject(map: Map<string, JsonElement>): JsonElement
```

创建包含键值对对象的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createObject(map: Map<string, JsonElement>): JsonElement--><!--Device-JsonElement-static createObject(map: Map<string, JsonElement>): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | Map&lt;string, [JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 | 待存储的键值对映射。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含该对象的新JsonElement。 |

## createString

```TypeScript
static createString(value: string): JsonElement
```

创建包含字符串值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createString(value: string): JsonElement--><!--Device-JsonElement-static createString(value: string): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 待存储的字符串值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含该字符串值的新JsonElement。 |

## createUndefined

```TypeScript
static createUndefined(): JsonElement
```

创建包含undefined值的新JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createUndefined(): JsonElement--><!--Device-JsonElement-static createUndefined(): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 包含undefined的新JsonElement。 |

## getArray

```TypeScript
getArray(key: string): Array<JsonElement>
```

按键从对象中获取JSON元素，并确保其为数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getArray(key: string): Array<JsonElement>--><!--Device-JsonElement-getArray(key: string): Array<JsonElement>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 该键关联的JSON元素。 |

## getBigInt

```TypeScript
getBigInt(key: string): bigint
```

按键从对象中获取bigint值，并确保其为bigint类型。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getBigInt(key: string): bigint--><!--Device-JsonElement-getBigInt(key: string): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | bigint值。 |

## getBoolean

```TypeScript
getBoolean(key: string): boolean
```

按键从对象中获取boolean值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getBoolean(key: string): boolean--><!--Device-JsonElement-getBoolean(key: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | boolean值。 |

## getDouble

```TypeScript
getDouble(key: string): double
```

按键从对象中获取double值，并确保其为double类型。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getDouble(key: string): double--><!--Device-JsonElement-getDouble(key: string): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | double值。 |

## getElement

```TypeScript
getElement(key: string): JsonElement
```

按键从对象中获取JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getElement(key: string): JsonElement--><!--Device-JsonElement-getElement(key: string): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 该键关联的JSON元素。 |

## getInteger

```TypeScript
getInteger(key: string): int
```

按键从对象中获取整数值，并确保其为整数。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getInteger(key: string): int--><!--Device-JsonElement-getInteger(key: string): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 整数值。 |

## getLong

```TypeScript
getLong(key: string): long
```

按键从对象中获取long值，并确保其为long类型。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getLong(key: string): long--><!--Device-JsonElement-getLong(key: string): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | long值。 |

## getNull

```TypeScript
getNull(key: string): null
```

按键从对象中获取null值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getNull(key: string): null--><!--Device-JsonElement-getNull(key: string): null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| null | null值。 |

## getString

```TypeScript
getString(key: string): string
```

按键从对象中获取字符串值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getString(key: string): string--><!--Device-JsonElement-getString(key: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 字符串值。 |

## removeElement

```TypeScript
removeElement(key: string): boolean
```

按键从对象中移除JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-removeElement(key: string): boolean--><!--Device-JsonElement-removeElement(key: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待移除的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果该元素被移除则返回true，否则返回false。 |

## setArray

```TypeScript
setArray(value: Array<JsonElement>): void
```

将当前JsonElement设置为数组值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setArray(value: Array<JsonElement>): void--><!--Device-JsonElement-setArray(value: Array<JsonElement>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 | 待设置的数组值。 |

## setBigInt

```TypeScript
setBigInt(value: bigint): void
```

将当前JsonElement设置为bigint值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setBigInt(value: bigint): void--><!--Device-JsonElement-setBigInt(value: bigint): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | 待设置的bigint值。 |

## setBoolean

```TypeScript
setBoolean(value: boolean): void
```

将当前JsonElement设置为boolean值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setBoolean(value: boolean): void--><!--Device-JsonElement-setBoolean(value: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 待设置的boolean值。 |

## setDouble

```TypeScript
setDouble(value: double): void
```

将当前JsonElement设置为double值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setDouble(value: double): void--><!--Device-JsonElement-setDouble(value: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | 待设置的double值。 |

## setElement

```TypeScript
setElement(key: string, value: JsonElement): void
```

按键在对象中设置JSON元素。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setElement(key: string, value: JsonElement): void--><!--Device-JsonElement-setElement(key: string, value: JsonElement): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待设置的键。 |
| value | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 是 | 待设置的JSON元素。 |

## setInteger

```TypeScript
setInteger(value: int): void
```

将当前JsonElement设置为整数值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setInteger(value: int): void--><!--Device-JsonElement-setInteger(value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | 待设置的整数值。 <br>取值约束：应为整数。 |

## setLong

```TypeScript
setLong(value: long): void
```

将当前JsonElement设置为long值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setLong(value: long): void--><!--Device-JsonElement-setLong(value: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | 待设置的long值。 |

## setNull

```TypeScript
setNull(): void
```

将当前JsonElement设置为null值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setNull(): void--><!--Device-JsonElement-setNull(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## setString

```TypeScript
setString(value: string): void
```

将当前JsonElement设置为字符串值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setString(value: string): void--><!--Device-JsonElement-setString(value: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 待设置的字符串值。 |

## setUndefined

```TypeScript
setUndefined(): void
```

将当前JsonElement设置为undefined值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setUndefined(): void--><!--Device-JsonElement-setUndefined(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## tryAsArray

```TypeScript
tryAsArray(): Array<JsonElement> | undefined
```

尝试从该元素中获取数组值。 如果该值不是数组，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsArray(): Array<JsonElement> | undefined--><!--Device-JsonElement-tryAsArray(): Array<JsonElement> | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; \| undefined | 找到时返回对应的数组值，否则返回undefined。 |

## tryAsBigInt

```TypeScript
tryAsBigInt(): bigint | undefined
```

尝试从该元素中获取bigint值。 如果该值不是bigint值，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsBigInt(): bigint | undefined--><!--Device-JsonElement-tryAsBigInt(): bigint | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint \| undefined | 找到时返回对应的bigint值，否则返回undefined。 |

## tryAsBoolean

```TypeScript
tryAsBoolean(): boolean | undefined
```

尝试从该元素中获取boolean值。 如果该值不是boolean值，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsBoolean(): boolean | undefined--><!--Device-JsonElement-tryAsBoolean(): boolean | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean \| undefined | 找到时返回对应的boolean值，否则返回undefined。 |

## tryAsDouble

```TypeScript
tryAsDouble(): double | undefined
```

尝试从该元素中获取double值。 如果该值不是double值，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsDouble(): double | undefined--><!--Device-JsonElement-tryAsDouble(): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double \| undefined | 找到时返回对应的double值，否则返回undefined。 |

## tryAsInteger

```TypeScript
tryAsInteger(): int | undefined
```

尝试从该元素中获取整数值。 如果该值不是整数，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsInteger(): int | undefined--><!--Device-JsonElement-tryAsInteger(): int | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int \| undefined | 找到时返回对应的整数值，否则返回undefined。 |

## tryAsLong

```TypeScript
tryAsLong(): long | undefined
```

尝试从该元素中获取long值。 如果该值不是long值，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsLong(): long | undefined--><!--Device-JsonElement-tryAsLong(): long | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long \| undefined | 找到时返回对应的long值，否则返回undefined。 |

## tryAsNull

```TypeScript
tryAsNull(): null | undefined
```

尝试从该元素中获取null值。 如果该值不是null，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsNull(): null | undefined--><!--Device-JsonElement-tryAsNull(): null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| null \| undefined | 找到时返回null值，否则返回undefined。 |

## tryAsString

```TypeScript
tryAsString(): string | undefined
```

尝试从该元素中获取字符串值。 如果该值不是字符串，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsString(): string | undefined--><!--Device-JsonElement-tryAsString(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string \| undefined | 找到时返回对应的字符串值，否则返回undefined。 |

## tryGetArray

```TypeScript
tryGetArray(key: string): Array<JsonElement>
```

尝试按键从对象中获取JSON元素，并确保其为数组。 如果未找到该键，或该值不是数组，则返回空数组。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetArray(key: string): Array<JsonElement>--><!--Device-JsonElement-tryGetArray(key: string): Array<JsonElement>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 找到时返回对应的JSON元素，否则返回空数组。 |

## tryGetBigInt

```TypeScript
tryGetBigInt(key: string, fallback: bigint = 0n): bigint
```

尝试按键从对象中获取bigint值。 如果未找到该键，或该值不是bigint值，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetBigInt(key: string, fallback: bigint = 0n): bigint--><!--Device-JsonElement-tryGetBigInt(key: string, fallback: bigint = 0n): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |
| fallback | bigint | 是 | 未找到该键时返回的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | 找到时返回对应的bigint值，否则返回默认值。 |

## tryGetBoolean

```TypeScript
tryGetBoolean(key: string, fallback: boolean = false): boolean
```

尝试按键从对象中获取boolean值。 如果未找到该键，或该值不是boolean值，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetBoolean(key: string, fallback: boolean = false): boolean--><!--Device-JsonElement-tryGetBoolean(key: string, fallback: boolean = false): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |
| fallback | boolean | 是 | 未找到该键时返回的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 找到时返回对应的boolean值，否则返回默认值。 |

## tryGetDouble

```TypeScript
tryGetDouble(key: string, fallback?: double): double | undefined
```

尝试按键从对象中获取double值，并确保其为double类型。 如果未找到该键，或该值不是double值，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetDouble(key: string, fallback?: double): double | undefined--><!--Device-JsonElement-tryGetDouble(key: string, fallback?: double): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |
| fallback | double | 否 | 未找到该键时返回的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double \| undefined | 找到时返回对应的double值，否则返回默认值。 |

## tryGetElement

```TypeScript
tryGetElement(key: string): JsonElement | undefined
```

尝试按键从对象中获取JSON元素。 如果未找到该键，或该元素不是对象，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetElement(key: string): JsonElement | undefined--><!--Device-JsonElement-tryGetElement(key: string): JsonElement | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) \| undefined | 找到时返回对应的JSON元素，否则返回undefined。 |

## tryGetInteger

```TypeScript
tryGetInteger(key: string, fallback: int = 0): int
```

尝试按键从对象中获取整数值。 如果未找到该键，或该值不是整数，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetInteger(key: string, fallback: int = 0): int--><!--Device-JsonElement-tryGetInteger(key: string, fallback: int = 0): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |
| fallback | int | 是 | 未找到该键时返回的默认值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | 找到时返回对应的整数值，否则返回默认值。 |

## tryGetLong

```TypeScript
tryGetLong(key: string, fallback: long = 0): long
```

尝试按键从对象中获取long值。 如果未找到该键，或该值不是long值，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetLong(key: string, fallback: long = 0): long--><!--Device-JsonElement-tryGetLong(key: string, fallback: long = 0): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |
| fallback | long | 是 | 未找到该键时返回的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | 找到时返回对应的long值，否则返回默认值。 |

## tryGetNull

```TypeScript
tryGetNull(key: string): null | undefined
```

尝试按键从对象中获取null值。 如果未找到该键，或该值不是null，则返回undefined。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetNull(key: string): null | undefined--><!--Device-JsonElement-tryGetNull(key: string): null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| null \| undefined | 找到时返回null值，否则返回undefined。 |

## tryGetString

```TypeScript
tryGetString(key: string, fallback: string = ""): string
```

尝试按键从对象中获取字符串值。 如果未找到该键，或该值不是字符串，则返回默认值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetString(key: string, fallback: string = ""): string--><!--Device-JsonElement-tryGetString(key: string, fallback: string = ""): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 待查找的键。 |
| fallback | string | 是 | 未找到该键时返回的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 找到时返回对应的字符串值，否则返回默认值。 |

