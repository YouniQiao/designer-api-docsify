# DBActionInfo (System API)

端云协同数据库级清除配置信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cloudData-interface DBActionInfo--><!--Device-cloudData-interface DBActionInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## action

```TypeScript
action: ClearAction
```

数据库默认数据清除方式。

**Type:** [ClearAction](arkts-arkdata-clouddata-clearaction-e-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DBActionInfo-action: ClearAction--><!--Device-DBActionInfo-action: ClearAction-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## tableInfo

```TypeScript
tableInfo?: Record<string, ClearAction>
```

要清除数据的表信息及清除规则。键为表名称，值为该表的清除方式。当未配置该参数时，默认使用数据库的数据清除方式。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ClearAction&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DBActionInfo-tableInfo?: Record<string, ClearAction>--><!--Device-DBActionInfo-tableInfo?: Record<string, ClearAction>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

