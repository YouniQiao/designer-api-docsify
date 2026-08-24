# JSON

表示JSON类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

<!--Device-unnamed-export class JSON--><!--Device-unnamed-export class JSON-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## parse

```TypeScript
parse<T>(text: string, type: Type): T | null | undefined
```

将JSON字符串解析为指定的类型。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parse<T>(text: string, type: Type): T | null | undefined--><!--Device-JSON-parse<T>(text: string, type: Type): T | null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待解析的JSON字符串。 |
| type | [Type](arkts-arkts-util-type-e.md) | 是 | 解析的目标类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| null \| undefined | 解析得到的对象。 |

## parse

```TypeScript
parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,
        options?: jsonx.ParseOptions): T | null | undefined
```

使用reviver函数将JSON字符串解析为指定的类型。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,        options?: jsonx.ParseOptions): T | null | undefined--><!--Device-JSON-parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,        options?: jsonx.ParseOptions): T | null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待解析的JSON字符串。 |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | 是 | 用于转换值的函数。 |
| type | [Type](arkts-arkts-util-type-e.md) | 是 | 解析的目标类型。 |
| options | jsonx.ParseOptions | 否 | 解析选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| null \| undefined | 解析得到的对象。 |

## parse

```TypeScript
parse<T>(json: string, type: Class): T | null | undefined
```

将JSON字符串解析为指定的类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parse<T>(json: string, type: Class): T | null | undefined--><!--Device-JSON-parse<T>(json: string, type: Class): T | null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| json | string | 是 | 待解析的JSON字符串。 |
| type | [Class](arkts-arkts-class-c.md) | 是 | 解析的目标类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| null \| undefined | 解析得到的对象。 |

## parse

```TypeScript
parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,
        options?: jsonx.ParseOptions): T | null | undefined
```

使用reviver函数将JSON字符串解析为指定的类。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,        options?: jsonx.ParseOptions): T | null | undefined--><!--Device-JSON-parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,        options?: jsonx.ParseOptions): T | null | undefined-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| json | string | 是 | 待解析的JSON字符串。 |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | 是 | 用于转换值的函数。 |
| type | [Class](arkts-arkts-class-c.md) | 是 | 解析的目标类。 |
| options | jsonx.ParseOptions | 否 | 解析选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T \| null \| undefined | 解析得到的对象。 |

## parseJsonArray

```TypeScript
public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>
```

解析JSON对象字符串并返回Array。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>--><!--Device-JSON-public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待解析的JSON字符串。 |
| options | jsonx.ParseOptions | 否 | BigInt解析选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[JsonRecordType](arkts-arkts-jsonrecordtype-t.md)&gt; | 解析得到的Array对象。 |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement
```

解析JSON字符串并返回JsonElement。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement--><!--Device-JSON-parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待解析的JSON字符串。 |
| options | jsonx.ParseOptions | 否 | BigInt解析选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| jsonx.JsonElement | 解析得到的JSON元素。 |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,
        options?: jsonx.ParseOptions): jsonx.JsonElement
```

使用reviver函数解析JSON字符串并返回JsonElement。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,        options?: jsonx.ParseOptions): jsonx.JsonElement--><!--Device-JSON-parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,        options?: jsonx.ParseOptions): jsonx.JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待解析的JSON字符串。 |
| reviver | (key: string, value: jsonx.JsonElement) =&gt; jsonx.JsonElement | 是 | 用于转换值的函数。 |
| options | jsonx.ParseOptions | 否 | BigInt解析选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| jsonx.JsonElement | 解析得到的JSON元素。 |

## parseJsonRecord

```TypeScript
public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>
```

解析JSON对象字符串并返回Record。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>--><!--Device-JSON-public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 待解析的JSON字符串。 |
| options | jsonx.ParseOptions | 否 | BigInt解析选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record&lt;string, [JsonRecordType](arkts-arkts-jsonrecordtype-t.md)&gt; | 解析得到的Record对象。 |

## parseUpdate

```TypeScript
parseUpdate<T>(json: string, instance: T): T
```

解析JSON字符串，并填充已有实例的字段。 与parse&lt;T&gt;(json, type)不同，该方法不要求类型具有默认构造函数。 JSON中不存在对应键的字段将保留实例上的当前值 （合并语义）。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parseUpdate<T>(json: string, instance: T): T--><!--Device-JSON-parseUpdate<T>(json: string, instance: T): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| json | string | 是 | 待解析的JSON字符串。 |
| instance | T | 是 | 字段将被填充的已有实例。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 填充字段后的同一实例。 |

## parseUpdate

```TypeScript
parseUpdate<T>(
        json: string,
        reviver: ((key: string, value: Any) => Any) | undefined,
        instance: T,
        options?: jsonx.ParseOptions
    ): T
```

解析JSON字符串并填充已有实例的字段， 可选传入reviver函数和解析选项。 与parse&lt;T&gt;(json, type)不同，该方法不要求类型具有默认构造函数。 JSON中不存在对应键的字段将保留实例上的当前值 （合并语义）。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-parseUpdate<T>(        json: string,        reviver: ((key: string, value: Any) => Any) | undefined,        instance: T,        options?: jsonx.ParseOptions    ): T--><!--Device-JSON-parseUpdate<T>(        json: string,        reviver: ((key: string, value: Any) => Any) | undefined,        instance: T,        options?: jsonx.ParseOptions    ): T-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| json | string | 是 | 待解析的JSON字符串。 |
| reviver | ((key: string, value: Any) =&gt; Any) \| undefined | 是 | 用于转换每个解析值的可选函数，也可传入undefined。 |
| instance | T | 是 | 字段将被填充的已有实例。 |
| options | jsonx.ParseOptions | 否 | 可选的ParseOptions（例如bigIntMode）。如果不传入， 则采用默认的解析选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 填充字段后的同一实例。 |

## stringify

```TypeScript
stringify(d: byte): string
```

将byte值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: byte): string--><!--Device-JSON-stringify(d: byte): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | byte | 是 | 待转换为JSON中Number的byte值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该byte值的JSON表示。 |

## stringify

```TypeScript
stringify(d: char): string
```

将char值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: char): string--><!--Device-JSON-stringify(d: char): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | char | 是 | 待转换为JSON中string的char值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该char值的JSON表示。 |

## stringify

```TypeScript
stringify(d: short): string
```

将short值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: short): string--><!--Device-JSON-stringify(d: short): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | short | 是 | 待转换为JSON中Number的short值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该short值的JSON表示。 |

## stringify

```TypeScript
stringify(d: int): string
```

将int值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: int): string--><!--Device-JSON-stringify(d: int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | int | 是 | 待转换为JSON中Number的int值。 <br>取值约束：应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该int值的JSON表示。 |

## stringify

```TypeScript
stringify(d: long): string
```

将long值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: long): string--><!--Device-JSON-stringify(d: long): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | long | 是 | 待转换为JSON中Number的long值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该long值的JSON表示。 |

## stringify

```TypeScript
stringify(d: float): string
```

将float值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: float): string--><!--Device-JSON-stringify(d: float): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | float | 是 | 待转换为JSON中Number的float值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该float值的JSON表示。 |

## stringify

```TypeScript
stringify(d: double): string
```

将double值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: double): string--><!--Device-JSON-stringify(d: double): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | double | 是 | 待转换为JSON中Number的double值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该double值的JSON表示。 |

## stringify

```TypeScript
stringify(d: bigint): string
```

将bigint值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: bigint): string--><!--Device-JSON-stringify(d: bigint): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | bigint | 是 | 待转换为JSON中Number的bigint值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该bigint值的JSON表示。 |

## stringify

```TypeScript
stringify(d: boolean): string
```

将boolean值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: boolean): string--><!--Device-JSON-stringify(d: boolean): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | boolean | 是 | 待转换为JSON中Boolean字面量的boolean值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该boolean值的JSON表示。 |

## stringify

```TypeScript
stringify(d: string): string
```

将字符串转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: string): string--><!--Device-JSON-stringify(d: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | string | 是 | 待转换为JSON中string的字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该字符串的JSON表示。 |

## stringify

```TypeScript
stringify(d: FixedArray<byte>): string
```

将byte数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<byte>): string--><!--Device-JSON-stringify(d: FixedArray<byte>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;byte&gt; | 是 | 待转换为JSON中Number数组的byte数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该byte数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: FixedArray<char>): string
```

将char数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<char>): string--><!--Device-JSON-stringify(d: FixedArray<char>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;char&gt; | 是 | 待转换为JSON中String数组的char数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该char数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: FixedArray<short>): string
```

将short数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<short>): string--><!--Device-JSON-stringify(d: FixedArray<short>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;short&gt; | 是 | 待转换为JSON中Number数组的short数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该short数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: FixedArray<int>): string
```

将int数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<int>): string--><!--Device-JSON-stringify(d: FixedArray<int>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;int&gt; | 是 | 待转换为JSON中Number数组的int数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该int数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: FixedArray<long>): string
```

将long数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<long>): string--><!--Device-JSON-stringify(d: FixedArray<long>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;long&gt; | 是 | 待转换为JSON中Number数组的long数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该long数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: FixedArray<float>): string
```

将float数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<float>): string--><!--Device-JSON-stringify(d: FixedArray<float>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;float&gt; | 是 | 待转换为JSON中Number数组的float数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该float数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: FixedArray<double>): string
```

将double数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<double>): string--><!--Device-JSON-stringify(d: FixedArray<double>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;double&gt; | 是 | 待转换为JSON中Number数组的double数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该double数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: FixedArray<boolean>): string
```

将boolean数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: FixedArray<boolean>): string--><!--Device-JSON-stringify(d: FixedArray<boolean>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | FixedArray&lt;boolean&gt; | 是 | 待转换为JSON中Boolean字面量数组的boolean数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该boolean数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: Array<Double>): string
```

将Double数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: Array<Double>): string--><!--Device-JSON-stringify(d: Array<Double>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | Array&lt;Double&gt; | 是 | 待转换的Double数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该数组的JSON表示。 |

## stringify

```TypeScript
stringify(d: ArrayLike<Double>): string
```

将Double ArrayLike对象转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(d: ArrayLike<Double>): string--><!--Device-JSON-stringify(d: ArrayLike<Double>): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | ArrayLike&lt;Double&gt; | 是 | 待转换的Double ArrayLike对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该ArrayLike对象的JSON表示。 |

## stringify

```TypeScript
stringify(obj: JsonReplacer): string
```

将JsonReplacer转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: JsonReplacer): string--><!--Device-JSON-stringify(obj: JsonReplacer): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | [JsonReplacer](arkts-arkts-json-jsonreplacer-i.md) | 是 | 待转换的JsonReplacer对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 对应的JSON表示。 |

## stringify

```TypeScript
stringify(obj: Any): string
```

将对象转换为JavaScript对象表示法（JSON）字符串。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: Any): string--><!--Device-JSON-stringify(obj: Any): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | 待转换的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该对象的JSON表示。 |

## stringify

```TypeScript
stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string
```

将对象转换为JavaScript对象表示法（JSON）字符串。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string--><!--Device-JSON-stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | 待转换的对象。 |
| replacer | ((key: string, value: Any) =&gt; Any) \| undefined \| null | 是 | 用于转换结果的函数。 |
| space | string \| int | 否 | 如果space为字符串，则将该字符串用作每一级的缩进字符； 如果space为整数，则使用指定数量（最多10个）的空格进行 缩进；如果不传入该参数，则不做格式化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该对象的JSON表示。 |

## stringify

```TypeScript
stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string
```

将对象转换为JavaScript对象表示法（JSON）字符串。

**起始版本：** 24

**ArkTS模式：** ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string--><!--Device-JSON-stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | 待转换的对象。 |
| replacer | FixedArray&lt;double \| string&gt; | 是 | 待包含的属性名称数组。 |
| space | int \| string | 否 | 如果space为字符串，则将该字符串用作每一级的缩进字符； 如果space为整数，则使用指定数量（最多10个）的空格进行 缩进；如果不传入该参数，则不做格式化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该对象的JSON表示。 |

## stringify

```TypeScript
stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

将对象转换为JavaScript对象表示法（JSON）字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string--><!--Device-JSON-stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | 待转换的对象。 |
| replacer | Array&lt;double \| string&gt; \| Array&lt;string&gt; \| Array&lt;double&gt; | 是 | 待包含的属性 名称数组。<br>**起始版本：** 26.0.0 |
| space | int \| string | 否 | 用于缩进的字符串或number值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该对象的JSON表示。 |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string
```

将JsonElementSerializable转换为JSON字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elem | jsonx.JsonElementSerializable | 是 | 待序列化为字符串的JsonElementDeserializable。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 对应的JSON字符串。 |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],
        space?: int | string): string
```

使用自定义格式将JsonElementSerializable转换为JSON字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],        space?: int | string): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],        space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elem | jsonx.JsonElementSerializable | 是 | 待序列化为字符串的JsonElementSerializable。 |
| replacer | (double \| string)[] | 否 | 包含若干元素的数组，用于指明需要包含的属性名。 |
| space | int \| string | 否 | 用于空白缩进的字符串或number值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 对应的JSON字符串。 |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement): string
```

将JsonElement转换为JSON字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elem | jsonx.JsonElement | 是 | 待序列化为字符串的JsonElement。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 对应的JSON字符串。 |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],
        space?: int | string): string
```

使用自定义格式将JsonElement转换为JSON字符串。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],        space?: int | string): string--><!--Device-JSON-public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],        space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elem | jsonx.JsonElement | 是 | 待序列化为字符串的JsonElement。 |
| replacer | (double \| string)[] | 否 | 包含若干元素的数组，用于指明需要包含的属性名。 |
| space | int \| string | 否 | 用于空白缩进的字符串或number值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 对应的JSON字符串。 |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(obj: Any): string
```

将对象转换为JavaScript对象表示法（JSON）字符串， 过程中会调用所有带@JSONStringifyGetter注解的实例方法， 并将其返回值写入输出。每个带注解方法的名称 作为JSON的键，其返回值作为对应的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringifyWithGetters(obj: Any): string--><!--Device-JSON-stringifyWithGetters(obj: Any): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | : - 待转换的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该对象的JSON表示，其中包含带注解getter方法的返回值。 |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: ((key: string, value: Any) => Any) | undefined | null,
      space?: int | string): string
```

将对象转换为JavaScript对象表示法（JSON）字符串， 过程中会调用所有带@JSONStringifyGetter注解的实例方法， 并将其返回值写入输出。每个带注解方法的名称 作为JSON的键，其返回值作为对应的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: ((key: string, value: Any) => Any) | undefined | null,      space?: int | string): string--><!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: ((key: string, value: Any) => Any) | undefined | null,      space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | : - 待转换的对象。 |
| replacer | ((key: string, value: Any) =&gt; Any) \| undefined \| null | 是 | 用于转换结果的函数。 |
| space | int \| string | 否 | 用于插入空白的字符串或number值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该对象的JSON表示，其中包含带注解getter方法的返回值。 |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

将对象转换为JavaScript对象表示法（JSON）字符串， 过程中会调用所有带@JSONStringifyGetter注解的实例方法， 并将其返回值写入输出。每个带注解方法的名称 作为JSON的键，其返回值作为对应的值。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string--><!--Device-JSON-stringifyWithGetters(      obj: Any,      replacer: Array<double | string> | Array<string> | Array<double>,      space?: int | string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Any | 是 | : - 待转换的对象。 |
| replacer | Array&lt;double \| string&gt; \| Array&lt;string&gt; \| Array&lt;double&gt; | 是 | 包含若干元素的数组，这些元素 指明对象中需要包含在最终JSON 字符串里的属性名。 名称出现在该数组中的带注解getter方法也会被包含。 |
| space | int \| string | 否 | 用于插入空白的字符串或number值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 该对象的JSON表示，其中包含带注解getter方法的返回值。 |

