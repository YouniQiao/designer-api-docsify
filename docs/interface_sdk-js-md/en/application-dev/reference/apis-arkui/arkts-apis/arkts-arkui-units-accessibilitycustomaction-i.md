# AccessibilityCustomAction

自定义无障碍操作接口。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface AccessibilityCustomAction--><!--Device-unnamed-export declare interface AccessibilityCustomAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onAction

```TypeScript
onAction: VoidCallback
```

处理自定义操作的回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityCustomAction-onAction: VoidCallback--><!--Device-AccessibilityCustomAction-onAction: VoidCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: ResourceStr
```

自定义操作的名称，用于标识和绑定操作回调。

**说明：**

名称的文本长度需在128字节以内，超出部分将被截断。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AccessibilityCustomAction-name: ResourceStr--><!--Device-AccessibilityCustomAction-name: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

