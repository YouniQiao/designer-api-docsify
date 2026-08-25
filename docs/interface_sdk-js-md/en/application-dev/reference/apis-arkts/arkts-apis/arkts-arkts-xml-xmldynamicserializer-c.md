# XmlDynamicSerializer

The XmlDynamicSerializer interface is used to dynamically generate an xml file.

**Since:** 20

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## addEmptyElement

```TypeScript
addEmptyElement(name: string): void
```

Add an empty element.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200064](../errorcode-utils.md#10200064-input-string-cannot-be-empty) |

## constructor

```TypeScript
constructor(encoding?: string)
```

A parameterized constructor used to create a new XmlDynamicSerializer instance. The input parameter is an encoding format of string type.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encoding | string | No |

**Error codes:**

| Error Code ID |
| --- |
| [10200066](../errorcode-utils.md#10200066-incorrect-encoding-format) |

## endElement

```TypeScript
endElement(): void
```

Writes end tag of the element.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200065](../errorcode-utils.md#10200065-mismatched-element-start-and-end-tags) |

## getOutput

```TypeScript
getOutput(): ArrayBuffer
```

Get an ArrayBuffer from a XmlDynamicSerializer instance.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| ArrayBuffer |

## setAttributes

```TypeScript
setAttributes(name: string, value: string): void
```

Write an attribute to xml element.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |
| value | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200063](../errorcode-utils.md#10200063-xml-declaration-or-attribute-position-error) |
| [10200064](../errorcode-utils.md#10200064-input-string-cannot-be-empty) |

## setCdata

```TypeScript
setCdata(text: string): void
```

Writes the CDATA.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200064](../errorcode-utils.md#10200064-input-string-cannot-be-empty) |

## setComment

```TypeScript
setComment(text: string): void
```

Writes the comment to xml.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200064](../errorcode-utils.md#10200064-input-string-cannot-be-empty) |

## setDeclaration

```TypeScript
setDeclaration(): void
```

Writes xml declaration with encoding. For example: &lt;?xml version="1.0" encoding="utf-8"?&gt;.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200063](../errorcode-utils.md#10200063-xml-declaration-or-attribute-position-error) |

## setDocType

```TypeScript
setDocType(text: string): void
```

Writes the DOCTYPE.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200064](../errorcode-utils.md#10200064-input-string-cannot-be-empty) |

## setNamespace

```TypeScript
setNamespace(prefix: string, namespace: string): void
```

Writes the namespace of the current element tag.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| prefix | string | Yes |
| namespace | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200064](../errorcode-utils.md#10200064-input-string-cannot-be-empty) |

## setText

```TypeScript
setText(text: string): void
```

Writes the text to xml element.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200064](../errorcode-utils.md#10200064-input-string-cannot-be-empty) |

## startElement

```TypeScript
startElement(name: string): void
```

Writes a element start tag with the given name.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10200062](../errorcode-utils.md#10200062-xml-cumulative-length-exceeded) |
| [10200064](../errorcode-utils.md#10200064-input-string-cannot-be-empty) |
