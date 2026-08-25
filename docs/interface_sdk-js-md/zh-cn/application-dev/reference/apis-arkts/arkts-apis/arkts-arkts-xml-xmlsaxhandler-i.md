# XmlSAXHandler

XmlSAXHandler定义了SAX解析xml文本时的回调方法。开发者需要实现这些回调方法来处理xml文本的不同部分。这些回调方法会在xml解析过程的对应时机触发。startDocument会在开始解析文档时触发， endDocument会在结束文档解析时触发，startElement会在开始解析元素时触发，endElement会在结束解析元素时触发，characters则会在解析元素间文本内容时触发。

**起始版本：** 24

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## characters

```TypeScript
characters(content: string): void
```

当解析器在XML元素内部遇到文本内容时调用的回调函数。该回调函数需要开发者自行实现。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| content | string | 是 |

## endDocument

```TypeScript
endDocument(): void
```

当解析器在XML文本结束解析时触发的回调函数。该回调函数需要开发者自行实现。具体使用示例可见[characters&lt;sup&gt;24+&lt;/sup&gt;](#characters)。

> **说明：**&gt;
> 当可读流结束时触发此回调。在stream中调用push()，传入null值，从而触发该回调。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## endElement

```TypeScript
endElement(elementName: string, namespaceURI: string | undefined, qName: string | undefined): void
```

当解析器遇到XML元素的结束标签时触发的回调函数。该回调函数需要开发者自行实现。具体使用示例可见[characters&lt;sup&gt;24+&lt;/sup&gt;](#characters)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | string | 是 |
| namespaceURI | string \| undefined | 是 |
| qName | string \| undefined | 是 |

## startDocument

```TypeScript
startDocument(): void
```

当解析器在XML文本开始解析时触发的回调函数。该回调函数需要开发者自行实现。具体使用示例可见[characters&lt;sup&gt;24+&lt;/sup&gt;](#characters)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

## startElement

```TypeScript
startElement(elementName: string, namespaceURI: string | undefined, qName: string | undefined, attributes: Map<string,string>): void
```

当解析器遇到XML元素的开始标签时触发的回调函数。该回调函数需要开发者自行实现。具体使用示例可见[characters&lt;sup&gt;24+&lt;/sup&gt;](#characters)。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementName | string | 是 |
| namespaceURI | string \| undefined | 是 |
| qName | string \| undefined | 是 |
| attributes | Map & lt;string, string & gt; | 是 |
