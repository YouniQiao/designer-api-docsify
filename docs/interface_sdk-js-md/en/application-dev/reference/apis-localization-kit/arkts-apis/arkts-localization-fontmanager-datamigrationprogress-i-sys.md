# DataMigrationProgress (System API)

Describes the progress information of data migration, including the progress percentage and estimated remaining time. This API is the parameter type of the \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ API in the data migration callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-fontManager-interface DataMigrationProgress--><!--Device-fontManager-interface DataMigrationProgress-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## progressPercentage

```TypeScript
progressPercentage: int
```

Data migration progress percentage, which is calculated based on the number or size of migrated font files and may not increase evenly. When \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ reaches \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_, the migration task is about to complete and the \_\_\_INLINE\_CODE\_DESC\_USD\_2\_\_\_ callback is about to be invoked.The value range is [0, 100].

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DataMigrationProgress-progressPercentage: int--><!--Device-DataMigrationProgress-progressPercentage: int-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## timeRemaining

```TypeScript
timeRemaining: int
```

Estimated remaining time, which may vary depending on factors such as device performance, file size, and system load.The value must be a non-negative integer, with a minimum value of 0.The unit is seconds.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-DataMigrationProgress-timeRemaining: int--><!--Device-DataMigrationProgress-timeRemaining: int-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

