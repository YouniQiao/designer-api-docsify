# KeyProcessingMode

Key processing mode. Determines the priority of key event processing when component cannot handle the key event.

@enum { number }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum KeyProcessingMode--><!--Device-unnamed-export declare enum KeyProcessingMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FOCUS_NAVIGATION

```TypeScript
FOCUS_NAVIGATION = 0
```

Key events are used to move focus.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyProcessingMode-FOCUS_NAVIGATION = 0--><!--Device-KeyProcessingMode-FOCUS_NAVIGATION = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ANCESTOR_EVENT

```TypeScript
ANCESTOR_EVENT = 1
```

Key events bubble up to ancestors.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyProcessingMode-ANCESTOR_EVENT = 1--><!--Device-KeyProcessingMode-ANCESTOR_EVENT = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

