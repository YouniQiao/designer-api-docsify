# ClearConfig (System API)

端云协同数据库级清除配置。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cloudData-interface ClearConfig--><!--Device-cloudData-interface ClearConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## dbInfo

```TypeScript
dbInfo: Record<string, DBActionInfo>
```

要清除数据的库信息及清除规则。键为数据库名称，值为该数据库的清除配置信息。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, DBActionInfo&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ClearConfig-dbInfo: Record<string, DBActionInfo>--><!--Device-ClearConfig-dbInfo: Record<string, DBActionInfo>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

