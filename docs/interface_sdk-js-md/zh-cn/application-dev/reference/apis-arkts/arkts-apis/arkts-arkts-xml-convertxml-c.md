# ConvertXML

ConvertXML类提供将XML文本转换为JavaScript对象的能力。 推荐使用[fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](#fastconverttojsobject)进行常规XML文本解析， 当单元素文本内容超过10M时推荐使用[largeConvertToJSObject&lt;sup&gt;23+&lt;/sup&gt;](#largeconverttojsobject)。 已废弃的[convertToJSObject](#converttojsobject)和[convert](#convert)方法不再维护， 建议使用[fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](#fastconverttojsobject)替代。

**起始版本：** 8

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { convertxml } from 'kits/@kit.ArkTS';
```

## convert

```TypeScript
convert(xml: string, options?: ConvertOptions): Object
```

将XML文本转换为Object类型对象。

> **说明：**&gt;
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](#fastconverttojsobject)替代。&gt;
> 在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [fastConvertToJSObject](#fastconverttojsobject)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [xml](arkts-convertxml.md) | string | 是 |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Object |

## convertToJSObject

```TypeScript
convertToJSObject(xml: string, options?: ConvertOptions): Object
```

将XML文本转换为Object类型对象，适用于XML配置文件解析、数据格式转换等场景。该方法将XML文本解析为层级嵌套结构，各XML组件按ConvertOptions中配置的键名映射为对象的属性。

> **说明：**&gt;
> 从API version 9开始支持，从API version 14开始废弃，建议使用
> [fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](#fastconverttojsobject)替代。&gt;
> 在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

**起始版本：** 9

**废弃版本：** 14

**替代接口：** [fastConvertToJSObject](#fastconverttojsobject)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [xml](arkts-convertxml.md) | string | 是 |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Object |

**错误码：**

| 错误码ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-参数解析错误) |

## fastConvertToJSObject

```TypeScript
fastConvertToJSObject(xml: string, options?: ConvertOptions): Object
```

将XML文本转换为Object类型对象，适用于XML配置文件解析、数据报文处理等场景。该方法将XML文本解析为层级嵌套结构，各XML组件按ConvertOptions中配置的键名映射为对象的属性。 当单元素文本内容超过10M时，建议使用[largeConvertToJSObject&lt;sup&gt;23+&lt;/sup&gt;](#largeconverttojsobject)替代。

> **说明：**&gt;
> 该接口无法满足解析单元素文本内容超过10M的XML文件，当单元素文本内容超过10M时，会输出异常日志信息并返回一个仅包含XML声明的基础Object对象。
> 如需解析单元素文本内容超过10M的XML文本，建议使用[largeConvertToJSObject&lt;sup&gt;23+&lt;/sup&gt;](#largeconverttojsobject)
> 替代。&gt;
> 在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。fastConvertToJSObject接口转换后的对象以换行符（LF）表示换行。

**起始版本：** 14

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [xml](arkts-convertxml.md) | string | 是 |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Object |

**错误码：**

| 错误码ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-参数解析错误) |

## largeConvertToJSObject

```TypeScript
largeConvertToJSObject(xml: string, options?: ConvertOptions): Object
```

将XML文本转换为Object类型对象，适用于XML日志文件、数据报文等大型XML解析场景。此方法支持解析单元素大小超过10M的大型XML文本，针对大文本场景进行了优化，可有效避免单元素文本过大导致的解析异常。 当[fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](#fastconverttojsobject)因单元素文本内容超过10M无法正常解析时， 可使用本方法作为替代方案。

> **说明：**&gt;
> 当传入的XML文本无法正确解析为Object类型对象时，输出异常日志信息并返回一个仅包含XML声明的基础Object对象。&gt;
> 在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [xml](arkts-convertxml.md) | string | 是 |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Object |

**错误码：**

| 错误码ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-参数解析错误) |
