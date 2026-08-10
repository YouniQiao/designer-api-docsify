# ShowActionMenuOptions

定义ShowActionMenu的选项。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

<!--Device-unnamed-export interface ShowActionMenuOptions--><!--Device-unnamed-export interface ShowActionMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ShowActionMenuOptions, Button, ShowToastOptions, ShowDialogOptions, ShowDialogSuccessResponse } from 'kits/@kit.ArkUI';
```

## complete

```TypeScript
complete?: () => void
```

关闭对话框时调用。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowActionMenuOptions-complete?: () => void--><!--Device-ShowActionMenuOptions-complete?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fail

```TypeScript
fail?: (errMsg: string) => void
```

接口调用失败的回调函数。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowActionMenuOptions-fail?: (errMsg: string) => void--><!--Device-ShowActionMenuOptions-fail?: (errMsg: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errMsg | string | Yes |  |

## success

```TypeScript
success?: (tapIndex: number, errMsg: string) => void
```

弹出对话框时调用。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowActionMenuOptions-success?: (tapIndex: number, errMsg: string) => void--><!--Device-ShowActionMenuOptions-success?: (tapIndex: number, errMsg: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tapIndex | number | Yes |  |
| errMsg | string | Yes |  |

## buttons

```TypeScript
buttons: [Button, Button?, Button?, Button?, Button?, Button?]
```

对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。

**Type:** [Button, Button?, Button?, Button?, Button?, Button?]

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowActionMenuOptions-buttons: [Button, Button?, Button?, Button?, Button?, Button?]--><!--Device-ShowActionMenuOptions-buttons: [Button, Button?, Button?, Button?, Button?, Button?]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string
```

标题文本。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowActionMenuOptions-title?: string--><!--Device-ShowActionMenuOptions-title?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

