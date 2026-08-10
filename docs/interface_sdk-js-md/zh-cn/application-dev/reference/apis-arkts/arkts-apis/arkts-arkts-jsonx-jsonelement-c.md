# JsonElement

Core class representing a JSON element that can hold any valid JSON value.Provides type-safe access to JSON values with both strict and lenient APIs.The class maintains an invariant that only one type of value can be set at a time.Attempting to set multiple values will result in a JsonTypeError.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-jsonx-export class JsonElement--><!--Device-jsonx-export class JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(index: int): JsonElement
```

Gets a JSON element from an array by index.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-$_get(index: int): JsonElement--><!--Device-JsonElement-$_get(index: int): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | int | 是 | The index to look up. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | The JSON element associated with the index. |

## $_get

```TypeScript
$_get(key: string): JsonElement
```

Gets a JSON element from an object by key.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-$_get(key: string): JsonElement--><!--Device-JsonElement-$_get(key: string): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | The JSON element associated with the key. |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[string, JsonElement]>
```

Iterator over object properties if jsonType == JsonType.JsonObject.on type error `JsonTypeError` is raised.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-$_iterator(): IterableIterator<[string, JsonElement]>--><!--Device-JsonElement-$_iterator(): IterableIterator<[string, JsonElement]>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [IterableIterator](arkts-arkts-iterator-iterableiterator-i.md)&lt;[string, JsonElement]&gt; | An iterator over the object properties. |

## asArray

```TypeScript
asArray(): Array<JsonElement>
```

Gets an array value from the element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asArray(): Array<JsonElement>--><!--Device-JsonElement-asArray(): Array<JsonElement>-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | The array value. |

## asBigInt

```TypeScript
asBigInt(): bigint
```

Gets a bigint value from the element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asBigInt(): bigint--><!--Device-JsonElement-asBigInt(): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | The bigint value. |

## asBoolean

```TypeScript
asBoolean(): boolean
```

Gets a boolean value from the element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asBoolean(): boolean--><!--Device-JsonElement-asBoolean(): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | The boolean value. |

## asDouble

```TypeScript
asDouble(): double
```

Gets a double value from the element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asDouble(): double--><!--Device-JsonElement-asDouble(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | The double value. |

## asInteger

```TypeScript
asInteger(): int
```

Gets an integer value from the element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asInteger(): int--><!--Device-JsonElement-asInteger(): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The integer value. |

## asLong

```TypeScript
asLong(): long
```

Gets a long value from the element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asLong(): long--><!--Device-JsonElement-asLong(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The long value. |

## asNull

```TypeScript
asNull(): null
```

Gets a null value from the element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asNull(): null--><!--Device-JsonElement-asNull(): null-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| null | The null value. |

## asString

```TypeScript
asString(): string
```

Gets a string value from the element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-asString(): string--><!--Device-JsonElement-asString(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The string value. |

## constructor

```TypeScript
constructor()
```

Default parameterless constructor.Creates an undefined JSON element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-constructor()--><!--Device-JsonElement-constructor()-End-->

**系统能力：** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(other: JsonElement)
```

Copy constructor (deep copy).Creates a new JSON element by copying the values from another JSON element.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-constructor(other: JsonElement)--><!--Device-JsonElement-constructor(other: JsonElement)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 是 | The JSON element to copy from. |

## constructor

```TypeScript
constructor(elements: Record<string, JsonElement>)
```

Creates a new JSON element from a key-value structure.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-constructor(elements: Record<string, JsonElement>)--><!--Device-JsonElement-constructor(elements: Record<string, JsonElement>)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, [JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 | The key-value structure to create from. |

## createArray

```TypeScript
static createArray(elements: Array<JsonElement>): JsonElement
```

Creates a new JSON element containing an array of JSON elements.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createArray(elements: Array<JsonElement>): JsonElement--><!--Device-JsonElement-static createArray(elements: Array<JsonElement>): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elements | Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 | The array of JSON elements to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing the array. |

## createBigInt

```TypeScript
static createBigInt(value: bigint): JsonElement
```

Creates a new JSON element containing a bigint value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createBigInt(value: bigint): JsonElement--><!--Device-JsonElement-static createBigInt(value: bigint): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | The bigint value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing the bigint value. |

## createBoolean

```TypeScript
static createBoolean(value: boolean): JsonElement
```

Creates a new JSON element containing a boolean value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createBoolean(value: boolean): JsonElement--><!--Device-JsonElement-static createBoolean(value: boolean): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | The boolean value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing the boolean value. |

## createDouble

```TypeScript
static createDouble(value: double): JsonElement
```

Creates a new JSON element containing a double value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createDouble(value: double): JsonElement--><!--Device-JsonElement-static createDouble(value: double): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | The double value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing the double value. |

## createInteger

```TypeScript
static createInteger(value: int): JsonElement
```

Creates a new JSON element containing an integer value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createInteger(value: int): JsonElement--><!--Device-JsonElement-static createInteger(value: int): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | The integer value to store. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing the integer value. |

## createLong

```TypeScript
static createLong(value: long): JsonElement
```

Creates a new JSON element containing a long value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createLong(value: long): JsonElement--><!--Device-JsonElement-static createLong(value: long): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | The long value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing the long value. |

## createNull

```TypeScript
static createNull(): JsonElement
```

Creates a new JSON element containing a null value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createNull(): JsonElement--><!--Device-JsonElement-static createNull(): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing null. |

## createObject

```TypeScript
static createObject(map: Map<string, JsonElement>): JsonElement
```

Creates a new JSON element containing an object with key-value pairs.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createObject(map: Map<string, JsonElement>): JsonElement--><!--Device-JsonElement-static createObject(map: Map<string, JsonElement>): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| map | Map&lt;string, [JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 | The map of key-value pairs to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing the object. |

## createString

```TypeScript
static createString(value: string): JsonElement
```

Creates a new JSON element containing a string value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createString(value: string): JsonElement--><!--Device-JsonElement-static createString(value: string): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | The string value to store. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing the string value. |

## createUndefined

```TypeScript
static createUndefined(): JsonElement
```

Creates a new JSON element containing an undefined value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-static createUndefined(): JsonElement--><!--Device-JsonElement-static createUndefined(): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | A new JsonElement containing undefined. |

## getArray

```TypeScript
getArray(key: string): Array<JsonElement>
```

Gets a JSON element from an object by key and ensures it is an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getArray(key: string): Array<JsonElement>--><!--Device-JsonElement-getArray(key: string): Array<JsonElement>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | The JSON element associated with the key. |

## getBigInt

```TypeScript
getBigInt(key: string): bigint
```

Gets a bigint value from an object by key and ensures it is a bigint.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getBigInt(key: string): bigint--><!--Device-JsonElement-getBigInt(key: string): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | The bigint value. |

## getBoolean

```TypeScript
getBoolean(key: string): boolean
```

Gets a boolean value from an object by key.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getBoolean(key: string): boolean--><!--Device-JsonElement-getBoolean(key: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | The boolean value. |

## getDouble

```TypeScript
getDouble(key: string): double
```

Gets a double value from an object by key and ensures it is a double.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getDouble(key: string): double--><!--Device-JsonElement-getDouble(key: string): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | The double value. |

## getElement

```TypeScript
getElement(key: string): JsonElement
```

Gets a JSON element from an object by key.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getElement(key: string): JsonElement--><!--Device-JsonElement-getElement(key: string): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | The JSON element associated with the key. |

## getInteger

```TypeScript
getInteger(key: string): int
```

Gets an integer value from an object by key and ensures it is an integer.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getInteger(key: string): int--><!--Device-JsonElement-getInteger(key: string): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The integer value. |

## getLong

```TypeScript
getLong(key: string): long
```

Gets a long value from an object by key and ensures it is a long.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getLong(key: string): long--><!--Device-JsonElement-getLong(key: string): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The long value. |

## getNull

```TypeScript
getNull(key: string): null
```

Gets a null value from an object by key.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getNull(key: string): null--><!--Device-JsonElement-getNull(key: string): null-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| null | The null value. |

## getString

```TypeScript
getString(key: string): string
```

Gets a string value from an object by key.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-getString(key: string): string--><!--Device-JsonElement-getString(key: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The string value. |

## removeElement

```TypeScript
removeElement(key: string): boolean
```

Removes a JSON element from an object by key.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-removeElement(key: string): boolean--><!--Device-JsonElement-removeElement(key: string): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to remove. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | True if the element was removed, false otherwise. |

## setArray

```TypeScript
setArray(value: Array<JsonElement>): void
```

Sets the current JsonElement to an array value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setArray(value: Array<JsonElement>): void--><!--Device-JsonElement-setArray(value: Array<JsonElement>): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | 是 | The array value to set. |

## setBigInt

```TypeScript
setBigInt(value: bigint): void
```

Sets the current JsonElement to a bigint value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setBigInt(value: bigint): void--><!--Device-JsonElement-setBigInt(value: bigint): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | bigint | 是 | The bigint value to set. |

## setBoolean

```TypeScript
setBoolean(value: boolean): void
```

Sets the current JsonElement to a boolean value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setBoolean(value: boolean): void--><!--Device-JsonElement-setBoolean(value: boolean): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | The boolean value to set. |

## setDouble

```TypeScript
setDouble(value: double): void
```

Sets the current JsonElement to a double value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setDouble(value: double): void--><!--Device-JsonElement-setDouble(value: double): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double | 是 | The double value to set. |

## setElement

```TypeScript
setElement(key: string, value: JsonElement): void
```

Sets a JSON element in an object by key.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setElement(key: string, value: JsonElement): void--><!--Device-JsonElement-setElement(key: string, value: JsonElement): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to set. |
| value | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 是 | The JSON element to set. |

## setInteger

```TypeScript
setInteger(value: int): void
```

Sets the current JsonElement to an integer value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setInteger(value: int): void--><!--Device-JsonElement-setInteger(value: int): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | int | 是 | The integer value to set. &lt;br&gt;The value should be an integer. |

## setLong

```TypeScript
setLong(value: long): void
```

Sets the current JsonElement to a long value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setLong(value: long): void--><!--Device-JsonElement-setLong(value: long): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | long | 是 | The long value to set. |

## setNull

```TypeScript
setNull(): void
```

Sets the current JsonElement to a null value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setNull(): void--><!--Device-JsonElement-setNull(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## setString

```TypeScript
setString(value: string): void
```

Sets the current JsonElement to a string value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setString(value: string): void--><!--Device-JsonElement-setString(value: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | The string value to set. |

## setUndefined

```TypeScript
setUndefined(): void
```

Sets the current JsonElement to an undefined value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-setUndefined(): void--><!--Device-JsonElement-setUndefined(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

## tryAsArray

```TypeScript
tryAsArray(): Array<JsonElement> | undefined
```

Attempts to get an array value from the element.Returns undefined if the value is not an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsArray(): Array<JsonElement> | undefined--><!--Device-JsonElement-tryAsArray(): Array<JsonElement> | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | The array value if found, undefined otherwise. |

## tryAsBigInt

```TypeScript
tryAsBigInt(): bigint | undefined
```

Attempts to get a bigint value from the element.Returns undefined if the value is not a bigint.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsBigInt(): bigint | undefined--><!--Device-JsonElement-tryAsBigInt(): bigint | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | The bigint value if found, undefined otherwise. |

## tryAsBoolean

```TypeScript
tryAsBoolean(): boolean | undefined
```

Attempts to get a boolean value from the element.Returns undefined if the value is not a boolean.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsBoolean(): boolean | undefined--><!--Device-JsonElement-tryAsBoolean(): boolean | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | The boolean value if found, undefined otherwise. |

## tryAsDouble

```TypeScript
tryAsDouble(): double | undefined
```

Attempts to get a double value from the element.Returns undefined if the value is not a double.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsDouble(): double | undefined--><!--Device-JsonElement-tryAsDouble(): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | The double value if found, undefined otherwise. |

## tryAsInteger

```TypeScript
tryAsInteger(): int | undefined
```

Attempts to get an integer value from the element.Returns undefined if the value is not an integer.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsInteger(): int | undefined--><!--Device-JsonElement-tryAsInteger(): int | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The integer value if found, undefined otherwise. |

## tryAsLong

```TypeScript
tryAsLong(): long | undefined
```

Attempts to get a long value from the element.Returns undefined if the value is not a long.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsLong(): long | undefined--><!--Device-JsonElement-tryAsLong(): long | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The long value if found, undefined otherwise. |

## tryAsNull

```TypeScript
tryAsNull(): null | undefined
```

Attempts to get a null value from the element.Returns undefined if the value is not null.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsNull(): null | undefined--><!--Device-JsonElement-tryAsNull(): null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| null | The null value if found, undefined otherwise. |

## tryAsString

```TypeScript
tryAsString(): string | undefined
```

Attempts to get a string value from the element.Returns undefined if the value is not a string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryAsString(): string | undefined--><!--Device-JsonElement-tryAsString(): string | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The string value if found, undefined otherwise. |

## tryGetArray

```TypeScript
tryGetArray(key: string): Array<JsonElement>
```

Attempts to get a JSON element from an object by key and ensures it is an array.Returns an empty array if the key is not found or if the value is not an array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetArray(key: string): Array<JsonElement>--><!--Device-JsonElement-tryGetArray(key: string): Array<JsonElement>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | The JSON element if found, an empty array otherwise. |

## tryGetBigInt

```TypeScript
tryGetBigInt(key: string, fallback: bigint = 0n): bigint
```

Attempts to get a bigint value from an object by key.Returns the fallback value if the key is not found or if the value is not a bigint.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetBigInt(key: string, fallback: bigint = 0n): bigint--><!--Device-JsonElement-tryGetBigInt(key: string, fallback: bigint = 0n): bigint-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |
| fallback | bigint | 是 | The fallback value to return if the key is not found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | The bigint value if found, fallback value otherwise. |

## tryGetBoolean

```TypeScript
tryGetBoolean(key: string, fallback: boolean = false): boolean
```

Attempts to get a boolean value from an object by key.Returns the fallback value if the key is not found or if the value is not a boolean.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetBoolean(key: string, fallback: boolean = false): boolean--><!--Device-JsonElement-tryGetBoolean(key: string, fallback: boolean = false): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |
| fallback | boolean | 是 | The fallback value to return if the key is not found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | The boolean value if found, fallback value otherwise. |

## tryGetDouble

```TypeScript
tryGetDouble(key: string, fallback?: double): double | undefined
```

Attempts to get a double value from an object by key and ensures it is a double.Returns the fallback value if the key is not found or if the value is not a double.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetDouble(key: string, fallback?: double): double | undefined--><!--Device-JsonElement-tryGetDouble(key: string, fallback?: double): double | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |
| fallback | double | 否 | The fallback value to return if the key is not found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | The double value if found, fallback value otherwise. |

## tryGetElement

```TypeScript
tryGetElement(key: string): JsonElement | undefined
```

Attempts to get a JSON element from an object by key.Returns undefined if the key is not found or if this element is not an object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetElement(key: string): JsonElement | undefined--><!--Device-JsonElement-tryGetElement(key: string): JsonElement | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | The JSON element if found, undefined otherwise. |

## tryGetInteger

```TypeScript
tryGetInteger(key: string, fallback: int = 0): int
```

Attempts to get an integer value from an object by key.Returns the fallback value if the key is not found or if the value is not an integer.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetInteger(key: string, fallback: int = 0): int--><!--Device-JsonElement-tryGetInteger(key: string, fallback: int = 0): int-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |
| fallback | int | 是 | The fallback value to return if the key is not found. &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | The integer value if found, fallback value otherwise. |

## tryGetLong

```TypeScript
tryGetLong(key: string, fallback: long = 0): long
```

Attempts to get a long value from an object by key.Returns the fallback value if the key is not found or if the value is not a long.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetLong(key: string, fallback: long = 0): long--><!--Device-JsonElement-tryGetLong(key: string, fallback: long = 0): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |
| fallback | long | 是 | The fallback value to return if the key is not found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | The long value if found, fallback value otherwise. |

## tryGetNull

```TypeScript
tryGetNull(key: string): null | undefined
```

Attempts to get a null value from an object by key.Returns undefined if the key is not found or if the value is not null.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetNull(key: string): null | undefined--><!--Device-JsonElement-tryGetNull(key: string): null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| null | The null value if found, undefined otherwise. |

## tryGetString

```TypeScript
tryGetString(key: string, fallback: string = ""): string
```

Attempts to get a string value from an object by key.Returns the fallback value if the key is not found or if the value is not a string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-tryGetString(key: string, fallback: string = ""): string--><!--Device-JsonElement-tryGetString(key: string, fallback: string = ""): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | The key to look up. |
| fallback | string | 是 | The fallback value to return if the key is not found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The string value if found, fallback value otherwise. |

## jsonKey

```TypeScript
get jsonKey(): string
```

Gets the key associated with this JSON element.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-get jsonKey(): string--><!--Device-JsonElement-get jsonKey(): string-End-->

**系统能力：** SystemCapability.Utils.Lang

## jsonType

```TypeScript
get jsonType(): JsonType
```

Gets the type of the JSON element.

**类型：** [JsonType](arkts-arkts-jsonx-jsontype-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElement-get jsonType(): JsonType--><!--Device-JsonElement-get jsonType(): JsonType-End-->

**系统能力：** SystemCapability.Utils.Lang

