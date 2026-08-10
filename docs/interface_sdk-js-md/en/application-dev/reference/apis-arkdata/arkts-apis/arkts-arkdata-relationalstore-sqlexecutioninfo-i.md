# SqlExecutionInfo

描述数据库执行的SQL语句的统计信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface SqlExecutionInfo--><!--Device-relationalStore-interface SqlExecutionInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## executeTime

```TypeScript
executeTime: long
```

表示执行SQL语句的时间，单位为μs。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SqlExecutionInfo-executeTime: long--><!--Device-SqlExecutionInfo-executeTime: long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## prepareTime

```TypeScript
prepareTime: long
```

表示准备SQL和绑定参数的时间，单位为μs。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SqlExecutionInfo-prepareTime: long--><!--Device-SqlExecutionInfo-prepareTime: long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## sql

```TypeScript
sql: Array<string>
```

表示执行的SQL语句的数组。当  
[batchInsert](arkts-arkdata-relationalstore-rdbstore-i.md#batchinsert)的参数太大时，可能有多个SQL。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SqlExecutionInfo-sql: Array<string>--><!--Device-SqlExecutionInfo-sql: Array<string>-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## totalTime

```TypeScript
totalTime: long
```

表示执行SQL语句的总时间，单位为μs。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SqlExecutionInfo-totalTime: long--><!--Device-SqlExecutionInfo-totalTime: long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## waitTime

```TypeScript
waitTime: long
```

表示获取句柄的时间，单位为μs。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-SqlExecutionInfo-waitTime: long--><!--Device-SqlExecutionInfo-waitTime: long-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

