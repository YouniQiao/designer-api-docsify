# AutoFillExtensionContext (System API)

The AutoFillExtensionContext module provides the context environment for the AutoFillExtensionAbility. It inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md#extensioncontext).

**Inheritance/Implementation:** AutoFillExtensionContext extends ExtensionContext

**Since:** 23

<!--Device-unnamed-declare class AutoFillExtensionContext--><!--Device-unnamed-declare class AutoFillExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## reloadInModal

```TypeScript
reloadInModal(customData: CustomData): Promise<void>
```

Reload autoFillExtension in modal window.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoFillExtensionContext-reloadInModal(customData: CustomData): Promise<void>--><!--Device-AutoFillExtensionContext-reloadInModal(customData: CustomData): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customData | [CustomData](arkts-ability-customdata-i-sys.md) | Yes | User defined data. When the modal window of AutoFillExtension needs to be raised again, pass this parameter to the application framework. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | If the input parameter is not valid parameter. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |

**Examples**

When an account is selected, reloadInModal is called to trigger the autofill service again, and a modal page is started in the onFillRequest lifecycle of the AutoFillExtensionAbility.

```TypeScript
// AutoFillAbility.ts
import { AutoFillExtensionAbility, autoFillManager, UIExtensionContentSession } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class AutoFillAbility extends AutoFillExtensionAbility {
  // ...
  onFillRequest(session: UIExtensionContentSession,
    request: autoFillManager.FillRequest,
    callback: autoFillManager.FillRequestCallback) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'autofill onFillRequest');
    try {
      let storage_fill: LocalStorage = new LocalStorage(
        {
          'session': session,
          'message': "AutoFill Page",
          'fillCallback': callback,
          'viewData': request.viewData,
          'autoFillExtensionContext': this.context,
          'customData': request.customData
        } as Record<string, Object>);
      if (request.customData == undefined) {
        // Load the autofill processing page.
        session.loadContent('pages/AccountPage', storage_fill);
      } else {
        // Start a modal page.
        session.loadContent('pages/ReloadInModal', storage_fill);
      }
    } catch (err) {
      hilog.error(0x0000, 'testTag', '%{public}s', 'autofill failed to load content');
    }
  }
}
```

When the user selects an account on the account selection page, the reloadInModal API is called.

```TypeScript
// AccountPage.ets
import { autoFillManager, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct AccountPage {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  viewData: autoFillManager.ViewData | undefined = this.storage?.get<autoFillManager.ViewData>('viewData');
  context: common.AutoFillExtensionContext | undefined = this.storage?.get<common.AutoFillExtensionContext>('autoFillExtensionContext');


  build() {
    Row() {
      Column() {
        List({ space: 10, initialIndex: 0 }) {
          ListItem() {
            Text('HelloWorld789456')
              .width('100%')
              .height(40)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .borderRadius(5)
          }
          .onClick(() => {
            if (this.viewData != undefined) {
              if (this.context != undefined) {
                this.context.reloadInModal({ data: { viewData: 20, text: 'HelloWorld789456' } }).then(() => {
                  console.info('reloadInModal successfully.')
                }).catch((err: BusinessError) => {
                  console.error('reloadInModal failed.')
                })
              }
            }
          })
        }
        // ...
      }
      .width('100%')
      .shadow(ShadowStyle.OUTER_FLOATING_SM)
    }
    .height('100%')
    .shadow(ShadowStyle.OUTER_FLOATING_SM)
  }
}
```

