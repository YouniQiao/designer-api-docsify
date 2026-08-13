# JSON

Represent JSON class

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

<!--Device-unnamed-export class JSON--><!--Device-unnamed-export class JSON-End-->

**System capability:** SystemCapability.Utils.Lang

## parse

```TypeScript
parse<T>(text: string, type: Type): T | null | undefined
```

Parses a JSON string to the specified Type

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-parse<T>(text: string, type: Type): T | null | undefined--><!--Device-JSON-parse<T>(text: string, type: Type): T | null | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | JSON string to parse |
| type | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Yes | Target type for parsing |

**Return value:**

| Type | Description |
| --- | --- |
| T | Parsed object |

## parse

```TypeScript
parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,
        options?: jsonx.ParseOptions): T | null | undefined
```

Parses a JSON string to the specified Type with reviver function

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,        options?: jsonx.ParseOptions): T | null | undefined--><!--Device-JSON-parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,        options?: jsonx.ParseOptions): T | null | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | JSON string to parse |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | Yes | Function to transform values |
| type | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Yes | Target type for parsing |
| options | jsonx.ParseOptions | No | Parse options |

**Return value:**

| Type | Description |
| --- | --- |
| T | Parsed object |

## parse

```TypeScript
parse<T>(json: string, type: Class): T | null | undefined
```

Parses a JSON string to the specified Class

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-parse<T>(json: string, type: Class): T | null | undefined--><!--Device-JSON-parse<T>(json: string, type: Class): T | null | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| json | string | Yes | JSON string to parse |
| type | [Class](arkts-na-class-c.md) | Yes | Target class for parsing |

**Return value:**

| Type | Description |
| --- | --- |
| T | Parsed object |

## parse

```TypeScript
parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,
        options?: jsonx.ParseOptions): T | null | undefined
```

Parses a JSON string to the specified Class with reviver function

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,        options?: jsonx.ParseOptions): T | null | undefined--><!--Device-JSON-parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,        options?: jsonx.ParseOptions): T | null | undefined-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| json | string | Yes | JSON string to parse |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | Yes | Function to transform values |
| type | [Class](arkts-na-class-c.md) | Yes | Target class for parsing |
| options | jsonx.ParseOptions | No | Parse options |

**Return value:**

| Type | Description |
| --- | --- |
| T | Parsed object |

## parseJsonArray

```TypeScript
public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>
```

Parses a JSON object string and returns an Array.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>--><!--Device-JSON-public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | The JSON string to parse |
| options | jsonx.ParseOptions | No | BigInt parsing options |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[JsonRecordType](arkts-na-jsonrecordtype-t.md)&gt; | The parsed Array object |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement
```

Parses a JSON string and returns a JsonElement.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement--><!--Device-JSON-parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | The JSON string to parse |
| options | jsonx.ParseOptions | No | BigInt parsing options |

**Return value:**

| Type | Description |
| --- | --- |
| jsonx.JsonElement | The parsed JSON element |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,
        options?: jsonx.ParseOptions): jsonx.JsonElement
```

Parses a JSON string with a reviver function and returns a JsonElement.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,        options?: jsonx.ParseOptions): jsonx.JsonElement--><!--Device-JSON-parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,        options?: jsonx.ParseOptions): jsonx.JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | The JSON string to parse |
| reviver | (key: string, value: jsonx.JsonElement) =&gt; jsonx.JsonElement | Yes | Function to transform values |
| options | jsonx.ParseOptions | No | BigInt parsing options |

**Return value:**

| Type | Description |
| --- | --- |
| jsonx.JsonElement | The parsed JSON element |

## parseJsonRecord

```TypeScript
public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>
```

Parses a JSON object string and returns a Record.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>--><!--Device-JSON-public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | The JSON string to parse |
| options | jsonx.ParseOptions | No | BigInt parsing options |

**Return value:**

| Type | Description |
| --- | --- |
| Record&lt;string, [JsonRecordType](arkts-na-jsonrecordtype-t.md)&gt; | The parsed Record object |

## parseUpdate

```TypeScript
parseUpdate<T>(json: string, instance: T): T
```

Parses a JSON string and populates the fields of an existing instance. Unlike parse&lt;T&gt;(json, type), this does NOT require a default constructor. Fields whose keys are absent from the JSON retain their current values on the instance (merge semantics).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-parseUpdate<T>(json: string, instance: T): T--><!--Device-JSON-parseUpdate<T>(json: string, instance: T): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| json | string | Yes | JSON string to parse |
| instance | T | Yes | Existing instance whose fields will be populated |

**Return value:**

| Type | Description |
| --- | --- |
| T | The same instance after population |

## parseUpdate

```TypeScript
parseUpdate<T>(
        json: string,
        reviver: ((key: string, value: Any) => Any) | undefined,
        instance: T,
        options?: jsonx.ParseOptions
    ): T
```

Parses a JSON string and populates the fields of an existing instance, with an optional reviver and parse options. Unlike parse&lt;T&gt;(json, type), this does NOT require a default constructor. Fields whose keys are absent from the JSON retain their current values on the instance (merge semantics).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-parseUpdate<T>(        json: string,        reviver: ((key: string, value: Any) => Any) | undefined,        instance: T,        options?: jsonx.ParseOptions    ): T--><!--Device-JSON-parseUpdate<T>(        json: string,        reviver: ((key: string, value: Any) => Any) | undefined,        instance: T,        options?: jsonx.ParseOptions    ): T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| json | string | Yes | JSON string to parse. |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | Yes | Optional function to transform each parsed value, or undefined. |
| instance | T | Yes | Existing instance whose fields will be populated. |
| options | jsonx.ParseOptions | No | Optional ParseOptions (e.g. bigIntMode). If not specified, default parsing options are applied. |

**Return value:**

| Type | Description |
| --- | --- |
| T | The same instance after population |

## stringify

```TypeScript
stringify(d: byte): string
```

Converts byte to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: byte): string--><!--Device-JSON-stringify(d: byte): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | byte | Yes | byte to be converted to a JSON as a Number |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of byte |

## stringify

```TypeScript
stringify(d: char): string
```

Converts char to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: char): string--><!--Device-JSON-stringify(d: char): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | char | Yes | char to be converted to a JSON as a string |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of char |

## stringify

```TypeScript
stringify(d: short): string
```

Converts short to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: short): string--><!--Device-JSON-stringify(d: short): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | short | Yes | short to be converted to a JSON as a Number |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of short |

## stringify

```TypeScript
stringify(d: int): string
```

Converts int to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: int): string--><!--Device-JSON-stringify(d: int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | int | Yes | int to be converted to a JSON as a Number &lt;br&gt;The value should be an integer. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of int |

## stringify

```TypeScript
stringify(d: long): string
```

Converts long to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: long): string--><!--Device-JSON-stringify(d: long): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | long | Yes | long to be converted to a JSON as a Number |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of long |

## stringify

```TypeScript
stringify(d: float): string
```

Converts float to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: float): string--><!--Device-JSON-stringify(d: float): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | float | Yes | float to be converted to a JSON as a Number |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of float |

## stringify

```TypeScript
stringify(d: double): string
```

Converts double to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: double): string--><!--Device-JSON-stringify(d: double): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | double | Yes | double to be converted to a JSON as a Number |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of double |

## stringify

```TypeScript
stringify(d: bigint): string
```

Converts bigint to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: bigint): string--><!--Device-JSON-stringify(d: bigint): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | bigint | Yes | bigint to be converted to a JSON as a Number |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of bigint |

## stringify

```TypeScript
stringify(d: boolean): string
```

Converts boolean to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: boolean): string--><!--Device-JSON-stringify(d: boolean): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | boolean | Yes | boolean to be converted to a JSON as a Boolean literal |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of boolean |

## stringify

```TypeScript
stringify(d: string): string
```

Converts string to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: string): string--><!--Device-JSON-stringify(d: string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | string | Yes | string to be converted to a JSON as a string |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of string |

## stringify

```TypeScript
stringify(d: FixedArray<byte>): string
```

Converts bytes array to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: FixedArray<byte>): string--><!--Device-JSON-stringify(d: FixedArray<byte>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | FixedArray&lt;byte&gt; | Yes | bytes array to be converted to a JSON as an Array of Numbers |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of bytes array |

## stringify

```TypeScript
stringify(d: FixedArray<char>): string
```

Converts chars array to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: FixedArray<char>): string--><!--Device-JSON-stringify(d: FixedArray<char>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | FixedArray&lt;char&gt; | Yes | chars array to be converted to a JSON as an Array of Strings |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of chars array |

## stringify

```TypeScript
stringify(d: FixedArray<short>): string
```

Converts shorts array to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: FixedArray<short>): string--><!--Device-JSON-stringify(d: FixedArray<short>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | FixedArray&lt;short&gt; | Yes | shorts array to be converted to a JSON as an Array of Numbers |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of shorts array |

## stringify

```TypeScript
stringify(d: FixedArray<int>): string
```

Converts ints array to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: FixedArray<int>): string--><!--Device-JSON-stringify(d: FixedArray<int>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | FixedArray&lt;int&gt; | Yes | ints array to be converted to a JSON as an Array of Numbers |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of ints array |

## stringify

```TypeScript
stringify(d: FixedArray<long>): string
```

Converts longs array to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: FixedArray<long>): string--><!--Device-JSON-stringify(d: FixedArray<long>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | FixedArray&lt;long&gt; | Yes | longs array to be converted to a JSON as an Array of Numbers |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of longs array |

## stringify

```TypeScript
stringify(d: FixedArray<float>): string
```

Converts array of floats to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: FixedArray<float>): string--><!--Device-JSON-stringify(d: FixedArray<float>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | FixedArray&lt;float&gt; | Yes | array of float to be converted to a JSON as an Array of Numbers |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of array of floats |

## stringify

```TypeScript
stringify(d: FixedArray<double>): string
```

Converts doubles array to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: FixedArray<double>): string--><!--Device-JSON-stringify(d: FixedArray<double>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | FixedArray&lt;double&gt; | Yes | doubles array to be converted to a JSON as an Array of Numbers |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of doubles array |

## stringify

```TypeScript
stringify(d: FixedArray<boolean>): string
```

Converts booleans array to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: FixedArray<boolean>): string--><!--Device-JSON-stringify(d: FixedArray<boolean>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | FixedArray&lt;boolean&gt; | Yes | booleans array to be converted to a JSON as an Array of Boolean literals |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of booleans array |

## stringify

```TypeScript
stringify(d: Array<Double>): string
```

Converts Array of Double to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: Array<Double>): string--><!--Device-JSON-stringify(d: Array<Double>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | Array&lt;[Double](arkts-na-double-c.md)&gt; | Yes | Array of Double to be converted |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of Array |

## stringify

```TypeScript
stringify(d: ArrayLike<Double>): string
```

Converts ArrayLike of Double to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(d: ArrayLike<Double>): string--><!--Device-JSON-stringify(d: ArrayLike<Double>): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| d | ArrayLike&lt;[Double](arkts-na-double-c.md)&gt; | Yes | ArrayLike of Double to be converted |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of ArrayLike |

## stringify

```TypeScript
stringify(obj: JsonReplacer): string
```

Converts JsonReplacer to JSON format

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(obj: JsonReplacer): string--><!--Device-JSON-stringify(obj: JsonReplacer): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | [JsonReplacer](arkts-na-json-jsonreplacer-i.md) | Yes | JsonReplacer object to be converted |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation |

## stringify

```TypeScript
stringify(obj: Any): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(obj: Any): string--><!--Device-JSON-stringify(obj: Any): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | Yes | An object to be converted |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of Object |

## stringify

```TypeScript
stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string--><!--Device-JSON-stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | Yes | An object to be converted. |
| replacer | ((key: string, value: Any) =&gt; Any) \| undefined \| null | Yes | A that transforms the results. |
| space | string \| int | No | If space is a string, the string is used as the indentation character for each level.If space is an integer, the specified number of spaces (up to a maximum of 10) is used for indentation.If not provided, no formatting is applied. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of Object |

## stringify

```TypeScript
stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string--><!--Device-JSON-stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | Yes | An object to be converted. |
| replacer | FixedArray&lt;double \| string&gt; | Yes | An array of property names to include. |
| space | int \| string | No | If space is a string, the string is used as the indentation character for each level.If space is an integer, the specified number of spaces (up to a maximum of 10) is used for indentation.If not provided, no formatting is applied. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of Object |

## stringify

```TypeScript
stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string--><!--Device-JSON-stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | Yes | An object to be converted. |
| replacer | Array&lt;double \| string&gt; \| Array&lt;string&gt; \| Array&lt;double&gt; | Yes | An array of property names to include.<br>**Since:** 26.0.0 |
| space | int \| string | No | A string or number for indentation. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of Object |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string
```

Converts a JsonElementSerializable to a JSON string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elem | jsonx.JsonElementSerializable | Yes | The JsonElementDeserializable to stringify |

**Return value:**

| Type | Description |
| --- | --- |
| string | The JSON string representation |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],
        space?: int | string): string
```

Converts a JsonElementSerializable to a JSON string with custom formatting.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],        space?: int | string): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],        space?: int | string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elem | jsonx.JsonElementSerializable | Yes | The JsonElementSerializable to stringify |
| replacer | (double \| string)[] | No | An array with elements indicating names of the properties to include |
| space | int \| string | No | A string or number for white space indentation |

**Return value:**

| Type | Description |
| --- | --- |
| string | The JSON string representation |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement): string
```

Converts a JsonElement to a JSON string.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elem | jsonx.JsonElement | Yes | The JsonElement to stringify |

**Return value:**

| Type | Description |
| --- | --- |
| string | The JSON string representation |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],
        space?: int | string): string
```

Converts a JsonElement to a JSON string with custom formatting.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],        space?: int | string): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],        space?: int | string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elem | jsonx.JsonElement | Yes | The JsonElement to stringify |
| replacer | (double \| string)[] | No | An array with elements indicating names of the properties to include |
| space | int \| string | No | A string or number for white space indentation |

**Return value:**

| Type | Description |
| --- | --- |
| string | The JSON string representation |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(obj: Any): string
```

Converts an object to a JavaScript Object Notation (JSON) string, invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringifyWithGetters(obj: Any): string--><!--Device-JSON-stringifyWithGetters(obj: Any): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | Yes | : - An object to be converted. |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of Object, including annotated getter values |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: ((key: string, value: Any) => Any) | undefined | null,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string, invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: ((key: string, value: Any) => Any) | undefined | null,      space?: int | string): string--><!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: ((key: string, value: Any) => Any) | undefined | null,      space?: int | string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | Yes | : - An object to be converted. |
| replacer | ((key: string, value: Any) =&gt; Any) \| undefined \| null | Yes | A function that transforms the results. |
| space | int \| string | No | A string or number that's used to insert white space |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of Object, including annotated getter values |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string, invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string--><!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| obj | Any | Yes | : - An object to be converted. |
| replacer | Array&lt;double \| string&gt; \| Array&lt;string&gt; \| Array&lt;double&gt; | Yes | An array with elements indicating names of the properties in the object that should be included in the resulting JSON string. Annotated getter methods whose names appear in this array are also included. |
| space | int \| string | No | A string or number that's used to insert white space |

**Return value:**

| Type | Description |
| --- | --- |
| string | JSON representation of Object, including annotated getter values |

