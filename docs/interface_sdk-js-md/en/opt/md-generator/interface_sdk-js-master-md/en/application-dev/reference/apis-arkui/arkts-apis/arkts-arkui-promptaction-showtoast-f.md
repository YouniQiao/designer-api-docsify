# showToast

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## showToast

```TypeScript
function showToast(options: ShowToastOptions): void
```

Creates and displays a toast.

> **NOTE：**
> 
> - This API is supported since API version 9 and deprecated since API version 18. You are advised to use
[showToast](arkts-apis-uicontext-promptaction.md#showtoast) instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) method in   
[UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showToast** can lead to the issue of   
[ambiguous UI context](../../ui/arkts-global-interface.md#ambiguous-ui-context).  
> 
> - Since API version 10, you can use the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) API
in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context.  
> 
> - The toast has a fixed style and does not support content customization. For specific supported capabilities,
see [ShowToastOptions](#showtoastoptions).

**Since:** 9

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.PromptAction#showToast

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-promptAction-function showToast(options: ShowToastOptions): void--><!--Device-promptAction-function showToast(options: ShowToastOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ShowToastOptions](arkts-arkui-system-prompt-showtoastoptions-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct toastExample {
  build() {
    Column() {
      Button('Show toast').fontSize(20)
        .onClick(() => {
          try {
            promptAction.showToast({
              message: 'Hello World',
              duration: 2000
            });
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`showToast args error code is ${code}, message is ${message}`);
          };
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```

```TypeScript
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct toastExample {
  build() {
    Column() {
      Button('Show toast').fontSize(20)
        .onClick(() => {
          try {
            promptAction.showToast({
              message: 'Hello World',
              duration: 2000
            });
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`showToast args error code is ${code}, message is ${message}`);
          };
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```
