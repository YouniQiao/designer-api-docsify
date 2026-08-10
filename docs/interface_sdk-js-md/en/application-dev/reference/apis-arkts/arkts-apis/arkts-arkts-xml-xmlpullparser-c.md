# XmlPullParser

XmlPullParser接口用于解析现有的XML文件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-xml-class XmlPullParser--><!--Device-xml-class XmlPullParser-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(buffer: ArrayBuffer | DataView, encoding?: string)
```

构造并返回一个XmlPullParser对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlPullParser-constructor(buffer: ArrayBuffer | DataView, encoding?: string)--><!--Device-XmlPullParser-constructor(buffer: ArrayBuffer | DataView, encoding?: string)-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer \| DataView | Yes | 用于解析的XML文本信息。 |
| encoding | string | No | 编码格式，默认'utf-8'（目前仅支持'utf-8'）。 |

## Examples

```TypeScript
import { util } from '@kit.ArkTS';

let strXml = '<title>Happy</title>'
let textEncoder = new util.TextEncoder();
let uint8Array = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(uint8Array.buffer as object as ArrayBuffer, 'UTF-8');
```

## parse

```TypeScript
parse(option: ParseOptions): void
```

该接口用于解析XML。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 14

**Substitutes:** ohos.xml.XmlPullParser.parseXml

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-XmlPullParser-parse(option: ParseOptions): void--><!--Device-XmlPullParser-parse(option: ParseOptions): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | Yes | XML解析选项。 |

## Examples

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

## parseXml

```TypeScript
parseXml(option: ParseOptions): void
```

解析XML。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-XmlPullParser-parseXml(option: ParseOptions): void--><!--Device-XmlPullParser-parseXml(option: ParseOptions): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | Yes | XML解析选项。 |

