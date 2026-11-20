# PasteDataProperty

```TypeScript
interface PasteDataProperty
```

Defines the properties of all data records on the pasteboard, including the timestamp, data type, pasteable range, and additional data. The defined properties can be applied to the pasteboard only with the [setProperty](arkts-basicservices-pasteboard-pastedata-i.md#setproperty) method.

**Since:** 7

<!--Device-pasteboard-interface PasteDataProperty--><!--Device-pasteboard-interface PasteDataProperty-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from '@kit.BasicServicesKit';
```

## additions

```TypeScript
additions: Record<string, object>
```

Additional property data. It does not allow for dynamic adding of properties. Properties can be added only by re-assigning values. This parameter is left empty by default. For details, see the example of **setProperty**.

**Type:** Record&lt;string, object&gt;

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-additions: Record<string, object>--><!--Device-PasteDataProperty-additions: Record<string, object>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## localOnly

```TypeScript
localOnly: boolean
```

Whether the pasteboard content is for local access only. The value **true** indicates that content is for local access only, and the value **false** indicates that cross-device data transfer is allowed. The default value is **false**. The value will be overwritten by the value of the **shareOption** attribute. You are advised to use the [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md) attribute instead.

**Type:** boolean

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-localOnly: boolean--><!--Device-PasteDataProperty-localOnly: boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## mimeTypes

```TypeScript
readonly mimeTypes: Array<string>
```

Non-repeating data types of the data records on the pasteboard.

**Type:** Array&lt;string&gt;

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-readonly mimeTypes: Array<string>--><!--Device-PasteDataProperty-readonly mimeTypes: Array<string>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## shareOption

```TypeScript
shareOption: ShareOption
```

Pasteable ranges of pasteboard data. The default value is **CROSSDEVICE**. This parameter is mutually exclusive with **localOnly**. Setting **shareOption** affects the actual value of **localOnly**.

**Type:** [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md)

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-shareOption: ShareOption--><!--Device-PasteDataProperty-shareOption: ShareOption-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## tag

```TypeScript
tag: string
```

Custom tag. This parameter is left empty by default.

**Type:** string

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-tag: string--><!--Device-PasteDataProperty-tag: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## timestamp

```TypeScript
readonly timestamp: number
```

Timestamp when data is written to the pasteboard (unit: nanoseconds since the device is powered on).

**Type:** number

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-readonly timestamp: long--><!--Device-PasteDataProperty-readonly timestamp: long-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard
