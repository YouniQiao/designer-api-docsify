# PreviewMenuOptions

预览菜单的选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PreviewMenuOptions--><!--Device-unnamed-export declare interface PreviewMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hapticFeedbackMode

```TypeScript
hapticFeedbackMode?: HapticFeedbackMode
```

菜单弹出时振动效果，当ImageSpan或BuilderSpan绑定预览菜单时生效。

默认值：HapticFeedbackMode.DISABLED，菜单弹出时不振动。

**说明：** 仅当应用具备ohos.permission.VIBRATE权限，且用户启用了触感反馈时才会生效。

**Type:** [HapticFeedbackMode](../arkts-components/arkts-arkui-hapticfeedbackmode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PreviewMenuOptions-hapticFeedbackMode?: HapticFeedbackMode--><!--Device-PreviewMenuOptions-hapticFeedbackMode?: HapticFeedbackMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

