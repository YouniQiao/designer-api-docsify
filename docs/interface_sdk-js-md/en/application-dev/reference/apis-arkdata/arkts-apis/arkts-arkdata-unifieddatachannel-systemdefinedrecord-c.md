# SystemDefinedRecord

SystemDefinedRecord是[UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)的子类，也是OpenHarmony系统特有数据类型的基类，用于描述仅在OpenHarmony系统范围内流通的特有数据类型，推荐开发者优先使用SystemDefinedRecord的子类描述数据，如  
[SystemDefinedForm](arkts-arkdata-unifieddatachannel-systemdefinedform-c.md)、  
[SystemDefinedAppItem](arkts-arkdata-unifieddatachannel-systemdefinedappitem-c.md)、  
[SystemDefinedPixelMap](arkts-arkdata-unifieddatachannel-systemdefinedpixelmap-c.md)等具体子类。

**Inheritance/Implementation:** SystemDefinedRecord extends [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class SystemDefinedRecord extends UnifiedRecord--><!--Device-unifiedDataChannel-class SystemDefinedRecord extends UnifiedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## details

```TypeScript
details?: Record<string, int | long | double | string | Uint8Array>
```

是一个字典类型对象，key是string类型，value可以写入number（数值类型）、string（字符串类型）、Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, int \| long \| double \| string \| Uint8Array&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemDefinedRecord-details?: Record<string, int | long | double | string | Uint8Array>--><!--Device-SystemDefinedRecord-details?: Record<string, int | long | double | string | Uint8Array>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

