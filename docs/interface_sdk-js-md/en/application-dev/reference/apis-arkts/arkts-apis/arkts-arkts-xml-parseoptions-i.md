# ParseOptions

XML解析选项。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-xml-interface ParseOptions--><!--Device-xml-interface ParseOptions-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { xml } from 'kits/@kit.ArkTS';
```

## attributeValueCallbackFunction

```TypeScript
attributeValueCallbackFunction?: (name: string, value: string) => boolean
```

解析属性和属性值，默认值undefined，表示不解析。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-attributeValueCallbackFunction?: (name: string, value: string) => boolean--><!--Device-ParseOptions-attributeValueCallbackFunction?: (name: string, value: string) => boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes |  |
| value | string | Yes |  |

## attributeWithTagCallbackFunction

```TypeScript
attributeWithTagCallbackFunction?: AttributeWithTagCb
```

解析tagName标签，默认值undefined，表示不解析。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-ParseOptions-attributeWithTagCallbackFunction?: AttributeWithTagCb--><!--Device-ParseOptions-attributeWithTagCallbackFunction?: AttributeWithTagCb-End-->

**System capability:** SystemCapability.Utils.Lang

## tagValueCallbackFunction

```TypeScript
tagValueCallbackFunction?: (name: string, value: string) => boolean
```

解析开始标签、标签值和结束标签，默认值undefined，表示不解析。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-tagValueCallbackFunction?: (name: string, value: string) => boolean--><!--Device-ParseOptions-tagValueCallbackFunction?: (name: string, value: string) => boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes |  |
| value | string | Yes |  |

## tokenValueCallbackFunction

```TypeScript
tokenValueCallbackFunction?: (eventType: EventType, value: ParseInfo) => boolean
```

解析元素事件类型([EventType](arkts-arkts-xml-eventtype-e.md))和[ParseInfo](arkts-arkts-xml-parseinfo-i.md)属性，默认值undefined，表示不解析。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-tokenValueCallbackFunction?: (eventType: EventType, value: ParseInfo) => boolean--><!--Device-ParseOptions-tokenValueCallbackFunction?: (eventType: EventType, value: ParseInfo) => boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | [EventType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md) | Yes |  |
| value | [ParseInfo](arkts-arkts-xml-parseinfo-i.md) | Yes |  |

## ignoreNameSpace

```TypeScript
ignoreNameSpace?: boolean
```

是否忽略命名空间，忽略命名空间后，将不会对其进行解析。true表示忽略命名空间，false表示不忽略命名空间，默认值false。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-ignoreNameSpace?: boolean--><!--Device-ParseOptions-ignoreNameSpace?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

## supportDoctype

```TypeScript
supportDoctype?: boolean
```

是否解析文档类型，false表示不解析文档类型，true表示解析文档类型，默认值false。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ParseOptions-supportDoctype?: boolean--><!--Device-ParseOptions-supportDoctype?: boolean-End-->

**System capability:** SystemCapability.Utils.Lang

