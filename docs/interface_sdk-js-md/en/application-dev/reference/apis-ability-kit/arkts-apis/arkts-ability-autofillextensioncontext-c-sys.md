# AutoFillExtensionContext (System API)

```TypeScript
declare class AutoFillExtensionContext extends ExtensionContext
```

The AutoFillExtensionContext module provides the context environment for the AutoFillExtensionAbility. It inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md).

**Inheritance/Implementation:** AutoFillExtensionContext extends [ExtensionContext](arkts-ability-extensioncontext-c.md)

**Since:** 11

<!--Device-unnamed-declare class AutoFillExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class AutoFillExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
```

Connects this AutoFillExtensionAbility to a ServiceExtensionAbility. It enables communication with the ServiceExtensionAbility via a proxy, allowing access to the capabilities exposed by the ServiceExtensionAbility. ServiceExtensionAbility is a special type of [ExtensionAbility](../../../application-models/extensionability-overview.md) provided by the system. It is designed to offer background services for specific scenarios and is not customizable by developers. It can be connected to by other components and handles requests in the background based on the caller information.

> **NOTE:** 
> 
> For details about the startup rules for the components in the stage model, see
> [Component Startup Rules (Stage Model)](../../../application-models/component-startup-rules.md).

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoFillExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long--><!--Device-AutoFillExtensionContext-connectServiceExtensionAbility(want: Want, options: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes | Want information required for connecting to the ServiceExtensionAbility, including the ability name and bundle name. |
| options | [ConnectOptions](arkts-ability-connectoptions-i.md) | Yes | Callback used to return the information indicating that the connection is successful, failed, or interrupted. |

**Return value:**

| Type | Description |
| --- | --- |
| number | Connection ID. The client can call [disconnectServiceExtensionAbility](#disconnectserviceextensionability) with this ID for disconnection. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) | The specified ability does not exist. |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) | Incorrect ability type. |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) | Cannot start an invisible component. |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) | The crowdtesting application expires. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000012](../errorcode-ability.md#16000012-application-under-control) | The application is controlled. |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) | The application is controlled by EDM. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1.Connect to system service failed. 2.System service failed to communicate with dependency module. |
| [16000053](../errorcode-ability.md#16000053-ability-not-in-the-foreground) | The ability is not on the top of the UI. |
| [16000055](../errorcode-ability.md#16000055-installation-free-timeout) | Installation-free timed out. |
| [16000070](../errorcode-ability.md#16000070-extensionability-fails-to-start-a-serviceextensionability-in-strict-mode) | The extension cannot start the service. |

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

Disconnects from a ServiceExtensionAbility. Once the connection is terminated, set the remote object, which is returned when the connection is established, to null. This API uses a promise to return the result. ServiceExtensionAbility is a special type of [ExtensionAbility](../../../application-models/extensionability-overview.md) provided by the system. It is designed to offer background services for specific scenarios and is not customizable by developers. It can be connected to by other components and handles requests in the background based on the caller information.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoFillExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-AutoFillExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| connection | number | Yes | ID of the connected ServiceExtensionAbility, that is, **connectionId** returned by [connectServiceExtensionAbility](#connectserviceextensionability). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. Possible causes: 1.Connect to system service failed. 2.System service failed to communicate with dependency module. |

## reloadInModal

```TypeScript
reloadInModal(customData: CustomData): Promise<void>
```

Reloads the modal page. This API uses a promise to return the result.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoFillExtensionContext-reloadInModal(customData: CustomData): Promise<void>--><!--Device-AutoFillExtensionContext-reloadInModal(customData: CustomData): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customData | [CustomData](arkts-ability-customdata-i-sys.md) | Yes | Custom information for raising the modal page. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | If the input parameter is not valid parameter. |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) | The context does not exist. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

<!--Del-->
**Examples**

The autofill service is triggered when a user touches the account and password text box, and an account selection page is displayed in the onFillRequest lifecycle of the [AutoFillExtensionAbility](arkts-ability-app-ability-autofillextensionability-autofillextensionability-c-sys.md).

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
      // Create a LocalStorage and store the data required for autofill.
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
                // Call the reloadInModal API to retrigger autofill and pass custom data for the modal page.
                this.context.reloadInModal({ data: { viewData: 20, text: 'HelloWorld789456' } }).then(() => {
                  console.info('reloadInModal successfully.')
                }).catch((err: BusinessError) => {
                  console.error(`reloadInModal failed. Code: ${err.code}, message: ${err.message}`);
                })
              }
            }
          });
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

<!--DelEnd-->
