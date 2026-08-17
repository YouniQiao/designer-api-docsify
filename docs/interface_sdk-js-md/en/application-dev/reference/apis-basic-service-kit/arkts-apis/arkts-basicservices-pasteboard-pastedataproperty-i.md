# PasteDataProperty

Defines the properties of PasteData in the pasteboard, including the timestamp, data types, pasteable range, and additional data. The defined properties can be applied to the pasteboard only with the [setProperty](arkts-basicservices-pasteboard-pastedata-i.md#setproperty) method.

**Since:** 23

<!--Device-pasteboard-interface PasteDataProperty--><!--Device-pasteboard-interface PasteDataProperty-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'pasteboard';
```

## additions

```TypeScript
additions: Record<string, RecordData>
```

additional property data. key-value pairs.

**Type:** Record&lt;string, [RecordData](arkts-basicservices-recorddata-t.md)&gt;

**Since:** 23

<!--Device-PasteDataProperty-additions: Record<string, RecordData>--><!--Device-PasteDataProperty-additions: Record<string, RecordData>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## localOnly

```TypeScript
localOnly: boolean
```

Whether the pasteboard content is for local access only. The default value is **false**. The value will be overwritten by the value of the **shareOption** attribute. You are advised to use the [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md#shareoption) attribute instead.

**Type:** boolean

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-localOnly: boolean--><!--Device-PasteDataProperty-localOnly: boolean-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## mimeTypes

```TypeScript
readonly mimeTypes: Array<string>
```

Data types of all records in PasteData.

**Type:** Array&lt;string&gt;

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-readonly mimeTypes: Array<string>--><!--Device-PasteDataProperty-readonly mimeTypes: Array<string>-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## shareOption

```TypeScript
shareOption: ShareOption
```

Pasteable ranges of PasteData. The default value is **CROSSDEVICE**.

**Type:** [ShareOption](arkts-basicservices-pasteboard-shareoption-e.md)

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-shareOption: ShareOption--><!--Device-PasteDataProperty-shareOption: ShareOption-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## tag

```TypeScript
tag: string
```

Custom tag. This parameter is left empty by default.

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-tag: string--><!--Device-PasteDataProperty-tag: string-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

## timestamp

```TypeScript
readonly timestamp: long
```

Timestamp when data is written to the pasteboard (unit: nanoseconds since the device is powered on).

**Type:** long

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-PasteDataProperty-readonly timestamp: long--><!--Device-PasteDataProperty-readonly timestamp: long-End-->

**System capability:** SystemCapability.MiscServices.Pasteboard

