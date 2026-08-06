# showToast

## showToast

```TypeScript
function showToast(options: ShowToastOptions): void
```

Displays the notification text.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.arkui.UIContext.PromptAction#showToast

<!--Device-prompt-function showToast(options: ShowToastOptions): void--><!--Device-prompt-function showToast(options: ShowToastOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Options. |

**Example**

```TypeScript
import prompt from '@ohos.prompt'
prompt.showToast({
  message: 'Message Info',
    duration: 2000
});
```

