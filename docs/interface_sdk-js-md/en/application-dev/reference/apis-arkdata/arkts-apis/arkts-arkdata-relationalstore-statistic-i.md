# Statistic

Defines a struct for the device-cloud sync statistics of a database table.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-relationalStore-interface Statistic--><!--Device-relationalStore-interface Statistic-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## failed

```TypeScript
failed: int
```

Number of rows that failed to be synced between the device and cloud in the database table.

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Statistic-failed: int--><!--Device-Statistic-failed: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## remained

```TypeScript
remained: int
```

Number of rows that are not executed for device-cloud sync in the database table.

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Statistic-remained: int--><!--Device-Statistic-remained: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## successful

```TypeScript
successful: int
```

Number of rows that are successfully synced between the device and cloud in the database table.

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Statistic-successful: int--><!--Device-Statistic-successful: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## total

```TypeScript
total: int
```

Total number of rows to be synced between the device and cloud in the database table.

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Statistic-total: int--><!--Device-Statistic-total: int-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

