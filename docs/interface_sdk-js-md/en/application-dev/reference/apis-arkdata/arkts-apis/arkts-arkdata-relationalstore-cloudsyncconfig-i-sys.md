# CloudSyncConfig

云同步配置信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-relationalStore-interface CloudSyncConfig--><!--Device-relationalStore-interface CloudSyncConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## downloadOnly

```TypeScript
downloadOnly?: boolean
```

是否仅下行云端数据到本地。true表示仅下行云端数据到本地，false表示先下行云端数据到本地，再上行本地数据到云侧的同步流程。默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CloudSyncConfig-downloadOnly?: boolean--><!--Device-CloudSyncConfig-downloadOnly?: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

