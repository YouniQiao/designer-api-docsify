# JSON

Represent JSON class

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export class JSON--><!--Device-unnamed-export class JSON-End-->

**系统能力：** SystemCapability.Utils.Lang

## parse

```TypeScript
parse<T>(text: string, type: Type): T | null | undefined
```

Parses a JSON string to the specified Type

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parse<T>(text: string, type: Type): T | null | undefined--><!--Device-JSON-parse<T>(text: string, type: Type): T | null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | JSON string to parse |
| type | [Type](arkts-arkts-util-type-e.md) | 是 | Target type for parsing |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | Parsed object |

## parse

```TypeScript
parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,
        options?: jsonx.ParseOptions): T | null | undefined
```

Parses a JSON string to the specified Type with reviver function

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,        options?: jsonx.ParseOptions): T | null | undefined--><!--Device-JSON-parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,        options?: jsonx.ParseOptions): T | null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | JSON string to parse |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | 是 | Function to transform values |
| type | [Type](arkts-arkts-util-type-e.md) | 是 | Target type for parsing |
| options | jsonx.ParseOptions | 否 | Parse options |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | Parsed object |

## parse

```TypeScript
parse<T>(json: string, type: Class): T | null | undefined
```

Parses a JSON string to the specified Class

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parse<T>(json: string, type: Class): T | null | undefined--><!--Device-JSON-parse<T>(json: string, type: Class): T | null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| json | string | 是 | JSON string to parse |
| type | [Class](arkts-arkts-class-c.md) | 是 | Target class for parsing |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | Parsed object |

## parse

```TypeScript
parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,
        options?: jsonx.ParseOptions): T | null | undefined
```

Parses a JSON string to the specified Class with reviver function

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,        options?: jsonx.ParseOptions): T | null | undefined--><!--Device-JSON-parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,        options?: jsonx.ParseOptions): T | null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| json | string | 是 | JSON string to parse |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | 是 | Function to transform values |
| type | [Class](arkts-arkts-class-c.md) | 是 | Target class for parsing |
| options | jsonx.ParseOptions | 否 | Parse options |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | Parsed object |

## parseJsonArray

```TypeScript
public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>
```

Parses a JSON object string and returns an Array.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>--><!--Device-JSON-public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | The JSON string to parse |
| options | jsonx.ParseOptions | 否 | BigInt parsing options |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;JsonRecordType&gt; | The parsed Array object |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement
```

Parses a JSON string and returns a JsonElement.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement--><!--Device-JSON-parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | The JSON string to parse |
| options | jsonx.ParseOptions | 否 | BigInt parsing options |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| jsonx.JsonElement | The parsed JSON element |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,
        options?: jsonx.ParseOptions): jsonx.JsonElement
```

Parses a JSON string with a reviver function and returns a JsonElement.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,        options?: jsonx.ParseOptions): jsonx.JsonElement--><!--Device-JSON-parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,        options?: jsonx.ParseOptions): jsonx.JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | The JSON string to parse |
| reviver | (key: string, value: jsonx.JsonElement) =&gt; jsonx.JsonElement | 是 | Function to transform values |
| options | jsonx.ParseOptions | 否 | BigInt parsing options |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| jsonx.JsonElement | The parsed JSON element |

## parseJsonRecord

```TypeScript
public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>
```

Parses a JSON object string and returns a Record.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>--><!--Device-JSON-public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | The JSON string to parse |
| options | jsonx.ParseOptions | 否 | BigInt parsing options |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, JsonRecordType&gt; | The parsed Record object |

## parseUpdate

```TypeScript
parseUpdate<T>(json: string, instance: T): T
```

Parses a JSON string and populates the fields of an existing instance.Unlike parse&lt;T&gt;(json, type), this does NOT require a default constructor.Fields whose keys are absent from the JSON retain their current values on the instance (merge semantics).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parseUpdate<T>(json: string, instance: T): T--><!--Device-JSON-parseUpdate<T>(json: string, instance: T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| json | string | 是 | JSON string to parse |
| instance | T | 是 | Existing instance whose fields will be populated |

**返回值：**

| 类型 | 说明 |
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

Parses a JSON string and populates the fields of an existing instance,with an optional reviver and parse options.Unlike parse&lt;T&gt;(json, type), this does NOT require a default constructor.Fields whose keys are absent from the JSON retain their current values on the instance (merge semantics).

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parseUpdate<T>(        json: string,        reviver: ((key: string, value: Any) => Any) | undefined,        instance: T,        options?: jsonx.ParseOptions    ): T--><!--Device-JSON-parseUpdate<T>(        json: string,        reviver: ((key: string, value: Any) => Any) | undefined,        instance: T,        options?: jsonx.ParseOptions    ): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| json | string | 是 | JSON string to parse. |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | 是 | Optional function to transform each parsed value, or undefined. |
| instance | T | 是 | Existing instance whose fields will be populated. |
| options | jsonx.ParseOptions | 否 | Optional ParseOptions (e.g. bigIntMode). If not specified, default parsing options are applied. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | The same instance after population |

## stringify

```TypeScript
stringify(d: byte): string
```

Converts byte to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: byte): string--><!--Device-JSON-stringify(d: byte): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | byte | 是 | byte to be converted to a JSON as a Number |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of byte |

## stringify

```TypeScript
stringify(d: char): string
```

Converts char to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: char): string--><!--Device-JSON-stringify(d: char): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | char | 是 | char to be converted to a JSON as a string |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of char |

## stringify

```TypeScript
stringify(d: short): string
```

Converts short to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: short): string--><!--Device-JSON-stringify(d: short): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | short | 是 | short to be converted to a JSON as a Number |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of short |

## stringify

```TypeScript
stringify(d: int): string
```

Converts int to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: int): string--><!--Device-JSON-stringify(d: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | int | 是 | int to be converted to a JSON as a Number &lt;br&gt;The value should be an integer. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of int |

## stringify

```TypeScript
stringify(d: long): string
```

Converts long to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: long): string--><!--Device-JSON-stringify(d: long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | long | 是 | long to be converted to a JSON as a Number |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of long |

## stringify

```TypeScript
stringify(d: float): string
```

Converts float to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: float): string--><!--Device-JSON-stringify(d: float): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | float | 是 | float to be converted to a JSON as a Number |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of float |

## stringify

```TypeScript
stringify(d: double): string
```

Converts double to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: double): string--><!--Device-JSON-stringify(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | double to be converted to a JSON as a Number |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of double |

## stringify

```TypeScript
stringify(d: bigint): string
```

Converts bigint to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: bigint): string--><!--Device-JSON-stringify(d: bigint): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | bigint | 是 | bigint to be converted to a JSON as a Number |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of bigint |

## stringify

```TypeScript
stringify(d: boolean): string
```

Converts boolean to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: boolean): string--><!--Device-JSON-stringify(d: boolean): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | boolean | 是 | boolean to be converted to a JSON as a Boolean literal |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of boolean |

## stringify

```TypeScript
stringify(d: string): string
```

Converts string to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: string): string--><!--Device-JSON-stringify(d: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | string | 是 | string to be converted to a JSON as a string |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of string |

## stringify

```TypeScript
stringify(d: FixedArray<byte>): string
```

Converts bytes array to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<byte>): string--><!--Device-JSON-stringify(d: FixedArray<byte>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;byte&gt; | 是 | bytes array to be converted to a JSON as an Array of Numbers |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of bytes array |

## stringify

```TypeScript
stringify(d: FixedArray<char>): string
```

Converts chars array to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<char>): string--><!--Device-JSON-stringify(d: FixedArray<char>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;char&gt; | 是 | chars array to be converted to a JSON as an Array of Strings |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of chars array |

## stringify

```TypeScript
stringify(d: FixedArray<short>): string
```

Converts shorts array to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<short>): string--><!--Device-JSON-stringify(d: FixedArray<short>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;short&gt; | 是 | shorts array to be converted to a JSON as an Array of Numbers |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of shorts array |

## stringify

```TypeScript
stringify(d: FixedArray<int>): string
```

Converts ints array to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<int>): string--><!--Device-JSON-stringify(d: FixedArray<int>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;int&gt; | 是 | ints array to be converted to a JSON as an Array of Numbers |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of ints array |

## stringify

```TypeScript
stringify(d: FixedArray<long>): string
```

Converts longs array to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<long>): string--><!--Device-JSON-stringify(d: FixedArray<long>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;long&gt; | 是 | longs array to be converted to a JSON as an Array of Numbers |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of longs array |

## stringify

```TypeScript
stringify(d: FixedArray<float>): string
```

Converts array of floats to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<float>): string--><!--Device-JSON-stringify(d: FixedArray<float>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;float&gt; | 是 | array of float to be converted to a JSON as an Array of Numbers |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of array of floats |

## stringify

```TypeScript
stringify(d: FixedArray<double>): string
```

Converts doubles array to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<double>): string--><!--Device-JSON-stringify(d: FixedArray<double>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;double&gt; | 是 | doubles array to be converted to a JSON as an Array of Numbers |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of doubles array |

## stringify

```TypeScript
stringify(d: FixedArray<boolean>): string
```

Converts booleans array to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<boolean>): string--><!--Device-JSON-stringify(d: FixedArray<boolean>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;boolean&gt; | 是 | booleans array to be converted to a JSON as an Array of Boolean literals |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of booleans array |

## stringify

```TypeScript
stringify(d: Array<Double>): string
```

Converts Array of Double to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: Array<Double>): string--><!--Device-JSON-stringify(d: Array<Double>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | Array&lt;Double&gt; | 是 | Array of Double to be converted |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of Array |

## stringify

```TypeScript
stringify(d: ArrayLike<Double>): string
```

Converts ArrayLike of Double to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: ArrayLike<Double>): string--><!--Device-JSON-stringify(d: ArrayLike<Double>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | [ArrayLike](arkts-arkts-arraylike-i.md)&lt;Double&gt; | 是 | ArrayLike of Double to be converted |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of ArrayLike |

## stringify

```TypeScript
stringify(obj: JsonReplacer): string
```

Converts JsonReplacer to JSON format

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: JsonReplacer): string--><!--Device-JSON-stringify(obj: JsonReplacer): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | [JsonReplacer](arkts-arkts-json-jsonreplacer-i.md) | 是 | JsonReplacer object to be converted |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation |

## stringify

```TypeScript
stringify(obj: Any): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: Any): string--><!--Device-JSON-stringify(obj: Any): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | An object to be converted |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of Object |

## stringify

```TypeScript
stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string--><!--Device-JSON-stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | An object to be converted. |
| replacer | ((key: string, value: Any) =&gt; Any) \| undefined \| null | 是 | A that transforms the results. |
| space | string \| int | 否 | If space is a string, the string is used as the indentation character for each level.If space is an integer, the specified number of spaces (up to a maximum of 10) is used for indentation.If not provided, no formatting is applied. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of Object |

## stringify

```TypeScript
stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string--><!--Device-JSON-stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | An object to be converted. |
| replacer | FixedArray&lt;double \| string&gt; | 是 | An array of property names to include. |
| space | int \| string | 否 | If space is a string, the string is used as the indentation character for each level.If space is an integer, the specified number of spaces (up to a maximum of 10) is used for indentation.If not provided, no formatting is applied. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of Object |

## stringify

```TypeScript
stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string--><!--Device-JSON-stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | An object to be converted. |
| replacer | Array&lt;double \| string&gt; \| Array&lt;string&gt; \| Array&lt;double&gt; | 是 | An array of property names to include.<br>**起始版本：** 26.0.0 |
| space | int \| string | 否 | A string or number for indentation. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of Object |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string
```

Converts a JsonElementSerializable to a JSON string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elem | jsonx.JsonElementSerializable | 是 | The JsonElementDeserializable to stringify |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The JSON string representation |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],
        space?: int | string): string
```

Converts a JsonElementSerializable to a JSON string with custom formatting.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],        space?: int | string): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],        space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elem | jsonx.JsonElementSerializable | 是 | The JsonElementSerializable to stringify |
| replacer | (double \| string)[] | 否 | An array with elements indicating names of the properties to include |
| space | int \| string | 否 | A string or number for white space indentation |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The JSON string representation |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement): string
```

Converts a JsonElement to a JSON string.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elem | jsonx.JsonElement | 是 | The JsonElement to stringify |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The JSON string representation |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],
        space?: int | string): string
```

Converts a JsonElement to a JSON string with custom formatting.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],        space?: int | string): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],        space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elem | jsonx.JsonElement | 是 | The JsonElement to stringify |
| replacer | (double \| string)[] | 否 | An array with elements indicating names of the properties to include |
| space | int \| string | 否 | A string or number for white space indentation |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The JSON string representation |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(obj: Any): string
```

Converts an object to a JavaScript Object Notation (JSON) string,invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringifyWithGetters(obj: Any): string--><!--Device-JSON-stringifyWithGetters(obj: Any): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | : - An object to be converted. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of Object, including annotated getter values |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: ((key: string, value: Any) => Any) | undefined | null,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string,invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: ((key: string, value: Any) => Any) | undefined | null,      space?: int | string): string--><!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: ((key: string, value: Any) => Any) | undefined | null,      space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | : - An object to be converted. |
| replacer | ((key: string, value: Any) =&gt; Any) \| undefined \| null | 是 | A function that transforms the results. |
| space | int \| string | 否 | A string or number that's used to insert white space |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of Object, including annotated getter values |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

Converts an object to a JavaScript Object Notation (JSON) string,invoking any instance methods annotated with @JSONStringifyGetter and including their return values in the output. Each annotated method's name is used as the JSON key, and its return value is used as the corresponding value.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string--><!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | : - An object to be converted. |
| replacer | Array&lt;double \| string&gt; \| Array&lt;string&gt; \| Array&lt;double&gt; | 是 | An array with elements indicating names of the properties in the object that should be included in the resulting JSON string. Annotated getter methods whose names appear in this array are also included. |
| space | int \| string | 否 | A string or number that's used to insert white space |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | JSON representation of Object, including annotated getter values |

