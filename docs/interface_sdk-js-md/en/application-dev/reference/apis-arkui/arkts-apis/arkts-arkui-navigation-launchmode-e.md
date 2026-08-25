# LaunchMode

Defines the mode of stack operation.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## STANDARD

```TypeScript
STANDARD = 0
```

The default mode of stack operation.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MOVE_TO_TOP_SINGLETON

```TypeScript
MOVE_TO_TOP_SINGLETON = 1
```

When the NavDestination with a specified name exists, it will be moved to top of stack, otherwise, the behavior will be consistent with the STANDARD mode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## POP_TO_SINGLETON

```TypeScript
POP_TO_SINGLETON = 2
```

When the NavDestination with a specified name exists, the stack will pop until that NavDestination, otherwise, the behavior will be consistent with the STANDARD mode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NEW_INSTANCE

```TypeScript
NEW_INSTANCE = 3
```

Forced to create a new NavDestination instance.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
