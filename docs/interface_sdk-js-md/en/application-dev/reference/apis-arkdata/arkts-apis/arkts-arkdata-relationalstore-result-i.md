# Result

记录受影响的数据行数量和结果集。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-relationalStore-interface Result--><!--Device-relationalStore-interface Result-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## changed

```TypeScript
readonly changed: long
```

表示受影响的行数量。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Result-readonly changed: long--><!--Device-Result-readonly changed: long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## resultSet

```TypeScript
readonly resultSet: LiteResultSet
```

表示受影响数据的结果集。默认返回1024行，最大支持32766行，超出部分将被丢弃。

**Type:** [LiteResultSet](arkts-arkdata-relationalstore-literesultset-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Result-readonly resultSet: LiteResultSet--><!--Device-Result-readonly resultSet: LiteResultSet-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

