# XmlPullParser

The XmlPullParser interface is used to parse the existing xml file.

**Since:** 8

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## constructor

```TypeScript
constructor(buffer: ArrayBuffer | DataView, encoding?: string)
```

Creates and returns an XmlPullParser object.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| buffer | ArrayBuffer \| DataView | Yes |
| encoding | string | No |

## parse

```TypeScript
parse(option: ParseOptions): void
```

Starts parsing the XML file.

**Since:** 8

**Deprecated since:** 14

**Substitutes:** [parseXml](#parsexml)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | Yes |

## parseXml

```TypeScript
parseXml(option: ParseOptions): void
```

Parses XML information.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [ParseOptions](arkts-arkts-json-parseoptions-i.md) | Yes |
