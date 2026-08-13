# LaunchMode

Defines the mode of stack operation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare enum LaunchMode--><!--Device-unnamed-export declare enum LaunchMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## STANDARD

```TypeScript
STANDARD = 0
```

The default mode of stack operation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LaunchMode-STANDARD = 0--><!--Device-LaunchMode-STANDARD = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MOVE_TO_TOP_SINGLETON

```TypeScript
MOVE_TO_TOP_SINGLETON = 1
```

When the NavDestination with a specified name exists, it will be moved to top of stack, otherwise, the behavior will be consistent with the STANDARD mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LaunchMode-MOVE_TO_TOP_SINGLETON = 1--><!--Device-LaunchMode-MOVE_TO_TOP_SINGLETON = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## POP_TO_SINGLETON

```TypeScript
POP_TO_SINGLETON = 2
```

When the NavDestination with a specified name exists, the stack will pop until that NavDestination, otherwise, the behavior will be consistent with the STANDARD mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LaunchMode-POP_TO_SINGLETON = 2--><!--Device-LaunchMode-POP_TO_SINGLETON = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NEW_INSTANCE

```TypeScript
NEW_INSTANCE = 3
```

Forced to create a new NavDestination instance.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-LaunchMode-NEW_INSTANCE = 3--><!--Device-LaunchMode-NEW_INSTANCE = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

