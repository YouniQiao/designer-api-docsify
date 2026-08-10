# @ohos.prompt

创建并显示文本提示框、对话框和操作菜单。

> **说明：**
> 
> 从API version 9 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](arkts-promptaction.md)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.promptAction/promptAction

<!--Device-unnamed-declare namespace prompt--><!--Device-unnamed-declare namespace prompt-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { prompt } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [showActionMenu](arkts-arkui-prompt-showactionmenu-f.md#showactionmenu) | 创建并显示操作菜单，菜单响应结果异步返回。 |
| [showActionMenu](arkts-arkui-prompt-showactionmenu-f.md#showactionmenu-1) | 创建并显示操作菜单，菜单响应后同步返回结果。 |
| [showDialog](arkts-arkui-prompt-showdialog-f.md#showdialog) | 创建并显示对话框，对话框响应结果异步返回。 |
| [showDialog](arkts-arkui-prompt-showdialog-f.md#showdialog-1) | 创建并显示对话框，对话框响应后同步返回结果。 |
| [showToast](arkts-arkui-prompt-showtoast-f.md#showtoast) | 创建并显示文本提示框。 |

### Interfaces

| Name | Description |
| --- | --- |
| [ActionMenuOptions](arkts-arkui-prompt-actionmenuoptions-i.md) | 操作菜单的选项。 |
| [ActionMenuSuccessResponse](arkts-arkui-prompt-actionmenusuccessresponse-i.md) | 操作菜单的响应结果。 |
| [Button](arkts-arkui-prompt-button-i.md) | 菜单中的菜单项按钮。 |
| [ShowDialogOptions](arkts-arkui-prompt-showdialogoptions-i.md) | 对话框的选项。 |
| [ShowDialogSuccessResponse](arkts-arkui-prompt-showdialogsuccessresponse-i.md) | 对话框的响应结果。 |
| [ShowToastOptions](arkts-arkui-prompt-showtoastoptions-i.md) | 文本提示框的选项。 |

