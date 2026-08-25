# ConvertXML

ConvertXML representation refers to extensible markup language.

**Since:** 8

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { convertxml } from 'kits/@kit.ArkTS';
```

## convert

```TypeScript
convert(xml: string, options?: ConvertOptions): Object
```

Converts an XML text to a JavaScript object.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [fastConvertToJSObject](#fastconverttojsobject)

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [xml](arkts-convertxml.md) | string | Yes |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

## convertToJSObject

```TypeScript
convertToJSObject(xml: string, options?: ConvertOptions): Object
```

Converts an XML text to an object of the object type.

**Since:** 9

**Deprecated since:** 14

**Substitutes:** [fastConvertToJSObject](#fastconverttojsobject)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [xml](arkts-convertxml.md) | string | Yes |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

**Error codes:**

| Error Code ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-parameter-parsing-error) |

## fastConvertToJSObject

```TypeScript
fastConvertToJSObject(xml: string, options?: ConvertOptions): Object
```

Converts an XML text to an object of the object type.

> **NOTE：**&gt;
> - This API cannot parse XML files with a large amount of data. If the text content of a single element exceeds
> 10 MB, an error message is displayed and an object that contains only the XML tag header will be returned.&gt;
> - In Windows, a newline is usually represented by the carriage return (CR) followed by the line feed (LF).
> However, the object obtained by calling this API uses only the LF to indicate a new line.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [xml](arkts-convertxml.md) | string | Yes |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

**Error codes:**

| Error Code ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-parameter-parsing-error) |

## largeConvertToJSObject

```TypeScript
largeConvertToJSObject(xml: string, options?: ConvertOptions): Object
```

Convert XML text to JavaScript objects, this method supports parsing large XML texts with a single node size exceeding 10M.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [xml](arkts-convertxml.md) | string | Yes |
| options | [ConvertOptions](arkts-arkts-xml-convertoptions-i.md) | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Object |

**Error codes:**

| Error Code ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-parameter-parsing-error) |
