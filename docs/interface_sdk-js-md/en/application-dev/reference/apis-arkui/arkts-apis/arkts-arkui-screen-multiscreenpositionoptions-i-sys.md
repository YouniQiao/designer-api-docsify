# MultiScreenPositionOptions (System API)

Describes the screen position information.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-screen-interface MultiScreenPositionOptions--><!--Device-screen-interface MultiScreenPositionOptions-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## id

```TypeScript
id: long
```

Screen ID. The value must be a positive integer. Any non-positive integer values will be considered invalid and result in an error.

**Type:** long

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-MultiScreenPositionOptions-id: long--><!--Device-MultiScreenPositionOptions-id: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## startX

```TypeScript
startX: long
```

Start X coordinate of the screen. The top-left vertex of the bounding rectangle formed by the two screens is used as the origin, with the positive direction being rightwards. in px. The value must be a non-negative integer. Any other values will be considered invalid and result in an error.

**Type:** long

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-MultiScreenPositionOptions-startX: long--><!--Device-MultiScreenPositionOptions-startX: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## startY

```TypeScript
startY: long
```

Start Y coordinate of the screen. The top-left vertex of the bounding rectangle formed by the two screens is used as the origin, with the positive direction being downwards. in px. The value must be a non-negative integer. Any other values will be considered invalid and result in an error.

**Type:** long

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-MultiScreenPositionOptions-startY: long--><!--Device-MultiScreenPositionOptions-startY: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

