# showToast

## Modules to Import

```TypeScript
import { prompt } from 'kits/@kit.ArkUI';
```

## showToast

```TypeScript
function showToast(options: ShowToastOptions): void
```

创建并显示文本提示框。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.arkui.UIContext.PromptAction#showToast

<!--Device-prompt-function showToast(options: ShowToastOptions): void--><!--Device-prompt-function showToast(options: ShowToastOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ShowToastOptions](arkts-arkui-system-prompt-showtoastoptions-i.md) | Yes | 文本弹窗选项。 |

## Examples

```TypeScript
import prompt from '@ohos.prompt'
prompt.showToast({
  message: 'Message Info',
    duration: 2000
});
```

