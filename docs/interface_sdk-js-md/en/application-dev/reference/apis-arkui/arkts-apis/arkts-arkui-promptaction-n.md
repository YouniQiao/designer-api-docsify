# promptAction

创建并显示即时反馈、对话框和操作菜单。

> **说明：**
> 
> - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
> 
> - 本模块不支持在[UIAbility](../../apis-ability-kit/arkts-apis/arkts-app-ability-uiability.md/arkts-app-ability-uiability.md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。
> 
> - 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../../../ui/arkts-global-interface.md#ui上下文不明确)的地方使用，参见
> [UIContext](arkts-arkui-uicontext.md)说明。建议&lt;!--Del--&gt;在除
> [ServiceExtensionAbility](../../../application-models/serviceextensionability-sys.md)等无UI界面的场景外，均&lt;!--DelEnd--&gt;使用
> UIContext中的弹窗方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace promptAction--><!--Device-unnamed-declare namespace promptAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [openToast](arkts-arkui-promptaction-opentoast-f.md#opentoast) | 显示即时反馈并通过Promise返回其id。 |
| [closeToast](arkts-arkui-promptaction-closetoast-f.md#closetoast) | 关闭即时反馈。 |

### Classes

| Name | Description |
| --- | --- |
| [CommonController](arkts-arkui-promptaction-commoncontroller-c.md) | 公共控制器，可以控制promptAction相关组件。 |
| [DialogController](arkts-arkui-promptaction-dialogcontroller-c.md) | 自定义弹窗控制器，继承自[CommonController](../../../reference/apis-arkui/js-apis-promptAction copy.md#commoncontroller18)。  DialogController可作为UIContext弹出自定义弹窗的成员变量，具体用法可看  [openCustomDialogWithController](../../../reference/apis-arkui/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)和[presentCustomDialog](../../../reference/apis-arkui/arkts-apis-uicontext-promptaction.md#presentcustomdialog18)示例。 |

### Interfaces

| Name | Description |
| --- | --- |
| [ShowToastOptions](arkts-arkui-promptaction-showtoastoptions-i.md) | Toast的选项。 |
| [Button](arkts-arkui-promptaction-button-i.md) | 菜单中的菜单项按钮。 |
| [ShowDialogSuccessResponse](arkts-arkui-promptaction-showdialogsuccessresponse-i.md) | 对话框的响应结果。 |
| [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | 对话框的选项。 |
| [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md) | 弹窗的选项。 |
| [CustomDialogOptions](arkts-arkui-promptaction-customdialogoptions-i.md) | 自定义弹窗的内容，继承自[BaseDialogOptions](../../../reference/apis-arkui/js-apis-promptAction copy.md#basedialogoptions11)。 |
| [DialogOptions](arkts-arkui-promptaction-dialogoptions-i.md) | 自定义弹窗的内容，继承自[BaseDialogOptions](../../../reference/apis-arkui/js-apis-promptAction copy.md#basedialogoptions11)。 |
| [ActionMenuSuccessResponse](arkts-arkui-promptaction-actionmenusuccessresponse-i.md) | 操作菜单的响应结果。 |
| [ActionMenuOptions](arkts-arkui-promptaction-actionmenuoptions-i.md) | 操作菜单的选项。 |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i-sys.md) | 对话框的选项。 |
| [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i-sys.md) | 弹窗的选项。 |
| [ActionMenuOptions](arkts-arkui-promptaction-actionmenuoptions-i-sys.md) | 操作菜单的选项。 |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e.md) | 设置Toast的显示模式，默认显示在应用内，支持显示在子窗。 |
| [CommonState](arkts-arkui-promptaction-commonstate-e.md) | 自定义弹窗的状态。 |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ToastShowMode](arkts-arkui-promptaction-toastshowmode-e-sys.md) | 设置Toast的显示模式，默认显示在应用内，支持显示在子窗。 |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [PromptActionSingleButton](arkts-arkui-promptaction-promptactionsinglebutton-t.md) | 菜单中的菜单项按钮，仅支持1个按钮。 |
| [PromptActionDoubleButtons](arkts-arkui-promptaction-promptactiondoublebuttons-t.md) | 菜单中的菜单项按钮，仅支持2个按钮。 |
| [PromptActionTripleButtons](arkts-arkui-promptaction-promptactiontriplebuttons-t.md) | 菜单中的菜单项按钮，仅支持3个按钮。 |
| [PromptActionQuadrupleButtons](arkts-arkui-promptaction-promptactionquadruplebuttons-t.md) | 菜单中的菜单项按钮，仅支持4个按钮。 |
| [PromptActionQuintupleButtons](arkts-arkui-promptaction-promptactionquintuplebuttons-t.md) | 菜单中的菜单项按钮，仅支持5个按钮。 |
| [PromptActionSextupleButtons](arkts-arkui-promptaction-promptactionsextuplebuttons-t.md) | 菜单中的菜单项按钮，仅支持6个按钮。 |
| [DialogOptionsCornerRadius](arkts-arkui-promptaction-dialogoptionscornerradius-t.md) | 表示弹窗背板的圆角半径允许的数据字段类型。 |
| [DialogOptionsBorderWidth](arkts-arkui-promptaction-dialogoptionsborderwidth-t.md) | 表示弹窗背板的边框宽度允许的数据字段类型。 |
| [DialogOptionsBorderColor](arkts-arkui-promptaction-dialogoptionsbordercolor-t.md) | 表示弹窗背板的边框颜色允许的数据字段类型。 |
| [DialogOptionsBorderStyle](arkts-arkui-promptaction-dialogoptionsborderstyle-t.md) | 表示弹窗背板的边框样式允许的数据字段类型。 |
| [DialogOptionsShadow](arkts-arkui-promptaction-dialogoptionsshadow-t.md) | 表示弹窗背板的阴影允许的数据字段类型。 |

