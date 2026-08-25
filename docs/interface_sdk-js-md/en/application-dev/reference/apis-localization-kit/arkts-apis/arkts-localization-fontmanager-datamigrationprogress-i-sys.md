# DataMigrationProgress (System API)

Describes the progress information of data migration, including the progress percentage and estimated remaining time. This API is the parameter type of the `onProgress` API in the data migration callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fontManager } from '@kit.LocalizationKit';
```

## progressPercentage

```TypeScript
progressPercentage: int
```

Data migration progress percentage, which is calculated based on the number or size of migrated font files and may not increase evenly. When `progressPercentage` reaches `100`, the migration task is about to complete and the `onResult` callback is about to be invoked. The value range is [0, 100].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## timeRemaining

```TypeScript
timeRemaining: int
```

Estimated remaining time, which may vary depending on factors such as device performance, file size, and system load. The value must be a non-negative integer, with a minimum value of 0. The unit is seconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.
