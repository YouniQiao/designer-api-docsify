# JSON

Represent JSON class

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## parse

```TypeScript
parse<T>(text: string, type: Type): T | null | undefined
```

Parses a JSON string to the specified Type

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| type | [Type](arkts-arkts-util-type-e.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T \| null \| undefined |

## parse

```TypeScript
parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,
        options?: jsonx.ParseOptions): T | null | undefined
```

Parses a JSON string to the specified Type with reviver function

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| reviver | ((key: string, value: Any) = & gt; Any) \ | undefined | Yes |
| type | [Type](arkts-arkts-util-type-e.md) | Yes |
| options | jsonx.ParseOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T \| null \| undefined |

## parse

```TypeScript
parse<T>(json: string, type: Class): T | null | undefined
```

Parses a JSON string to the specified Class

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [json](arkts-util-json.md) | string | Yes |
| type | [Class](arkts-arkts-class-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T \| null \| undefined |

## parse

```TypeScript
parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,
        options?: jsonx.ParseOptions): T | null | undefined
```

Parses a JSON string to the specified Class with reviver function

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [json](arkts-util-json.md) | string | Yes |
| reviver | ((key: string, value: Any) = & gt; Any) \ | undefined | Yes |
| type | [Class](arkts-arkts-class-c.md) | Yes |
| options | jsonx.ParseOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T \| null \| undefined |

## parseJsonArray

```TypeScript
public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>
```

Parses a JSON object string and returns an Array.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| options | jsonx.ParseOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[JsonRecordType](arkts-arkts-jsonrecordtype-t.md)&gt; |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement
```

Parses a JSON string and returns a JsonElement.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| options | jsonx.ParseOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| jsonx.JsonElement |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,
        options?: jsonx.ParseOptions): jsonx.JsonElement
```

Parses a JSON string with a reviver function and returns a JsonElement.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| reviver | (key: string, value: jsonx.JsonElement) = & gt; jsonx.JsonElement | Yes |
| options | jsonx.ParseOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| jsonx.JsonElement |

## parseJsonRecord

```TypeScript
public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>
```

Parses a JSON object string and returns a Record.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| options | jsonx.ParseOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Record&lt;string, [JsonRecordType](arkts-arkts-jsonrecordtype-t.md)&gt; |

## parseUpdate

```TypeScript
parseUpdate<T>(json: string, instance: T): T
```

Parses a JSON string and populates the fields of an existing instance. Unlike parse&lt;T&gt;(json, type), this does NOT require a default constructor. Fields whose keys are absent from the JSON retain their current values on the instance (merge semantics).

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [json](arkts-util-json.md) | string | Yes |
| instance | T | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

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

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [json](arkts-util-json.md) | string | Yes |
| reviver | ((key: string, value: Any) = & gt; Any) \ | undefined | Yes |
| instance | T | Yes |
| options | jsonx.ParseOptions | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |

## stringify

```TypeScript
stringify(d: byte): string
```

Converts byte to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | byte | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: char): string
```

Converts char to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | char | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: short): string
```

Converts short to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | short | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: int): string
```

Converts int to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | int | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: long): string
```

Converts long to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | long | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: float): string
```

Converts float to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | float | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: double): string
```

Converts double to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: bigint): string
```

Converts bigint to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | bigint | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: boolean): string
```

Converts boolean to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | boolean | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: string): string
```

Converts string to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<byte>): string
```

Converts bytes array to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;byte & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<char>): string
```

Converts chars array to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;char & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<short>): string
```

Converts shorts array to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;short & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<int>): string
```

Converts ints array to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;int & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<long>): string
```

Converts longs array to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;long & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<float>): string
```

Converts array of floats to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;float & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<double>): string
```

Converts doubles array to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;double & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<boolean>): string
```

Converts booleans array to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;boolean & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: Array<Double>): string
```

Converts Array of Double to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | Array & lt;Double & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(d: ArrayLike<Double>): string
```

Converts ArrayLike of Double to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | ArrayLike & lt;Double & gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: JsonReplacer): string
```

Converts JsonReplacer to JSON format

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | [JsonReplacer](arkts-arkts-json-jsonreplacer-i.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: Any): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Any | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Any | Yes |
| replacer | ((key: string, value: Any) = & gt; Any) \ | undefined \| null | Yes |
| space | string \| int | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Any | Yes |
| replacer | FixedArray & lt;double \ | string & gt; | Yes |
| space | int \| string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Any | Yes |
| replacer | Array & lt;double \ | string & gt; \ | Array & lt;string & gt; \ | Array & lt;double & gt; | Yes |
| space | int \| string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string
```

Converts a JsonElementSerializable to a JSON string.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elem | jsonx.JsonElementSerializable | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],
        space?: int | string): string
```

Converts a JsonElementSerializable to a JSON string with custom formatting.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elem | jsonx.JsonElementSerializable | Yes |
| replacer | (double \| string)[] | No |
| space | int \| string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement): string
```

Converts a JsonElement to a JSON string.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elem | jsonx.JsonElement | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],
        space?: int | string): string
```

Converts a JsonElement to a JSON string with custom formatting.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| elem | jsonx.JsonElement | Yes |
| replacer | (double \| string)[] | No |
| space | int \| string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(obj: Any): string
```

Converts an object to a JavaScript Object Notation (JSON) string, invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Any | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: ((key: string, value: Any) => Any) | undefined | null,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string, invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Any | Yes |
| replacer | ((key: string, value: Any) = & gt; Any) \ | undefined \| null | Yes |
| space | int \| string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string, invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| obj | Any | Yes |
| replacer | Array & lt;double \ | string & gt; \ | Array & lt;string & gt; \ | Array & lt;double & gt; | Yes |
| space | int \| string | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| string |
