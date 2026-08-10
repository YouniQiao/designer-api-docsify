# ConvertXML

ConvertXML类提供将XML文本转换为JavaScript对象的能力。推荐使用[fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](arkts-arkts-xml-convertxml-c.md#fastconverttojsobject)进行常规XML文本解析，当单元素文本内容超过10M时推荐使用[largeConvertToJSObject&lt;sup&gt;23+&lt;/sup&gt;](arkts-arkts-xml-convertxml-c.md#largeconverttojsobject)。已废弃的[convertToJSObject](arkts-arkts-xml-convertxml-c.md#converttojsobject)和[convert](arkts-arkts-xml-convertxml-c.md#convert)方法不再维护，建议使用[fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](arkts-arkts-xml-convertxml-c.md#fastconverttojsobject)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-xml-class ConvertXML--><!--Device-xml-class ConvertXML-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { convertxml } from 'kits/@kit.ArkTS';
```

## convert

```TypeScript
convert(xml: string, options?: ConvertOptions): Object
```

将XML文本转换为Object类型对象。

> **说明：**
> 
> 从API version 8开始支持，从API version 9开始废弃，建议使用
> [fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](arkts-arkts-xml-convertxml-c.md#fastconverttojsobject)替代。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [xml.ConvertXML#fastConvertToJSObject](arkts-arkts-xml-convertxml-c.md#fastconverttojsobject)

<!--Device-ConvertXML-convert(xml: string, options?: ConvertOptions): Object--><!--Device-ConvertXML-convert(xml: string, options?: ConvertOptions): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xml | string | Yes | XML文本，需符合XML语法规范，若包含"&"字符，请使用实体引用"&amp;"替换。 |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | No | 转换选项，用于自定义XML转换行为。不传入时使用ConvertOptions各属性的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 转换后的JavaScript对象，包含解析后的XML结构信息，具体属性键名由ConvertOptions定义。 |

## Examples

```TypeScript
let xml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '    <title>Happy</title>' +
    '    <todo>Work</todo>' +
    '    <todo>Play</todo>' +
    '</note>';
let conv = new convertxml.ConvertXML();
let options: convertxml.ConvertOptions = {
  trim: false,
  declarationKey: "_declaration",
  instructionKey: "_instruction",
  attributesKey: "_attributes",
  textKey: "_text",
  cdataKey: "_cdata",
  doctypeKey: "_doctype",
  commentKey: "_comment",
  parentKey: "_parent",
  typeKey: "_type",
  nameKey: "_name",
  elementsKey: "_elements"
};
let result = JSON.stringify(conv.convert(xml, options));
console.info(result);
// Output (non-compact)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Play"}]}]}]}
```

## convertToJSObject

```TypeScript
convertToJSObject(xml: string, options?: ConvertOptions): Object
```

将XML文本转换为Object类型对象，适用于XML配置文件解析、数据格式转换等场景。该方法将XML文本解析为层级嵌套结构，各XML组件按ConvertOptions中配置的键名映射为对象的属性。

> **说明：**
> 
> 从API version 9开始支持，从API version 14开始废弃，建议使用
> [fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](arkts-arkts-xml-convertxml-c.md#fastconverttojsobject)替代。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 14

**Substitutes:** [xml.ConvertXML#fastConvertToJSObject](arkts-arkts-xml-convertxml-c.md#fastconverttojsobject)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ConvertXML-convertToJSObject(xml: string, options?: ConvertOptions): Object--><!--Device-ConvertXML-convertToJSObject(xml: string, options?: ConvertOptions): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xml | string | Yes | XML文本，需符合XML语法规范，若包含"&"字符，请使用实体引用"&amp;"替换。 |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | No | 转换选项，用于自定义XML转换行为。不传入时使用ConvertOptions各属性的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 转换后的JavaScript对象，包含解析后的XML结构信息，具体属性键名由ConvertOptions定义。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200002 | Invalid xml string. |

## Examples

```TypeScript
try {
  let xml =
    '<?xml version="1.0" encoding="utf-8"?>' +
      '<note importance="high" logged="true">' +
      '    <title>Happy</title>' +
      '    <todo>Work</todo>' +
      '    <todo>Play</todo>' +
      '</note>';
  let conv = new convertxml.ConvertXML();
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  let result = JSON.stringify(conv.convertToJSObject(xml, options));
  console.info(result);
} catch (e) {
  console.error((e as Object).toString());
}
// Output (non-compact)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"text","_text":"Play"}]}]}]}
```

## fastConvertToJSObject

```TypeScript
fastConvertToJSObject(xml: string, options?: ConvertOptions): Object
```

将XML文本转换为Object类型对象，适用于XML配置文件解析、数据报文处理等场景。该方法将XML文本解析为层级嵌套结构，各XML组件按ConvertOptions中配置的键名映射为对象的属性。当单元素文本内容超过10M时，建议使用[largeConvertToJSObject&lt;sup&gt;23+&lt;/sup&gt;](arkts-arkts-xml-convertxml-c.md#largeconverttojsobject)替代。

> **说明：**
> 
> 该接口无法满足解析单元素文本内容超过10M的XML文件，当单元素文本内容超过10M时，会输出异常日志信息并返回一个仅包含XML声明的基础Object对象。
> 如需解析单元素文本内容超过10M的XML文本，建议使用[largeConvertToJSObject&lt;sup&gt;23+&lt;/sup&gt;](arkts-arkts-xml-convertxml-c.md#largeconverttojsobject)
> 替代。
> 
> 在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。fastConvertToJSObject接口转换后的对象以换行符（LF）表示换行。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ConvertXML-fastConvertToJSObject(xml: string, options?: ConvertOptions): Object--><!--Device-ConvertXML-fastConvertToJSObject(xml: string, options?: ConvertOptions): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xml | string | Yes | XML文本，需符合XML语法规范，若包含"&"字符，请使用实体引用"&amp;"替换。 单元素文本内容超过10M时，输出异常日志并返回仅包含XML声明的基础Object，建议使用largeConvertToJSObject替代。 |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | No | 转换选项，用于自定义XML转换行为。不传入时使用ConvertOptions各属性的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 转换后的JavaScript对象，用于提供解析后的XML结构信息，具体属性键名由ConvertOptions定义，可通过配置键名访问XML各组件的映射数据。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200002 | Invalid xml string. |

## Examples

```TypeScript
try {
  let xml =
    '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '   <title>Hello\r\nWorld</title>' +
    '   <todo><![CDATA[Work\r\n]]></todo>' +
    '</note>';
  let conv = new convertxml.ConvertXML();
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  let result = JSON.stringify(conv.fastConvertToJSObject(xml, options));
  console.info(result);
} catch (e) {
  console.error((e as Object).toString());
}
// Output (non-compact)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note","_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title","_elements":[{"_type":"text","_text":"Hello\nWorld"}]},{"_type":"element","_name":"todo","_elements":[{"_type":"cdata","_cdata":"Work\n"}]}]}]}
```

## largeConvertToJSObject

```TypeScript
largeConvertToJSObject(xml: string, options?: ConvertOptions): Object
```

将XML文本转换为Object类型对象，适用于XML日志文件、数据报文等大型XML解析场景。此方法支持解析单元素大小超过10M的大型XML文本，针对大文本场景进行了优化，可有效避免单元素文本过大导致的解析异常。当[fastConvertToJSObject&lt;sup&gt;14+&lt;/sup&gt;](arkts-arkts-xml-convertxml-c.md#fastconverttojsobject)因单元素文本内容超过10M无法正常解析时，可使用本方法作为替代方案。

> **说明：**
> 
> 当传入的XML文本无法正确解析为Object类型对象时，输出异常日志信息并返回一个仅包含XML声明的基础Object对象。
> 
> 在Windows环境中，通常以回车符（CR）和换行符（LF）一对字符来表示换行。本接口转换后的对象以换行符（LF）表示换行。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ConvertXML-largeConvertToJSObject(xml: string, options?: ConvertOptions): Object--><!--Device-ConvertXML-largeConvertToJSObject(xml: string, options?: ConvertOptions): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xml | string | Yes | XML文本，需符合XML语法规范，若包含"&"字符，请使用实体引用"&amp;"替换。 |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | No | 转换选项，用于自定义XML转换行为。不传入时使用ConvertOptions各属性的默认值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | 转换后的JavaScript对象，包含解析后的XML结构信息，具体属性键名由ConvertOptions定义。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200002 | Invalid xml string. |

## Examples

```TypeScript
try {
  let xmlstr =
    '<?xml version="1.0" encoding="utf-8"?>' +
    '<?custom-pi processing="example"?>' +
    '<catalog id="books">' +
      '<!-- Bestseller Example -->' +
      '<book category="fiction" ref="B101">' +
        '<title>Echoes &amp; Whispers</title>' +
        '<price unit="USD">19.99</price>' +
        '<descr>' +
          '<![CDATA[<b>suspense</b>novel & Legendary Stories]]>' +
        '</descr>' +
        '<popular/>' +
      '</book>' +
    '</catalog>';
  let conv = new convertxml.ConvertXML();
  let options: convertxml.ConvertOptions = {
    trim: false,
    declarationKey: "_declaration",
    instructionKey: "_instruction",
    attributesKey: "_attributes",
    textKey: "_text",
    cdataKey: "_cdata",
    doctypeKey: "_doctype",
    commentKey: "_comment",
    parentKey: "_parent",
    typeKey: "_type",
    nameKey: "_name",
    elementsKey: "_elements"
  };
  let result = JSON.stringify(conv.largeConvertToJSObject(xmlstr, options));
  console.info(result);
} catch (e) {
  console.error((e as Object).toString());
}
// Output (non-compact)
// {"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"instruction","_name":"custom-pi","_instruction":"processing=\"example\""},{"_type":"element","_name":"catalog","_attributes":{"id":"books"},"_elements":[{"_type":"comment","_comment":" Bestseller Example "},{"_type":"element","_name":"book","_parent":"catalog","_attributes":{"category":"fiction","ref":"B101"},"_elements":[{"_type":"element","_name":"title","_parent":"book","_elements":[{"_type":"text","_text":"Echoes & Whispers"}]},{"_type":"element","_name":"price","_parent":"book","_attributes":{"unit":"USD"},"_elements":[{"_type":"text","_text":"19.99"}]},{"_type":"element","_name":"descr","_parent":"book","_elements":[{"_type":"cdata","_cdata":"<b>suspense</b>novel & Legendary Stories"}]},{"_type":"element","_name":"popular","_parent":"book"}]}]}]}
```

