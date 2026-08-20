# AccessibilitySamePageMode

Enumerates the same-page modes for cross-process embedded components and their host applications. @enum { int }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum AccessibilitySamePageMode--><!--Device-unnamed-export declare enum AccessibilitySamePageMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SEMI_SILENT

```TypeScript
SEMI_SILENT = 0
```

Ignores initial page loading events and root node page events from the cross-process embedded component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilitySamePageMode-SEMI_SILENT = 0--><!--Device-AccessibilitySamePageMode-SEMI_SILENT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FULL_SILENT

```TypeScript
FULL_SILENT = 1
```

Ignores all page events from the cross-process embedded component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilitySamePageMode-FULL_SILENT = 1--><!--Device-AccessibilitySamePageMode-FULL_SILENT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

