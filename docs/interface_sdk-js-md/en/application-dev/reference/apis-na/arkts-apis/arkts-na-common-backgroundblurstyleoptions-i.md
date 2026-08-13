# BackgroundBlurStyleOptions

Defines the options of backgroundBlurStyle

**Inheritance/Implementation:** BackgroundBlurStyleOptions extends [BlurStyleOptions](arkts-na-common-blurstyleoptions-i.md#BlurStyleOptions)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface BackgroundBlurStyleOptions--><!--Device-unnamed-export declare interface BackgroundBlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## inactiveColor

```TypeScript
inactiveColor?: ResourceColor
```

Color of the background effect when the window is not focused.

**Type:** [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundBlurStyleOptions-inactiveColor?: ResourceColor--><!--Device-BackgroundBlurStyleOptions-inactiveColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## policy

```TypeScript
policy?: BlurStyleActivePolicy
```

Defines the policy for activating the blur style.

**Type:** [BlurStyleActivePolicy](arkts-na-common-blurstyleactivepolicy-e.md)

**Default:** BlurStyleActivePolicy.ALWAYS_ACTIVE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundBlurStyleOptions-policy?: BlurStyleActivePolicy--><!--Device-BackgroundBlurStyleOptions-policy?: BlurStyleActivePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

