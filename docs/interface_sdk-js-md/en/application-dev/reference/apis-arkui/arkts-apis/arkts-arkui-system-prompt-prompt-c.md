# Prompt

创建并显示文本提示框、对话框和操作菜单。

> **说明：**
> 
> - 从API version 8 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](arkts-promptaction.md)。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

<!--Device-unnamed-export default class Prompt--><!--Device-unnamed-export default class Prompt-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ShowActionMenuOptions, Button, ShowToastOptions, ShowDialogOptions, ShowDialogSuccessResponse } from 'kits/@kit.ArkUI';
```

## showActionMenu

```TypeScript
static showActionMenu(options: ShowActionMenuOptions): void
```

显示操作菜单。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Prompt-static showActionMenu(options: ShowActionMenuOptions): void--><!--Device-Prompt-static showActionMenu(options: ShowActionMenuOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ShowActionMenuOptions](arkts-arkui-system-prompt-showactionmenuoptions-i.md) | Yes | 定义ShowActionMenu的选项。 |

## showDialog

```TypeScript
static showDialog(options: ShowDialogOptions): void
```

显示对话框。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Prompt-static showDialog(options: ShowDialogOptions): void--><!--Device-Prompt-static showDialog(options: ShowDialogOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ShowDialogOptions](arkts-arkui-promptaction-showdialogoptions-i.md) | Yes | 定义显示对话框的选项。 |

## showToast

```TypeScript
static showToast(options: ShowToastOptions): void
```

显示文本弹窗。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Prompt-static showToast(options: ShowToastOptions): void--><!--Device-Prompt-static showToast(options: ShowToastOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ShowToastOptions](arkts-arkui-system-prompt-showtoastoptions-i.md) | Yes | 定义ShowToast的选项。 |

