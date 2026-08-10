# BackupConfig

用于备份数据库的配置信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-distributedKVStore-interface BackupConfig--><!--Device-distributedKVStore-interface BackupConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## fileName

```TypeScript
fileName: string
```

备份数据库的名称，无长度限制，不能包含特殊字符'/'。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupConfig-fileName: string--><!--Device-BackupConfig-fileName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## filePath

```TypeScript
filePath: string
```

备份数据库的路径，无长度限制。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupConfig-filePath: string--><!--Device-BackupConfig-filePath: string-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

