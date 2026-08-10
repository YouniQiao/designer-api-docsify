# Statistic

描述数据库表的端云同步过程的统计信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface Statistic--><!--Device-relationalStore-interface Statistic-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## failed

```TypeScript
failed: int
```

表示数据库表中端云同步失败的行数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Statistic-failed: int--><!--Device-Statistic-failed: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## remained

```TypeScript
remained: int
```

表示数据库表中端云同步剩余未执行的行数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Statistic-remained: int--><!--Device-Statistic-remained: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## successful

```TypeScript
successful: int
```

表示数据库表中端云同步成功的行数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Statistic-successful: int--><!--Device-Statistic-successful: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## total

```TypeScript
total: int
```

表示数据库表中需要端云同步的总行数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Statistic-total: int--><!--Device-Statistic-total: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

