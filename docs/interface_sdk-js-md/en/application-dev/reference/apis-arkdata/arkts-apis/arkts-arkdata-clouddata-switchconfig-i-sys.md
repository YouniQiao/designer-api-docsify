# SwitchConfig (System API)

端云协同数据库级配置。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cloudData-interface SwitchConfig--><!--Device-cloudData-interface SwitchConfig-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## dbInfo

```TypeScript
dbInfo: Record<string, DBSwitchInfo>
```

数据库级别的开关配置信息。键为库名称，值为该库的配置信息。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, DBSwitchInfo&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-SwitchConfig-dbInfo: Record<string, DBSwitchInfo>--><!--Device-SwitchConfig-dbInfo: Record<string, DBSwitchInfo>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

