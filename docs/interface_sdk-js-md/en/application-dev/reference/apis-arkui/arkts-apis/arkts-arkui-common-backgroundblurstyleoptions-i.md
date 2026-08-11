# BackgroundBlurStyleOptions

Defines the options of backgroundBlurStyle

**Inheritance/Implementation:** BackgroundBlurStyleOptions extends [BlurStyleOptions](../arkts-components/arkts-arkui-blurstyleoptions-i.md/arkts-arkui-blurstyleoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BackgroundBlurStyleOptions extends BlurStyleOptions--><!--Device-unnamed-export declare interface BackgroundBlurStyleOptions extends BlurStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## inactiveColor

```TypeScript
inactiveColor?: ResourceColor
```

Color of the background effect when the window is not focused.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.Transparent

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundBlurStyleOptions-inactiveColor?: ResourceColor--><!--Device-BackgroundBlurStyleOptions-inactiveColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## policy

```TypeScript
policy?: BlurStyleActivePolicy
```

Defines the policy for activating the blur style.

**Type:** [BlurStyleActivePolicy](../arkts-components/arkts-arkui-blurstyleactivepolicy-e.md)

**Default:** BlurStyleActivePolicy.ALWAYS_ACTIVE

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackgroundBlurStyleOptions-policy?: BlurStyleActivePolicy--><!--Device-BackgroundBlurStyleOptions-policy?: BlurStyleActivePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

