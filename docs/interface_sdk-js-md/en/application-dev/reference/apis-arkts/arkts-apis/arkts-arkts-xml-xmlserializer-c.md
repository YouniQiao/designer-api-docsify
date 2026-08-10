# XmlSerializer

XmlSerializer接口用于生成XML文件。该接口基于预分配的ArrayBuffer缓存区域，通过顺序调用元素写入方法（如startElement、setAttributes、setText和endElement）将XML文本写入缓存。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-xml-class XmlSerializer--><!--Device-xml-class XmlSerializer-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## addEmptyElement

```TypeScript
addEmptyElement(name: string): void
```

添加一个空元素。

> **说明：**
> 
> 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。例如不允许添加数字开头的元素名称。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-addEmptyElement(name: string): void--><!--Device-XmlSerializer-addEmptyElement(name: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 元素的名称，取值原则：不允许以数字开头。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.addEmptyElement("d");
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <d/>
```

## constructor

```TypeScript
constructor(buffer: ArrayBuffer | DataView, encoding?: string)
```

构造并返回一个XmlSerializer对象，用于将XML信息写入指定的ArrayBuffer或DataView内存中。

> **说明：**
> 
> buffer是开发者根据需要自定义大小的缓冲区，用于临时存储生成的XML文本。在使用过程中必须确保缓冲区足以容纳生成的文本内容。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-constructor(buffer: ArrayBuffer | DataView, encoding?: string)--><!--Device-XmlSerializer-constructor(buffer: ArrayBuffer | DataView, encoding?: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| DataView | Yes | 用于接收写入XML信息的ArrayBuffer或DataView内存，需确保缓存区域足以容纳生成的文本内容。 |
| encoding | string | No | 编码格式，默认'utf-8'（目前仅支持'utf-8'）。 |

## Examples

```TypeScript
let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer, "utf-8");
```

## endElement

```TypeScript
endElement(): void
```

添加元素结束标记。

> **说明：**
> 
> 调用该接口前必须先调用[startElement](arkts-arkts-xml-xmlserializer-c.md#startelement)接口写入元素开始标记。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-endElement(): void--><!--Device-XmlSerializer-endElement(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <note>Happy</note>
```

## setAttributes

```TypeScript
setAttributes(name: string, value: string): void
```

添加元素的属性和属性值。

> **说明：**
> 
> 该接口必须在[startElement](arkts-arkts-xml-xmlserializer-c.md#startelement)之后调用，用于为当前已开启的元素设置属性。在元素开始标记写入之前调用此接口将产生无效XML。
> 
> 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。例如不允许添加数字开头的属性名称以及添加多个同名的属性名称。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-setAttributes(name: string, value: string): void--><!--Device-XmlSerializer-setAttributes(name: string, value: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | XML元素的属性名称。 |
| value | string | Yes | XML元素的属性值，与name参数指定的属性名对应。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setAttributes("importance", "high");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high"/>
```

## setCDATA

```TypeScript
setCDATA(text: string): void
```

提供在CDATA标签中添加数据的能力，适用于XML内容中包含特殊字符（如&lt;、&等）需要原样保留而不被XML解析器处理的场景。所生成的CDATA标签结构为：`<![CDATA[` + 所添加的数据 + `]]>`。

&gt;&lt;![CDATA[` + 所添加的数据 + `]]&gt;`。

> **说明：**
> 
> 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。例如不允许在CDATA标签中添加包含"\]\]\>"字符串的数据。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-setCDATA(text: string): void--><!--Device-XmlSerializer-setCDATA(text: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | CDATA标签中的数据内容。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setCDATA('root SYSTEM')
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <![CDATA[root SYSTEM]]>
```

## setComment

```TypeScript
setComment(text: string): void
```

添加注释内容，所生成的注释结构为：`&lt;!--` + 注释内容 + `--&gt;`。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-setComment(text: string): void--><!--Device-XmlSerializer-setComment(text: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | 当前元素的注释内容。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setComment("Hello, World!");
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!--Hello, World!-->
```

## setDeclaration

```TypeScript
setDeclaration(): void
```

设置带有编码信息的文件声明，调用后将在XML文本中生成`&lt;?xml version="1.0" encoding="utf-8"?&gt;`格式的声明。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-setDeclaration(): void--><!--Device-XmlSerializer-setDeclaration(): void-End-->

**System capability:** SystemCapability.Utils.Lang

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setDeclaration();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <?xml version="1.0" encoding="utf-8"?>
```

## setDocType

```TypeScript
setDocType(text: string): void
```

添加文档类型。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-setDocType(text: string): void--><!--Device-XmlSerializer-setDocType(text: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | DocType属性的内容。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setDocType('root SYSTEM "http://www.test.org/test.dtd"');
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <!DOCTYPE root SYSTEM "http://www.test.org/test.dtd">
```

## setNamespace

```TypeScript
setNamespace(prefix: string, namespace: string): void
```

添加当前元素标记的命名空间，适用于需要在同一XML文档中区分来自不同词汇表或模式的元素的场景，如混合使用多个XML标准的文档。

> **说明：**
> 
> 该接口应在[startElement](arkts-arkts-xml-xmlserializer-c.md#startelement)之前调用，为即将开启的元素设置命名空间前缀。调用顺序：先调用setNamespace设置命名空间，再调用startElement开启元素。
> 
> 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。例如禁止添加数字开头的前缀以及为同一个元素设置多个命名空间。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-setNamespace(prefix: string, namespace: string): void--><!--Device-XmlSerializer-setNamespace(prefix: string, namespace: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| prefix | string | Yes | 当前元素及其子元素的前缀。 |
| namespace | string | Yes | 当前元素及其子元素的命名空间。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.setNamespace("h", "http://www.w3.org/TR/html4/");
thatSer.startElement("note");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <h:note xmlns:h="http://www.w3.org/TR/html4/"/>
```

## setText

```TypeScript
setText(text: string): void
```

添加标签值，标签值将作为当前元素的文本内容，写入元素的开始标记与结束标记之间。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-setText(text: string): void--><!--Device-XmlSerializer-setText(text: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | XML元素的标签文本内容。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setAttributes("importance", "high");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result); // <note importance="high">Happy</note>
```

## startElement

```TypeScript
startElement(name: string): void
```

根据给定名称添加元素开始标记。

> **说明：**
> 
> - 调用该接口后须调用[endElement](arkts-arkts-xml-xmlserializer-c.md#endelement)写入元素结束标记，以确保节点正确闭合。
> 
> - 该接口对所添加数据不做标准XML校验处理，请确保所添加的数据符合标准XML规范。比如不允许添加数字开头的元素名称。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlSerializer-startElement(name: string): void--><!--Device-XmlSerializer-startElement(name: string): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 当前元素的元素名。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer);
thatSer.startElement("note");
thatSer.setText("Happy");
thatSer.endElement();
let uint8 = new Uint8Array(arrayBuffer);
let result = util.TextDecoder.create().decodeToString(uint8);
console.info(result);
// <note>Happy</note>
```

