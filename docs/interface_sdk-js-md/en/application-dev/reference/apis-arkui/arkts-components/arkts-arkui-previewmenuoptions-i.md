# PreviewMenuOptions

Defines the options of the preview menu.

**Since:** 18

<!--Device-unnamed-declare interface PreviewMenuOptions--><!--Device-unnamed-declare interface PreviewMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hapticFeedbackMode

```TypeScript
hapticFeedbackMode? : HapticFeedbackMode
```

Vibration effect when the menu is displayed. This parameter takes effect when ImageSpan or BuilderSpan is bound to the preview menu.

Default value: **HapticFeedbackMode.DISABLED** (no vibration when the menu is displayed)

Note: The settings take effect only when the application has the ohos.permission.VIBRATE permission and the user has enabled haptic feedback.

**Type:** HapticFeedbackMode

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PreviewMenuOptions-hapticFeedbackMode? : HapticFeedbackMode--><!--Device-PreviewMenuOptions-hapticFeedbackMode? : HapticFeedbackMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

