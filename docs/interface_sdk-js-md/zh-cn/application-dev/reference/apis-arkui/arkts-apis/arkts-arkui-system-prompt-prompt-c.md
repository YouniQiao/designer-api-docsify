# Prompt

创建并显示文本提示框、对话框和操作菜单。

> **说明：**&gt;
> - 从API version 8 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](arkts-arkui-promptaction-n.md)。

**起始版本：** 3

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { Prompt, Button, ShowActionMenuOptions, ShowDialogOptions, ShowDialogSuccessResponse, ShowToastOptions } from 'kits/@kit.ArkUI';
```

## showActionMenu

```TypeScript
static showActionMenu(options: ShowActionMenuOptions): void
```

显示操作菜单。

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowActionMenuOptions](arkts-arkui-system-prompt-showactionmenuoptions-i.md) | 是 |

## showDialog

```TypeScript
static showDialog(options: ShowDialogOptions): void
```

显示对话框。

**起始版本：** 3

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowDialogOptions](arkts-arkui-system-prompt-showdialogoptions-i.md) | 是 |

## showToast

```TypeScript
static showToast(options: ShowToastOptions): void
```

显示文本弹窗。

**起始版本：** 3

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ShowToastOptions](arkts-arkui-system-prompt-showtoastoptions-i.md) | 是 |
