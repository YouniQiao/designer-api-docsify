# JsonElement

Core class representing a JSON element that can hold any valid JSON value. Provides type-safe access to JSON values with both strict and lenient APIs. The class maintains an invariant that only one type of value can be set at a time. Attempting to set multiple values will result in a JsonTypeError.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## $_get

```TypeScript
$_get(index: int): JsonElement
```

Gets a JSON element from an array by index.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## $_get

```TypeScript
$_get(key: string): JsonElement
```

Gets a JSON element from an object by key.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[string, JsonElement]>
```

Iterator over object properties if jsonType == JsonType.JsonObject. on type error `JsonTypeError` is raised.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| IterableIterator & lt;[string, JsonElement] & gt; |

## asArray

```TypeScript
asArray(): Array<JsonElement>
```

Gets an array value from the element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; |

## asBigInt

```TypeScript
asBigInt(): bigint
```

Gets a bigint value from the element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## asBoolean

```TypeScript
asBoolean(): boolean
```

Gets a boolean value from the element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## asDouble

```TypeScript
asDouble(): double
```

Gets a double value from the element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## asInteger

```TypeScript
asInteger(): int
```

Gets an integer value from the element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## asLong

```TypeScript
asLong(): long
```

Gets a long value from the element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## asNull

```TypeScript
asNull(): null
```

Gets a null value from the element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| null |

## asString

```TypeScript
asString(): string
```

Gets a string value from the element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## constructor

```TypeScript
constructor()
```

Default parameterless constructor. Creates an undefined JSON element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(other: JsonElement)
```

Copy constructor (deep copy). Creates a new JSON element by copying the values from another JSON element.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | Yes |

## constructor

```TypeScript
constructor(elements: Record<string, JsonElement>)
```

Creates a new JSON element from a key-value structure.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [elements](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Record&lt;string, [JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | Yes |

## createArray

```TypeScript
static createArray(elements: Array<JsonElement>): JsonElement
```

Creates a new JSON element containing an array of JSON elements.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [elements](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-pagemediaentity-i.md) | Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createBigInt

```TypeScript
static createBigInt(value: bigint): JsonElement
```

Creates a new JSON element containing a bigint value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createBoolean

```TypeScript
static createBoolean(value: boolean): JsonElement
```

Creates a new JSON element containing a boolean value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createDouble

```TypeScript
static createDouble(value: double): JsonElement
```

Creates a new JSON element containing a double value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createInteger

```TypeScript
static createInteger(value: int): JsonElement
```

Creates a new JSON element containing an integer value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createLong

```TypeScript
static createLong(value: long): JsonElement
```

Creates a new JSON element containing a long value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createNull

```TypeScript
static createNull(): JsonElement
```

Creates a new JSON element containing a null value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createObject

```TypeScript
static createObject(map: Map<string, JsonElement>): JsonElement
```

Creates a new JSON element containing an object with key-value pairs.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| map | Map&lt;string, [JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createString

```TypeScript
static createString(value: string): JsonElement
```

Creates a new JSON element containing a string value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## createUndefined

```TypeScript
static createUndefined(): JsonElement
```

Creates a new JSON element containing an undefined value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## getArray

```TypeScript
getArray(key: string): Array<JsonElement>
```

Gets a JSON element from an object by key and ensures it is an array.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; |

## getBigInt

```TypeScript
getBigInt(key: string): bigint
```

Gets a bigint value from an object by key and ensures it is a bigint.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## getBoolean

```TypeScript
getBoolean(key: string): boolean
```

Gets a boolean value from an object by key.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## getDouble

```TypeScript
getDouble(key: string): double
```

Gets a double value from an object by key and ensures it is a double.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double |

## getElement

```TypeScript
getElement(key: string): JsonElement
```

Gets a JSON element from an object by key.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |

## getInteger

```TypeScript
getInteger(key: string): int
```

Gets an integer value from an object by key and ensures it is an integer.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## getLong

```TypeScript
getLong(key: string): long
```

Gets a long value from an object by key and ensures it is a long.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## getNull

```TypeScript
getNull(key: string): null
```

Gets a null value from an object by key.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| null |

## getString

```TypeScript
getString(key: string): string
```

Gets a string value from an object by key.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## removeElement

```TypeScript
removeElement(key: string): boolean
```

Removes a JSON element from an object by key.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## setArray

```TypeScript
setArray(value: Array<JsonElement>): void
```

Sets the current JsonElement to an array value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; | Yes |

## setBigInt

```TypeScript
setBigInt(value: bigint): void
```

Sets the current JsonElement to a bigint value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | bigint | Yes |

## setBoolean

```TypeScript
setBoolean(value: boolean): void
```

Sets the current JsonElement to a boolean value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## setDouble

```TypeScript
setDouble(value: double): void
```

Sets the current JsonElement to a double value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double | Yes |

## setElement

```TypeScript
setElement(key: string, value: JsonElement): void
```

Sets a JSON element in an object by key.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| value | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | Yes |

## setInteger

```TypeScript
setInteger(value: int): void
```

Sets the current JsonElement to an integer value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int | Yes |

## setLong

```TypeScript
setLong(value: long): void
```

Sets the current JsonElement to a long value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | long | Yes |

## setNull

```TypeScript
setNull(): void
```

Sets the current JsonElement to a null value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## setString

```TypeScript
setString(value: string): void
```

Sets the current JsonElement to a string value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## setUndefined

```TypeScript
setUndefined(): void
```

Sets the current JsonElement to an undefined value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## tryAsArray

```TypeScript
tryAsArray(): Array<JsonElement> | undefined
```

Attempts to get an array value from the element. Returns undefined if the value is not an array.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; \| undefined |

## tryAsBigInt

```TypeScript
tryAsBigInt(): bigint | undefined
```

Attempts to get a bigint value from the element. Returns undefined if the value is not a bigint.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint \| undefined |

## tryAsBoolean

```TypeScript
tryAsBoolean(): boolean | undefined
```

Attempts to get a boolean value from the element. Returns undefined if the value is not a boolean.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean \| undefined |

## tryAsDouble

```TypeScript
tryAsDouble(): double | undefined
```

Attempts to get a double value from the element. Returns undefined if the value is not a double.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double \| undefined |

## tryAsInteger

```TypeScript
tryAsInteger(): int | undefined
```

Attempts to get an integer value from the element. Returns undefined if the value is not an integer.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int \| undefined |

## tryAsLong

```TypeScript
tryAsLong(): long | undefined
```

Attempts to get a long value from the element. Returns undefined if the value is not a long.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long \| undefined |

## tryAsNull

```TypeScript
tryAsNull(): null | undefined
```

Attempts to get a null value from the element. Returns undefined if the value is not null.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| null \| undefined |

## tryAsString

```TypeScript
tryAsString(): string | undefined
```

Attempts to get a string value from the element. Returns undefined if the value is not a string.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string \| undefined |

## tryGetArray

```TypeScript
tryGetArray(key: string): Array<JsonElement>
```

Attempts to get a JSON element from an object by key and ensures it is an array. Returns an empty array if the key is not found or if the value is not an array.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[JsonElement](arkts-arkts-jsonx-jsonelement-c.md)&gt; |

## tryGetBigInt

```TypeScript
tryGetBigInt(key: string, fallback: bigint = 0n): bigint
```

Attempts to get a bigint value from an object by key. Returns the fallback value if the key is not found or if the value is not a bigint.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| fallback | bigint | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| bigint |

## tryGetBoolean

```TypeScript
tryGetBoolean(key: string, fallback: boolean = false): boolean
```

Attempts to get a boolean value from an object by key. Returns the fallback value if the key is not found or if the value is not a boolean.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| fallback | boolean | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## tryGetDouble

```TypeScript
tryGetDouble(key: string, fallback?: double): double | undefined
```

Attempts to get a double value from an object by key and ensures it is a double. Returns the fallback value if the key is not found or if the value is not a double.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| fallback | double | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| double \| undefined |

## tryGetElement

```TypeScript
tryGetElement(key: string): JsonElement | undefined
```

Attempts to get a JSON element from an object by key. Returns undefined if the key is not found or if this element is not an object.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) \| undefined |

## tryGetInteger

```TypeScript
tryGetInteger(key: string, fallback: int = 0): int
```

Attempts to get an integer value from an object by key. Returns the fallback value if the key is not found or if the value is not an integer.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| fallback | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| int |

## tryGetLong

```TypeScript
tryGetLong(key: string, fallback: long = 0): long
```

Attempts to get a long value from an object by key. Returns the fallback value if the key is not found or if the value is not a long.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| fallback | long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| long |

## tryGetNull

```TypeScript
tryGetNull(key: string): null | undefined
```

Attempts to get a null value from an object by key. Returns undefined if the key is not found or if the value is not null.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| null \| undefined |

## tryGetString

```TypeScript
tryGetString(key: string, fallback: string = ""): string
```

Attempts to get a string value from an object by key. Returns the fallback value if the key is not found or if the value is not a string.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| fallback | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## jsonKey

```TypeScript
get jsonKey(): string
```

Gets the key associated with this JSON element.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

## jsonType

```TypeScript
get jsonType(): JsonType
```

Gets the type of the JSON element.

**Type:** [JsonType](arkts-arkts-jsonx-jsontype-e.md)

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang
