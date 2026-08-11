# XmlSAXParser

The XmlSAXParser provides the capability of parsing XML in a streaming manner.

**Since:** 24

<!--Device-xml-class XmlSAXParser--><!--Device-xml-class XmlSAXParser-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputStream | stream.Readable | Yes |
| encoding | string | No |

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| xmlSAXHandler | [XmlSAXHandler](arkts-arkts-xml-xmlsaxhandler-i.md) | Yes |
