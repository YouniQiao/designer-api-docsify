# XmlDynamicSerializer

XmlDynamicSerializer类用于动态生成XML字符串。当无法确定XML内容长度时，推荐使用该类。 > **说明：** > > 使用该类构造的对象无需自行创建ArrayBuffer，程序动态扩容，可以不断添加XML元素，最终序列化结果字符串长度上限为100000。

**起始版本：** 23

<!--Device-xml-class XmlDynamicSerializer--><!--Device-xml-class XmlDynamicSerializer-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## addEmptyElement

```TypeScript
addEmptyElement(name: string): void
```

写入一个空元素。 > **说明：** > > 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-addEmptyElement(name: string): void--><!--Device-XmlDynamicSerializer-addEmptyElement(name: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200064](../errorcode-utils.md#10200064-入参字符串不能为空) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.addEmptyElement("d");
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <d/>
```

## constructor

```TypeScript
constructor(encoding?: string)
```

构造并返回一个XmlDynamicSerializer对象，该对象支持动态扩容生成XML字符串，无需预先指定缓存大小。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-constructor(encoding?: string)--><!--Device-XmlDynamicSerializer-constructor(encoding?: string)-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| encoding | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [10200066](../errorcode-utils.md#10200066-编码格式错误) |

**示例**

```TypeScript
let serializer = new xml.XmlDynamicSerializer('utf-8');
```

## endElement

```TypeScript
endElement(): void
```

写入元素结束标记。 > **说明：** > > 调用该接口前必须先调用[startElement](arkts-arkts-xml-xmlserializer-c.md#startelement)接口写入元素开始标记。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-endElement(): void--><!--Device-XmlDynamicSerializer-endElement(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200065](../errorcode-utils.md#10200065-元素开始标记与元素结束标记未匹配使用) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>
```

## getOutput

```TypeScript
getOutput(): ArrayBuffer
```

返回XML字符串的ArrayBuffer。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-getOutput(): ArrayBuffer--><!--Device-XmlDynamicSerializer-getOutput(): ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| ArrayBuffer |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arr = serializer.getOutput();
let uint8 = new Uint8Array(arr);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>
```

## setAttributes

```TypeScript
setAttributes(name: string, value: string): void
```

写入元素的属性和属性值。 > **说明：** > > 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的属性名称以及添加多个同名的属性名称。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-setAttributes(name: string, value: string): void--><!--Device-XmlDynamicSerializer-setAttributes(name: string, value: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| value | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200063](../errorcode-utils.md#10200063-xml文件声明或属性位置设置错误) |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200064](../errorcode-utils.md#10200064-入参字符串不能为空) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setAttributes("importance", "high");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high"/>
```

## setCdata

```TypeScript
setCdata(text: string): void
```

提供在CDATA标签中添加数据的能力，所生成的CDATA标签结构为：`&lt;![CDATA[` + 所添加的数据 + `]]&gt;`。 > **说明：** > > 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许在CDATA标签中添加包含"\]\]\>"字符串的数据。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-setCdata(text: string): void--><!--Device-XmlDynamicSerializer-setCdata(text: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200064](../errorcode-utils.md#10200064-入参字符串不能为空) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setCdata('root SYSTEM')
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <![CDATA[root SYSTEM]]>
```

## setComment

```TypeScript
setComment(text: string): void
```

写入注释内容，所生成的注释结构为：`&lt;!--` + 注释内容 + `--&gt;`。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-setComment(text: string): void--><!--Device-XmlDynamicSerializer-setComment(text: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200064](../errorcode-utils.md#10200064-入参字符串不能为空) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setComment("Hello, World!");
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!--Hello, World!-->
```

## setDeclaration

```TypeScript
setDeclaration(): void
```

编写带有编码的文件声明，调用后将在XML文本中生成`&lt;?xml version="1.0" encoding="utf-8"?&gt;`格式的声明。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-setDeclaration(): void--><!--Device-XmlDynamicSerializer-setDeclaration(): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**错误码：**

| 错误码ID |
| --- |
| [10200063](../errorcode-utils.md#10200063-xml文件声明或属性位置设置错误) |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setDeclaration();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <?xml version="1.0" encoding="utf-8"?>
```

## setDocType

```TypeScript
setDocType(text: string): void
```

写入文档类型。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-setDocType(text: string): void--><!--Device-XmlDynamicSerializer-setDocType(text: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200064](../errorcode-utils.md#10200064-入参字符串不能为空) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setDocType('root SYSTEM "http://www.test.org/test.dtd"');
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!DOCTYPE root SYSTEM "http://www.test.org/test.dtd">
```

## setNamespace

```TypeScript
setNamespace(prefix: string, namespace: string): void
```

写入当前元素标记的命名空间。 > **说明：** > > 该接口应在[startElement](#startelement)之前调用，为即将开启的元素设置命名空间前缀。调用顺序： > 先调用setNamespace设置命名空间，再调用startElement开启元素。 > > 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的前缀以及对同一个元素设置多个命名空间。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-setNamespace(prefix: string, namespace: string): void--><!--Device-XmlDynamicSerializer-setNamespace(prefix: string, namespace: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |
| namespace | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200064](../errorcode-utils.md#10200064-入参字符串不能为空) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.setNamespace("h", "http://www.w3.org/TR/html4/");
serializer.startElement("note");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <h:note xmlns:h="http://www.w3.org/TR/html4/"/>
```

## setText

```TypeScript
setText(text: string): void
```

写入标签值。 > **说明：** > > 该接口必须在[startElement](#startelement)之后、 > [endElement](#endelement)之前调用，用于设置当前元素的文本内容。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-setText(text: string): void--><!--Device-XmlDynamicSerializer-setText(text: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| text | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200064](../errorcode-utils.md#10200064-入参字符串不能为空) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setAttributes("importance", "high");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high">Happy</note>
```

## startElement

```TypeScript
startElement(name: string): void
```

写入元素开始标记。 > **说明：** > > - 调用该接口后须调用[endElement](arkts-arkts-xml-xmlserializer-c.md#endelement)写入元素结束标记，以确保节点正确闭合。 > > - 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-XmlDynamicSerializer-startElement(name: string): void--><!--Device-XmlDynamicSerializer-startElement(name: string): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml的累积长度已超过上限) |
| [10200064](../errorcode-utils.md#10200064-入参字符串不能为空) |

**示例**

```TypeScript
import { util } from '@kit.ArkTS';

let serializer = new xml.XmlDynamicSerializer('utf-8');
serializer.startElement("note");
serializer.setText("Happy");
serializer.endElement();
let arrayBuffer = serializer.getOutput();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note>Happy</note>
```
