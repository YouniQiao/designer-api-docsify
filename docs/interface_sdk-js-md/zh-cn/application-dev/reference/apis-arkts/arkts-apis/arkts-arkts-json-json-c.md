# JSON

表示JSON类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| type | [Type](arkts-arkts-util-type-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T \| null \| undefined |

## parse

```TypeScript
parse<T>(text: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Type,
        options?: jsonx.ParseOptions): T | null | undefined
```

使用reviver函数将JSON字符串解析为指定的类型。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| reviver | ((key: string, value: Any) = & gt; Any) \ | undefined | 是 |
| type | [Type](arkts-arkts-util-type-e.md) | 是 |
| options | jsonx.ParseOptions | 否 |

**返回值：**

| 类型 |
| --- |
| T \| null \| undefined |

## parse

```TypeScript
parse<T>(json: string, type: Class): T | null | undefined
```

将JSON字符串解析为指定的类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [json](arkts-util-json.md) | string | 是 |
| type | [Class](arkts-arkts-class-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| T \| null \| undefined |

## parse

```TypeScript
parse<T>(json: string, reviver: ((key: string, value: Any) => Any) | undefined, type: Class,
        options?: jsonx.ParseOptions): T | null | undefined
```

使用reviver函数将JSON字符串解析为指定的类。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [json](arkts-util-json.md) | string | 是 |
| reviver | ((key: string, value: Any) = & gt; Any) \ | undefined | 是 |
| type | [Class](arkts-arkts-class-c.md) | 是 |
| options | jsonx.ParseOptions | 否 |

**返回值：**

| 类型 |
| --- |
| T \| null \| undefined |

## parseJsonArray

```TypeScript
public static parseJsonArray(text: string, options?: jsonx.ParseOptions): Array<JsonRecordType>
```

解析JSON对象字符串并返回Array。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| options | jsonx.ParseOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Array&lt;[JsonRecordType](arkts-arkts-jsonrecordtype-t.md)&gt; |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, options?: jsonx.ParseOptions): jsonx.JsonElement
```

解析JSON字符串并返回JsonElement。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| options | jsonx.ParseOptions | 否 |

**返回值：**

| 类型 |
| --- |
| jsonx.JsonElement |

## parseJsonElement

```TypeScript
parseJsonElement(text: string, reviver: (key: string, value: jsonx.JsonElement) => jsonx.JsonElement,
        options?: jsonx.ParseOptions): jsonx.JsonElement
```

使用reviver函数解析JSON字符串并返回JsonElement。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| reviver | (key: string, value: jsonx.JsonElement) = & gt; jsonx.JsonElement | 是 |
| options | jsonx.ParseOptions | 否 |

**返回值：**

| 类型 |
| --- |
| jsonx.JsonElement |

## parseJsonRecord

```TypeScript
public static parseJsonRecord(text: string, options?: jsonx.ParseOptions): Record<string, JsonRecordType>
```

解析JSON对象字符串并返回Record。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |
| options | jsonx.ParseOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Record&lt;string, [JsonRecordType](arkts-arkts-jsonrecordtype-t.md)&gt; |

## parseUpdate

```TypeScript
parseUpdate<T>(json: string, instance: T): T
```

解析JSON字符串，并填充已有实例的字段。 与parse&lt;T&gt;(json, type)不同，该方法不要求类型具有默认构造函数。 JSON中不存在对应键的字段将保留实例上的当前值 （合并语义）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [json](arkts-util-json.md) | string | 是 |
| instance | T | 是 |

**返回值：**

| 类型 |
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

解析JSON字符串并填充已有实例的字段， 可选传入reviver函数和解析选项。 与parse&lt;T&gt;(json, type)不同，该方法不要求类型具有默认构造函数。 JSON中不存在对应键的字段将保留实例上的当前值 （合并语义）。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [json](arkts-util-json.md) | string | 是 |
| reviver | ((key: string, value: Any) = & gt; Any) \ | undefined | 是 |
| instance | T | 是 |
| options | jsonx.ParseOptions | 否 |

**返回值：**

| 类型 |
| --- |
| T |

## stringify

```TypeScript
stringify(d: byte): string
```

将byte值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | byte | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: char): string
```

将char值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | char | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: short): string
```

将short值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | short | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: int): string
```

将int值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | int | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: long): string
```

将long值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | long | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: float): string
```

将float值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | float | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: double): string
```

将double值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | double | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: bigint): string
```

将bigint值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | bigint | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: boolean): string
```

将boolean值转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: string): string
```

将字符串转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<byte>): string
```

将byte数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;byte & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<char>): string
```

将char数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;char & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<short>): string
```

将short数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;short & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<int>): string
```

将int数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;int & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<long>): string
```

将long数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;long & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<float>): string
```

将float数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;float & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<double>): string
```

将double数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;double & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: FixedArray<boolean>): string
```

将boolean数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | FixedArray & lt;boolean & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: Array<Double>): string
```

将Double数组转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | Array & lt;Double & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(d: ArrayLike<Double>): string
```

将Double ArrayLike对象转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [d](arkts-arkts-math-decimal-decimal-c.md) | ArrayLike & lt;Double & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: JsonReplacer): string
```

将JsonReplacer转换为JSON格式。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | [JsonReplacer](arkts-arkts-json-jsonreplacer-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: Any): string
```

将对象转换为JavaScript对象表示法（JSON）字符串。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Any | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: Any, replacer: ((key: string, value: Any) => Any) | undefined | null, space?: string | int): string
```

将对象转换为JavaScript对象表示法（JSON）字符串。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Any | 是 |
| replacer | ((key: string, value: Any) = & gt; Any) \ | undefined \| null | 是 |
| space | string \| int | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: Any, replacer: FixedArray<double | string>, space?: int | string): string
```

将对象转换为JavaScript对象表示法（JSON）字符串。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Any | 是 |
| replacer | FixedArray & lt;double \ | string & gt; | 是 |
| space | int \| string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## stringify

```TypeScript
stringify(obj: Any, replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

将对象转换为JavaScript对象表示法（JSON）字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Any | 是 |
| replacer | Array & lt;double \ | string & gt; \ | Array & lt;string & gt; \ | Array & lt;double & gt; | 是 |
| space | int \| string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable): string
```

将JsonElementSerializable转换为JSON字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elem | jsonx.JsonElementSerializable | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElementSerializable, replacer?: (double | string)[],
        space?: int | string): string
```

使用自定义格式将JsonElementSerializable转换为JSON字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elem | jsonx.JsonElementSerializable | 是 |
| replacer | (double \| string)[] | 否 |
| space | int \| string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement): string
```

将JsonElement转换为JSON字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elem | jsonx.JsonElement | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringifyJsonElement

```TypeScript
public static stringifyJsonElement(elem: jsonx.JsonElement, replacer?: (double | string)[],
        space?: int | string): string
```

使用自定义格式将JsonElement转换为JSON字符串。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elem | jsonx.JsonElement | 是 |
| replacer | (double \| string)[] | 否 |
| space | int \| string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(obj: Any): string
```

将对象转换为JavaScript对象表示法（JSON）字符串， 过程中会调用所有带@JSONStringifyGetter注解的实例方法， 并将其返回值写入输出。每个带注解方法的名称 作为JSON的键，其返回值作为对应的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Any | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: ((key: string, value: Any) => Any) | undefined | null,
      space?: int | string): string
```

将对象转换为JavaScript对象表示法（JSON）字符串， 过程中会调用所有带@JSONStringifyGetter注解的实例方法， 并将其返回值写入输出。每个带注解方法的名称 作为JSON的键，其返回值作为对应的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Any | 是 |
| replacer | ((key: string, value: Any) = & gt; Any) \ | undefined \| null | 是 |
| space | int \| string | 否 |

**返回值：**

| 类型 |
| --- |
| string |

## stringifyWithGetters

```TypeScript
stringifyWithGetters(
      obj: Any,
      replacer: Array<double | string> | Array<string> | Array<double>,
      space?: int | string): string
```

将对象转换为JavaScript对象表示法（JSON）字符串， 过程中会调用所有带@JSONStringifyGetter注解的实例方法， 并将其返回值写入输出。每个带注解方法的名称 作为JSON的键，其返回值作为对应的值。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Any | 是 |
| replacer | Array & lt;double \ | string & gt; \ | Array & lt;string & gt; \ | Array & lt;double & gt; | 是 |
| space | int \| string | 否 |

**返回值：**

| 类型 |
| --- |
| string |
