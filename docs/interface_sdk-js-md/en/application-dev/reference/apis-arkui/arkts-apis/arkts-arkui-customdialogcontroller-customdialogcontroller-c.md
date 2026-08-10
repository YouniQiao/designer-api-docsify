# CustomDialogController

自定义弹窗的控制器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class CustomDialogController--><!--Device-unnamed-export declare class CustomDialogController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## close

```TypeScript
close(): void
```

关闭显示的自定义弹窗，若已关闭，则不生效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-close(): void--><!--Device-CustomDialogController-close(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: CustomDialogControllerOptions)
```

自定义弹窗的构造器。

> **说明：**
> 
> 自定义弹窗的所有参数，不支持动态刷新，但可以通过设置customStyle为true，并在自定义组件上设置
[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、  
[backgroundBlurStyle](ts-universal-attributes-background.md#backgroundblurstyle9)、  
[尺寸设置](ts-universal-attributes-size.md)等属性，通过属性绑定的状态变量来实现动态刷新的效果。  
> 
> 在CustomDialogController作为全局变量以实现全局自定义弹窗的场景下，若对controller重新赋值，则无法通过其关闭之前的弹窗。建议在重新赋值前先关闭弹窗。
> 
> 在自定义弹窗内拉起另一个自定义弹窗时，不建议直接关闭拉起方。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-constructor(value: CustomDialogControllerOptions)--><!--Device-CustomDialogController-constructor(value: CustomDialogControllerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CustomDialogControllerOptions](arkts-arkui-customdialogcontroller-customdialogcontrolleroptions-i.md) | Yes |  |

## getExternalOptions

```TypeScript
getExternalOptions(): CustomDialogControllerExternalOptions
```

获取自定义弹窗的外部选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-getExternalOptions(): CustomDialogControllerExternalOptions--><!--Device-CustomDialogController-getExternalOptions(): CustomDialogControllerExternalOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [CustomDialogControllerExternalOptions](arkts-arkui-customdialogcontroller-customdialogcontrollerexternaloptions-i.md) | 返回自定义弹窗的外部选项。 |

## getState

```TypeScript
getState(): PromptActionCommonState
```

获取自定义弹窗的状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-getState(): PromptActionCommonState--><!--Device-CustomDialogController-getState(): PromptActionCommonState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PromptActionCommonState](arkts-arkui-promptactioncommonstate-t.md) | 返回对应的弹窗状态。 |

## open

```TypeScript
open(): void
```

显示自定义弹窗内容，允许多次使用。如果弹框为SubWindow模式，弹窗可以显示在主窗口之外，此时弹框不允许再弹出SubWindow弹框。

> **说明：**
> 
> 不支持在输入法类型窗口中使用子窗（showInSubwindow为true）的CustomDialog，详情见输入法框架的约束与限制说明
[createPanel](../../apis-ime-kit/js-apis-inputmethodengine.md#createpanel10-1)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomDialogController-open(): void--><!--Device-CustomDialogController-open(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

