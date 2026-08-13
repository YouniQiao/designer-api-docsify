# openToast

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## openToast

```TypeScript
function openToast(options: ShowToastOptions): Promise<number>
```

Shows a toast. This API uses a promise to return the toast ID. > **NOTE：**> > - Subwindows with **showMode** set to **TOP_MOST** or **SYSTEM_TOP_MOST** do not support **openToast** in input > method type windows. For details, see the constraints in the input method framework > [createPanel](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethodengine-inputmethodability-i.md#createPanel) > . > > - Directly using **openToast** can lead to the issue of > [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the > **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the > [openToast](arkts-arkui-arkui-uicontext-promptaction-c.md#openToast) API through this object.

**Since:** 18

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-promptAction-function openToast(options: ShowToastOptions): Promise<number>--><!--Device-promptAction-function openToast(options: ShowToastOptions): Promise<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ShowToastOptions](arkts-arkui-system-prompt-showtoastoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { PromptAction, UIContext } from '@kit.ArkUI';

@Entry
@Component
struct toastExample {
  @State toastId: number = 0;
  uiContext: UIContext = this.getUIContext();
  promptAction: PromptAction = this.uiContext.getPromptAction();

  build() {
    Column() {
      Button('Open Toast')
        .height(100)
        .type(ButtonType.Capsule)
        .onClick(() => {
          this.promptAction.openToast({
            message: 'Toast Message',
            duration: 10000,
          }).then((toastId: number) => {
            this.toastId = toastId;
          })
            .catch((error: BusinessError) => {
              console.error(`openToast error code is ${error.code}, message is ${error.message}`);
            })
        })
      Blank().height(50)
      Button('Close Toast')
        .height(100)
        .type(ButtonType.Capsule)
        .onClick(() => {
          try {
            this.promptAction.closeToast(this.toastId);
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`CloseToast error code is ${code}, message is ${message}`);
          }
        })
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```
