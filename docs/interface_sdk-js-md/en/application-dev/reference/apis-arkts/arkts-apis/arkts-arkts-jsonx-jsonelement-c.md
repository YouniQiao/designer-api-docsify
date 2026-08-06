# JsonElement

Core class representing a JSON element that can hold any valid JSON value.Provides type-safe access to JSON values with both strict and lenient APIs.The class maintains an invariant that only one type of value can be set at a time.Attempting to set multiple values will result in a JsonTypeError.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-jsonx-export class JsonElement--><!--Device-jsonx-export class JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

## $_get

```TypeScript
$_get(index: int): JsonElement
```

Gets a JSON element from an array by index.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-$_get(index: int): JsonElement--><!--Device-JsonElement-$_get(index: int): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index to look up. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The JSON element associated with the index. |

## $_get

```TypeScript
$_get(key: string): JsonElement
```

Gets a JSON element from an object by key.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-$_get(key: string): JsonElement--><!--Device-JsonElement-$_get(key: string): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The JSON element associated with the key. |

## $_iterator

```TypeScript
$_iterator(): IterableIterator<[string, JsonElement]>
```

Iterator over object properties if jsonType == JsonType.JsonObject.on type error \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ is raised.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-$_iterator(): IterableIterator<[string, JsonElement]>--><!--Device-JsonElement-$_iterator(): IterableIterator<[string, JsonElement]>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;[string, JsonElement]&gt; | An iterator over the object properties. |

## asArray

```TypeScript
asArray(): Array<JsonElement>
```

Gets an array value from the element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-asArray(): Array<JsonElement>--><!--Device-JsonElement-asArray(): Array<JsonElement>-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | The array value. |

## asBigInt

```TypeScript
asBigInt(): bigint
```

Gets a bigint value from the element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-asBigInt(): bigint--><!--Device-JsonElement-asBigInt(): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| bigint | The bigint value. |

## asBoolean

```TypeScript
asBoolean(): boolean
```

Gets a boolean value from the element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-asBoolean(): boolean--><!--Device-JsonElement-asBoolean(): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The boolean value. |

## asDouble

```TypeScript
asDouble(): double
```

Gets a double value from the element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-asDouble(): double--><!--Device-JsonElement-asDouble(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | The double value. |

## asInteger

```TypeScript
asInteger(): int
```

Gets an integer value from the element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-asInteger(): int--><!--Device-JsonElement-asInteger(): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The integer value. |

## asLong

```TypeScript
asLong(): long
```

Gets a long value from the element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-asLong(): long--><!--Device-JsonElement-asLong(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | The long value. |

## asNull

```TypeScript
asNull(): null
```

Gets a null value from the element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-asNull(): null--><!--Device-JsonElement-asNull(): null-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| null | The null value. |

## asString

```TypeScript
asString(): string
```

Gets a string value from the element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-asString(): string--><!--Device-JsonElement-asString(): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The string value. |

## constructor

```TypeScript
constructor()
```

Default parameterless constructor.Creates an undefined JSON element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-constructor()--><!--Device-JsonElement-constructor()-End-->

**System capability:** SystemCapability.Utils.Lang

## constructor

```TypeScript
constructor(other: JsonElement)
```

Copy constructor (deep copy).Creates a new JSON element by copying the values from another JSON element.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-constructor(other: JsonElement)--><!--Device-JsonElement-constructor(other: JsonElement)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| other | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The JSON element to copy from. |

## constructor

```TypeScript
constructor(elements: Record<string, JsonElement>)
```

Creates a new JSON element from a key-value structure.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-constructor(elements: Record<string, JsonElement>)--><!--Device-JsonElement-constructor(elements: Record<string, JsonElement>)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, \_\_\_MD\_LINK\_USD\_1\_\_\_&gt; | Yes | The key-value structure to create from. |

## createArray

```TypeScript
static createArray(elements: Array<JsonElement>): JsonElement
```

Creates a new JSON element containing an array of JSON elements.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createArray(elements: Array<JsonElement>): JsonElement--><!--Device-JsonElement-static createArray(elements: Array<JsonElement>): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elements | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | Yes | The array of JSON elements to store. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing the array. |

## createBigInt

```TypeScript
static createBigInt(value: bigint): JsonElement
```

Creates a new JSON element containing a bigint value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createBigInt(value: bigint): JsonElement--><!--Device-JsonElement-static createBigInt(value: bigint): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint | Yes | The bigint value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing the bigint value. |

## createBoolean

```TypeScript
static createBoolean(value: boolean): JsonElement
```

Creates a new JSON element containing a boolean value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createBoolean(value: boolean): JsonElement--><!--Device-JsonElement-static createBoolean(value: boolean): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | The boolean value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing the boolean value. |

## createDouble

```TypeScript
static createDouble(value: double): JsonElement
```

Creates a new JSON element containing a double value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createDouble(value: double): JsonElement--><!--Device-JsonElement-static createDouble(value: double): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The double value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing the double value. |

## createInteger

```TypeScript
static createInteger(value: int): JsonElement
```

Creates a new JSON element containing an integer value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createInteger(value: int): JsonElement--><!--Device-JsonElement-static createInteger(value: int): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | The integer value to store. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing the integer value. |

## createLong

```TypeScript
static createLong(value: long): JsonElement
```

Creates a new JSON element containing a long value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createLong(value: long): JsonElement--><!--Device-JsonElement-static createLong(value: long): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | The long value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing the long value. |

## createNull

```TypeScript
static createNull(): JsonElement
```

Creates a new JSON element containing a null value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createNull(): JsonElement--><!--Device-JsonElement-static createNull(): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing null. |

## createObject

```TypeScript
static createObject(map: Map<string, JsonElement>): JsonElement
```

Creates a new JSON element containing an object with key-value pairs.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createObject(map: Map<string, JsonElement>): JsonElement--><!--Device-JsonElement-static createObject(map: Map<string, JsonElement>): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| map | Map&lt;string, \_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | Yes | The map of key-value pairs to store. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing the object. |

## createString

```TypeScript
static createString(value: string): JsonElement
```

Creates a new JSON element containing a string value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createString(value: string): JsonElement--><!--Device-JsonElement-static createString(value: string): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | The string value to store. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing the string value. |

## createUndefined

```TypeScript
static createUndefined(): JsonElement
```

Creates a new JSON element containing an undefined value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-static createUndefined(): JsonElement--><!--Device-JsonElement-static createUndefined(): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | A new JsonElement containing undefined. |

## getArray

```TypeScript
getArray(key: string): Array<JsonElement>
```

Gets a JSON element from an object by key and ensures it is an array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getArray(key: string): Array<JsonElement>--><!--Device-JsonElement-getArray(key: string): Array<JsonElement>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | The JSON element associated with the key. |

## getBigInt

```TypeScript
getBigInt(key: string): bigint
```

Gets a bigint value from an object by key and ensures it is a bigint.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getBigInt(key: string): bigint--><!--Device-JsonElement-getBigInt(key: string): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | The bigint value. |

## getBoolean

```TypeScript
getBoolean(key: string): boolean
```

Gets a boolean value from an object by key.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getBoolean(key: string): boolean--><!--Device-JsonElement-getBoolean(key: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The boolean value. |

## getDouble

```TypeScript
getDouble(key: string): double
```

Gets a double value from an object by key and ensures it is a double.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getDouble(key: string): double--><!--Device-JsonElement-getDouble(key: string): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| double | The double value. |

## getElement

```TypeScript
getElement(key: string): JsonElement
```

Gets a JSON element from an object by key.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getElement(key: string): JsonElement--><!--Device-JsonElement-getElement(key: string): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The JSON element associated with the key. |

## getInteger

```TypeScript
getInteger(key: string): int
```

Gets an integer value from an object by key and ensures it is an integer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getInteger(key: string): int--><!--Device-JsonElement-getInteger(key: string): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The integer value. |

## getLong

```TypeScript
getLong(key: string): long
```

Gets a long value from an object by key and ensures it is a long.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getLong(key: string): long--><!--Device-JsonElement-getLong(key: string): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The long value. |

## getNull

```TypeScript
getNull(key: string): null
```

Gets a null value from an object by key.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getNull(key: string): null--><!--Device-JsonElement-getNull(key: string): null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| null | The null value. |

## getString

```TypeScript
getString(key: string): string
```

Gets a string value from an object by key.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-getString(key: string): string--><!--Device-JsonElement-getString(key: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The string value. |

## removeElement

```TypeScript
removeElement(key: string): boolean
```

Removes a JSON element from an object by key.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-removeElement(key: string): boolean--><!--Device-JsonElement-removeElement(key: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to remove. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | True if the element was removed, false otherwise. |

## setArray

```TypeScript
setArray(value: Array<JsonElement>): void
```

Sets the current JsonElement to an array value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setArray(value: Array<JsonElement>): void--><!--Device-JsonElement-setArray(value: Array<JsonElement>): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | Yes | The array value to set. |

## setBigInt

```TypeScript
setBigInt(value: bigint): void
```

Sets the current JsonElement to a bigint value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setBigInt(value: bigint): void--><!--Device-JsonElement-setBigInt(value: bigint): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | bigint | Yes | The bigint value to set. |

## setBoolean

```TypeScript
setBoolean(value: boolean): void
```

Sets the current JsonElement to a boolean value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setBoolean(value: boolean): void--><!--Device-JsonElement-setBoolean(value: boolean): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | The boolean value to set. |

## setDouble

```TypeScript
setDouble(value: double): void
```

Sets the current JsonElement to a double value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setDouble(value: double): void--><!--Device-JsonElement-setDouble(value: double): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double | Yes | The double value to set. |

## setElement

```TypeScript
setElement(key: string, value: JsonElement): void
```

Sets a JSON element in an object by key.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setElement(key: string, value: JsonElement): void--><!--Device-JsonElement-setElement(key: string, value: JsonElement): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to set. |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The JSON element to set. |

## setInteger

```TypeScript
setInteger(value: int): void
```

Sets the current JsonElement to an integer value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setInteger(value: int): void--><!--Device-JsonElement-setInteger(value: int): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | The integer value to set. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

## setLong

```TypeScript
setLong(value: long): void
```

Sets the current JsonElement to a long value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setLong(value: long): void--><!--Device-JsonElement-setLong(value: long): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | long | Yes | The long value to set. |

## setNull

```TypeScript
setNull(): void
```

Sets the current JsonElement to a null value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setNull(): void--><!--Device-JsonElement-setNull(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## setString

```TypeScript
setString(value: string): void
```

Sets the current JsonElement to a string value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setString(value: string): void--><!--Device-JsonElement-setString(value: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | The string value to set. |

## setUndefined

```TypeScript
setUndefined(): void
```

Sets the current JsonElement to an undefined value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-setUndefined(): void--><!--Device-JsonElement-setUndefined(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## tryAsArray

```TypeScript
tryAsArray(): Array<JsonElement> | undefined
```

Attempts to get an array value from the element.Returns undefined if the value is not an array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryAsArray(): Array<JsonElement> | undefined--><!--Device-JsonElement-tryAsArray(): Array<JsonElement> | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | The array value if found, undefined otherwise. |

## tryAsBigInt

```TypeScript
tryAsBigInt(): bigint | undefined
```

Attempts to get a bigint value from the element.Returns undefined if the value is not a bigint.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryAsBigInt(): bigint | undefined--><!--Device-JsonElement-tryAsBigInt(): bigint | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| bigint | The bigint value if found, undefined otherwise. |

## tryAsBoolean

```TypeScript
tryAsBoolean(): boolean | undefined
```

Attempts to get a boolean value from the element.Returns undefined if the value is not a boolean.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryAsBoolean(): boolean | undefined--><!--Device-JsonElement-tryAsBoolean(): boolean | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The boolean value if found, undefined otherwise. |

## tryAsDouble

```TypeScript
tryAsDouble(): double | undefined
```

Attempts to get a double value from the element.Returns undefined if the value is not a double.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryAsDouble(): double | undefined--><!--Device-JsonElement-tryAsDouble(): double | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | The double value if found, undefined otherwise. |

## tryAsInteger

```TypeScript
tryAsInteger(): int | undefined
```

Attempts to get an integer value from the element.Returns undefined if the value is not an integer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryAsInteger(): int | undefined--><!--Device-JsonElement-tryAsInteger(): int | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| int | The integer value if found, undefined otherwise. |

## tryAsLong

```TypeScript
tryAsLong(): long | undefined
```

Attempts to get a long value from the element.Returns undefined if the value is not a long.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryAsLong(): long | undefined--><!--Device-JsonElement-tryAsLong(): long | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | The long value if found, undefined otherwise. |

## tryAsNull

```TypeScript
tryAsNull(): null | undefined
```

Attempts to get a null value from the element.Returns undefined if the value is not null.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryAsNull(): null | undefined--><!--Device-JsonElement-tryAsNull(): null | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| null | The null value if found, undefined otherwise. |

## tryAsString

```TypeScript
tryAsString(): string | undefined
```

Attempts to get a string value from the element.Returns undefined if the value is not a string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryAsString(): string | undefined--><!--Device-JsonElement-tryAsString(): string | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| string | The string value if found, undefined otherwise. |

## tryGetArray

```TypeScript
tryGetArray(key: string): Array<JsonElement>
```

Attempts to get a JSON element from an object by key and ensures it is an array.Returns an empty array if the key is not found or if the value is not an array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetArray(key: string): Array<JsonElement>--><!--Device-JsonElement-tryGetArray(key: string): Array<JsonElement>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; | The JSON element if found, an empty array otherwise. |

## tryGetBigInt

```TypeScript
tryGetBigInt(key: string, fallback: bigint = 0n): bigint
```

Attempts to get a bigint value from an object by key.Returns the fallback value if the key is not found or if the value is not a bigint.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetBigInt(key: string, fallback: bigint = 0n): bigint--><!--Device-JsonElement-tryGetBigInt(key: string, fallback: bigint = 0n): bigint-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |
| fallback | bigint | Yes | The fallback value to return if the key is not found. |

**Return value:**

| Type | Description |
| --- | --- |
| bigint | The bigint value if found, fallback value otherwise. |

## tryGetBoolean

```TypeScript
tryGetBoolean(key: string, fallback: boolean = false): boolean
```

Attempts to get a boolean value from an object by key.Returns the fallback value if the key is not found or if the value is not a boolean.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetBoolean(key: string, fallback: boolean = false): boolean--><!--Device-JsonElement-tryGetBoolean(key: string, fallback: boolean = false): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |
| fallback | boolean | Yes | The fallback value to return if the key is not found. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | The boolean value if found, fallback value otherwise. |

## tryGetDouble

```TypeScript
tryGetDouble(key: string, fallback?: double): double | undefined
```

Attempts to get a double value from an object by key and ensures it is a double.Returns the fallback value if the key is not found or if the value is not a double.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetDouble(key: string, fallback?: double): double | undefined--><!--Device-JsonElement-tryGetDouble(key: string, fallback?: double): double | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |
| fallback | double | No | The fallback value to return if the key is not found. |

**Return value:**

| Type | Description |
| --- | --- |
| double | The double value if found, fallback value otherwise. |

## tryGetElement

```TypeScript
tryGetElement(key: string): JsonElement | undefined
```

Attempts to get a JSON element from an object by key.Returns undefined if the key is not found or if this element is not an object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetElement(key: string): JsonElement | undefined--><!--Device-JsonElement-tryGetElement(key: string): JsonElement | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The JSON element if found, undefined otherwise. |

## tryGetInteger

```TypeScript
tryGetInteger(key: string, fallback: int = 0): int
```

Attempts to get an integer value from an object by key.Returns the fallback value if the key is not found or if the value is not an integer.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetInteger(key: string, fallback: int = 0): int--><!--Device-JsonElement-tryGetInteger(key: string, fallback: int = 0): int-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |
| fallback | int | Yes | The fallback value to return if the key is not found. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| int | The integer value if found, fallback value otherwise. |

## tryGetLong

```TypeScript
tryGetLong(key: string, fallback: long = 0): long
```

Attempts to get a long value from an object by key.Returns the fallback value if the key is not found or if the value is not a long.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetLong(key: string, fallback: long = 0): long--><!--Device-JsonElement-tryGetLong(key: string, fallback: long = 0): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |
| fallback | long | Yes | The fallback value to return if the key is not found. |

**Return value:**

| Type | Description |
| --- | --- |
| long | The long value if found, fallback value otherwise. |

## tryGetNull

```TypeScript
tryGetNull(key: string): null | undefined
```

Attempts to get a null value from an object by key.Returns undefined if the key is not found or if the value is not null.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetNull(key: string): null | undefined--><!--Device-JsonElement-tryGetNull(key: string): null | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |

**Return value:**

| Type | Description |
| --- | --- |
| null | The null value if found, undefined otherwise. |

## tryGetString

```TypeScript
tryGetString(key: string, fallback: string = ""): string
```

Attempts to get a string value from an object by key.Returns the fallback value if the key is not found or if the value is not a string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-tryGetString(key: string, fallback: string = ""): string--><!--Device-JsonElement-tryGetString(key: string, fallback: string = ""): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | The key to look up. |
| fallback | string | Yes | The fallback value to return if the key is not found. |

**Return value:**

| Type | Description |
| --- | --- |
| string | The string value if found, fallback value otherwise. |

## jsonKey

```TypeScript
get jsonKey(): string
```

Gets the key associated with this JSON element.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-get jsonKey(): string--><!--Device-JsonElement-get jsonKey(): string-End-->

**System capability:** SystemCapability.Utils.Lang

## jsonType

```TypeScript
get jsonType(): JsonType
```

Gets the type of the JSON element.

**Type:** JsonType

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElement-get jsonType(): JsonType--><!--Device-JsonElement-get jsonType(): JsonType-End-->

**System capability:** SystemCapability.Utils.Lang

