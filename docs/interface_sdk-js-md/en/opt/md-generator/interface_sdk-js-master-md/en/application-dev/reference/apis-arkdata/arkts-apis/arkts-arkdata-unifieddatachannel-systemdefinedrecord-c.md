# SystemDefinedRecord

Represents specific data types defined by OpenHarmony. It is a child class of [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md#UnifiedRecord) and a base class of OpenHarmony-specific data types. You are advised to use the child class of **SystemDefinedRecord**, for example, [SystemDefinedForm](arkts-arkdata-unifieddatachannel-systemdefinedform-c.md#SystemDefinedForm), [SystemDefinedAppItem](arkts-arkdata-unifieddatachannel-systemdefinedappitem-c.md#SystemDefinedAppItem), and [SystemDefinedPixelMap](arkts-arkdata-unifieddatachannel-systemdefinedpixelmap-c.md#SystemDefinedPixelMap), to describe OpenHarmony-specific data.

**Inheritance/Implementation:** SystemDefinedRecord extends [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md#UnifiedRecord)

**Since:** 23

**Deprecated since:** -1

<!--Device-unifiedDataChannel-class SystemDefinedRecord--><!--Device-unifiedDataChannel-class SystemDefinedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

## details

```TypeScript
details?: Record<string, number | number | number | string | Uint8Array>
```

A dictionary type object, where the key is of the string type, and the value can be a number, a string, or a Uint 8Array. The default value is an empty dictionary object.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, number \| number \| number \| string \| Uint8Array&gt;

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemDefinedRecord-details?: Record<string, int | long | double | string | Uint8Array>--><!--Device-SystemDefinedRecord-details?: Record<string, int | long | double | string | Uint8Array>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core
