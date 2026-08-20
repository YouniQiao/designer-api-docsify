# BlurStyleActivePolicy

Enumerates the policies for activating the blur style.

@enum { number }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum BlurStyleActivePolicy--><!--Device-unnamed-export declare enum BlurStyleActivePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FOLLOWS_WINDOW_ACTIVE_STATE

```TypeScript
FOLLOWS_WINDOW_ACTIVE_STATE = 0
```

The component has the blur effect only when the window is focused.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlurStyleActivePolicy-FOLLOWS_WINDOW_ACTIVE_STATE = 0--><!--Device-BlurStyleActivePolicy-FOLLOWS_WINDOW_ACTIVE_STATE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_ACTIVE

```TypeScript
ALWAYS_ACTIVE = 1
```

The component always has the blur effect, regardless of whether the window is focused.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlurStyleActivePolicy-ALWAYS_ACTIVE = 1--><!--Device-BlurStyleActivePolicy-ALWAYS_ACTIVE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALWAYS_INACTIVE

```TypeScript
ALWAYS_INACTIVE = 2
```

The component does not have the blur effect, regardless of whether the window is focused.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlurStyleActivePolicy-ALWAYS_INACTIVE = 2--><!--Device-BlurStyleActivePolicy-ALWAYS_INACTIVE = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

