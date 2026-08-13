# showToast

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## showToast

```TypeScript
function showToast(options: ShowToastOptions): void
```

Creates and displays a toast. > **NOTE：**> > - This API is supported since API version 9 and deprecated since API version 18. You are advised to use showToast instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](arkts-arkui-arkui-uicontext-uicontext-c.md#getPromptAction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showToast** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 10, you can use the [getPromptAction](arkts-arkui-arkui-uicontext-uicontext-c.md#getPromptAction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context. > > - The toast has a fixed style and does not support content customization. For specific supported capabilities, see ShowToastOptions.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** showToast

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-promptAction-function showToast(options: ShowToastOptions): void--><!--Device-promptAction-function showToast(options: ShowToastOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | ShowToastOptions | Yes | Toast configuration options. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

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

