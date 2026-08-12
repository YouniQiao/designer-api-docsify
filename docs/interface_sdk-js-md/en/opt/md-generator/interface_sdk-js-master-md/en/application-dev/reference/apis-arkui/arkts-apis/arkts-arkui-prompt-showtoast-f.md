# showToast

## Modules to Import

```TypeScript
import { prompt } from '@kit.ArkUI';
```

## showToast

```TypeScript
function showToast(options: ShowToastOptions): void
```

Displays the notification text.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [showToast](ohos.arkui.UIContext.PromptAction#showToast)

<!--Device-prompt-function showToast(options: ShowToastOptions): void--><!--Device-prompt-function showToast(options: ShowToastOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ShowToastOptions](arkts-arkui-system-prompt-showtoastoptions-i.md) | Yes |

## Examples

```TypeScript
import prompt from '@ohos.prompt'
prompt.showToast({
  message: 'Message Info',
    duration: 2000
});
```
