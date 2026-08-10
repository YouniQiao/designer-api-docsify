# SystemDefinedPixelMap

与系统侧定义的[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)数据类型对应的图片数据类型，是  
[SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md)的子类，仅保存PixelMap的二进制数据。

**Inheritance/Implementation:** SystemDefinedPixelMap extends [SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class SystemDefinedPixelMap extends SystemDefinedRecord--><!--Device-unifiedDataChannel-class SystemDefinedPixelMap extends SystemDefinedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## rawData

```TypeScript
set rawData(value: Uint8Array)
```

PixelMap对象的二进制数据。

**Type:** Uint8Array

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SystemDefinedPixelMap-set rawData(value: Uint8Array)--><!--Device-SystemDefinedPixelMap-set rawData(value: Uint8Array)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

