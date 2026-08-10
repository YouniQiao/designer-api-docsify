# ApplicationDefinedRecord

ApplicationDefinedRecord是[UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)的子类，也是应用自定义数据类型的基类，用于描述仅在应用生态内部流通的自定义数据类型，应用可基于此类进行自定义数据类型的扩展。

**Inheritance/Implementation:** ApplicationDefinedRecord extends [UnifiedRecord](arkts-arkdata-unifieddatachannel-unifiedrecord-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class ApplicationDefinedRecord extends UnifiedRecord--><!--Device-unifiedDataChannel-class ApplicationDefinedRecord extends UnifiedRecord-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## applicationDefinedType

```TypeScript
set applicationDefinedType(value: string)
```

应用自定义类型标识符，必须以'ApplicationDefined'开头。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationDefinedRecord-set applicationDefinedType(value: string)--><!--Device-ApplicationDefinedRecord-set applicationDefinedType(value: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## rawData

```TypeScript
set rawData(value: Uint8Array)
```

应用自定义数据类型的二进制数据。

**Type:** Uint8Array

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ApplicationDefinedRecord-set rawData(value: Uint8Array)--><!--Device-ApplicationDefinedRecord-set rawData(value: Uint8Array)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

