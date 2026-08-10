# Audio

音频类型数据，是[File](arkts-arkdata-unifieddatachannel-file-c.md)的子类，用于描述音频文件。

**Inheritance/Implementation:** Audio extends [File](arkts-arkdata-unifieddatachannel-file-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unifiedDataChannel-class Audio extends File--><!--Device-unifiedDataChannel-class Audio extends File-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from 'kits/@kit.ArkData';
```

## audioUri

```TypeScript
set audioUri(value: string)
```

本地音频数据uri或网络音频uri，本地音频数据uri可通过[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)函数获取。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Audio-set audioUri(value: string)--><!--Device-Audio-set audioUri(value: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

