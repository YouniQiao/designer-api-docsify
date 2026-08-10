# TextMenuShowMode

菜单的显示模式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum TextMenuShowMode--><!--Device-unnamed-export declare enum TextMenuShowMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

显示在当前窗口中。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuShowMode-DEFAULT = 0--><!--Device-TextMenuShowMode-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PREFER_WINDOW

```TypeScript
PREFER_WINDOW = 1
```

优先显示在独立窗口中，若不支持独立窗口，则显示在当前窗口中。

**说明：**

除应用主窗口、应用子窗口、系统模态窗口及系统桌面类型的窗口外，其他类型的窗口不支持将文本选择菜单显示在独立窗口中。

在预览器中不支持将文本选择菜单显示在独立窗口中。

在[UIExtension](../../../reference/apis-arkui/js-apis-arkui-uiExtension.md)中不支持将文本选择菜单显示在独立窗口中。

当文本类组件已经显示在子窗类型的[Popup](../../../reference/apis-arkui/arkui-ts/ohos-arkui-advanced-Popup.md)、  
[Dialog](../../../reference/apis-arkui/arkui-ts/ohos-arkui-advanced-Dialog.md)、  
[Toast](../../../ui/arkts-create-toast.md)、  
[Menu](../../../reference/apis-arkui/arkui-ts/ts-basic-components-menu.md)中时，不支持将其对应的文本选择菜单显示在独立窗口中。

当TextInput、TextArea可支持拉起AutoFill时，不支持将其对应的文本选择菜单显示在独立窗口中。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextMenuShowMode-PREFER_WINDOW = 1--><!--Device-TextMenuShowMode-PREFER_WINDOW = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

