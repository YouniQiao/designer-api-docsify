# DistributedInfo (System API)

记录分布式信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-relationalStore-interface DistributedInfo--><!--Device-relationalStore-interface DistributedInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## flag

```TypeScript
flag?: DistributedOrigin
```

表示数据来源，不传入则保持原有数值。

**Type:** [DistributedOrigin](arkts-arkdata-relationalstore-distributedorigin-e-sys.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedInfo-flag?: DistributedOrigin--><!--Device-DistributedInfo-flag?: DistributedOrigin-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

## oriDevice

```TypeScript
oriDevice?: string
```

表示数据产生者的设备id，不传入则保持原有设备id。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DistributedInfo-oriDevice?: string--><!--Device-DistributedInfo-oriDevice?: string-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**System API:** This is a system API.

