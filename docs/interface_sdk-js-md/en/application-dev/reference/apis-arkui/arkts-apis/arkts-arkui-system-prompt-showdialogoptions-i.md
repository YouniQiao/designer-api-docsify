# ShowDialogOptions

定义显示对话框的选项。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

<!--Device-unnamed-export interface ShowDialogOptions--><!--Device-unnamed-export interface ShowDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ShowActionMenuOptions, Button, ShowToastOptions, ShowDialogOptions, ShowDialogSuccessResponse } from 'kits/@kit.ArkUI';
```

## cancel

```TypeScript
cancel?: (data: string, code: string) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-cancel?: (data: string, code: string) => void--><!--Device-ShowDialogOptions-cancel?: (data: string, code: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | string | Yes |  |

## complete

```TypeScript
complete?: (data: string) => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-complete?: (data: string) => void--><!--Device-ShowDialogOptions-complete?: (data: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |

## success

```TypeScript
success?: (data: ShowDialogSuccessResponse) => void
```

接口调用成功的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-success?: (data: ShowDialogSuccessResponse) => void--><!--Device-ShowDialogOptions-success?: (data: ShowDialogSuccessResponse) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [ShowDialogSuccessResponse](arkts-arkui-promptaction-showdialogsuccessresponse-i.md) | Yes |  |

## buttons

```TypeScript
buttons?: [Button, Button?, Button?]
```

对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。

**Type:** [Button, Button?, Button?]

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-buttons?: [Button, Button?, Button?]--><!--Device-ShowDialogOptions-buttons?: [Button, Button?, Button?]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## message

```TypeScript
message?: string
```

文本内容。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-message?: string--><!--Device-ShowDialogOptions-message?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
title?: string
```

标题文本。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShowDialogOptions-title?: string--><!--Device-ShowDialogOptions-title?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

