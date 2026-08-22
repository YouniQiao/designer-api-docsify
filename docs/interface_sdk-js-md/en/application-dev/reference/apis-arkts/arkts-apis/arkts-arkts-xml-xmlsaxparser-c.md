# XmlSAXParser

The XmlSAXParser provides the capability of parsing XML in a streaming manner.

**Since:** 24

<!--Device-xml-class XmlSAXParser--><!--Device-xml-class XmlSAXParser-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { xml } from '@kit.ArkTS';
```

## constructor

```TypeScript
constructor(inputStream: stream.Readable, encoding?: string)
```

Creates and returns an XmlSAXParser instance.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-XmlSAXParser-constructor(inputStream: stream.Readable, encoding?: string)--><!--Device-XmlSAXParser-constructor(inputStream: stream.Readable, encoding?: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| inputStream | stream.Readable | Yes | An instance, of stream.Readable for the new XmlSAXParser. |
| encoding | string | No | [encoding='utf8'] this is its encoding. |

**Examples**

```TypeScript
let arrayBuffer = new ArrayBuffer(2048);
let thatSer = new xml.XmlSerializer(arrayBuffer, "utf-8");
```

```TypeScript
let serializer = new xml.XmlDynamicSerializer('utf-8');
```

```TypeScript
import { util } from '@kit.ArkTS';

let strXml = '<title>Happy</title>'
let textEncoder = new util.TextEncoder();
let uint8Array = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(uint8Array.buffer as object as ArrayBuffer, 'UTF-8');
```

## parse

```TypeScript
parse(xmlSAXHandler: XmlSAXHandler): void
```

Creates and returns an XmlSAXParser instance.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-XmlSAXParser-parse(xmlSAXHandler: XmlSAXHandler): void--><!--Device-XmlSAXParser-parse(xmlSAXHandler: XmlSAXHandler): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| xmlSAXHandler | [XmlSAXHandler](arkts-arkts-xml-xmlsaxhandler-i.md) | Yes | The simple API for XML handler. |

**Examples**

```TypeScript
import { util } from '@kit.ArkTS';

let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
    '<company>John &amp; Hans</company>' +
    '<title>Happy</title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer as object as ArrayBuffer, 'UTF-8');
let str = '';
function func(name: string, value: string) {
  str = name + value;
  console.info(str);
  return true;
}
let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tagValueCallbackFunction:func}
that.parse(options);
// note
// company
// John & Hans
// company
// title
// Happy
// title
// note
```

