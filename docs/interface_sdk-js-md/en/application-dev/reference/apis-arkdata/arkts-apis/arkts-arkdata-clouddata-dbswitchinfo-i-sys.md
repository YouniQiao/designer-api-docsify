# DBSwitchInfo (System API)

端云协同数据库开关配置信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cloudData-interface DBSwitchInfo--><!--Device-cloudData-interface DBSwitchInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## enable

```TypeScript
enable: boolean
```

数据库是否启用端云协同开关。true为启用端云协同开关，false为不启用该开关。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DBSwitchInfo-enable: boolean--><!--Device-DBSwitchInfo-enable: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## tableInfo

```TypeScript
tableInfo?: Record<string, boolean>
```

表级别的端云协同开关配置信息。键为表名，值为该表的开关状态。true为打开该表的端云协同开关，false为关闭该表开关。当未配置该参数时，默认按照数据库级开关状态enable生效。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, boolean&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DBSwitchInfo-tableInfo?: Record<string, boolean>--><!--Device-DBSwitchInfo-tableInfo?: Record<string, boolean>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

