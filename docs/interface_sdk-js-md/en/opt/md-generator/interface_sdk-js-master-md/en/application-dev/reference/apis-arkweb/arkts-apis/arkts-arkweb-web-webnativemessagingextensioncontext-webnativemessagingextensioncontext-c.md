# WebNativeMessagingExtensionContext

WebNativeMessagingExtensionContext is the runtime context of the native web message extension ( [WebNativeMessagingExtensionAbility](arkts-arkweb-web-webnativemessagingextensionability-webnativemessagingextensionability-c.md#webnativemessagingextensionability)). It inherits from ExtensionContext and provides lifecycle management, ability startup, and native message connection control capabilities for the extension ability. In an extension that inherits from WebNativeMessagingExtensionAbility, developers can obtain this context through `this.context` and then call [startAbility](#startability) to start another ability, call [startAbilityForResult](#startabilityforresult) to start a UIAbility and receive the return result, call [terminateSelf](#terminateself) to terminate the current extension, or call [stopNativeConnection](#stopnativeconnection) to stop a specified native web message connection.

**Inheritance/Implementation:** WebNativeMessagingExtensionContext extends ExtensionContext

**Since:** 21

<!--Device-unnamed-export default class WebNativeMessagingExtensionContext--><!--Device-unnamed-export default class WebNativeMessagingExtensionContext-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

Starts an ability. This API uses a promise to return the result. To obtain the return result when the started UIAbility exits, use [startAbilityForResult](#startabilityforresult).

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebNativeMessagingExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-WebNativeMessagingExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-installationfree-timeout) |
| [16000080](../../apis-ability-kit/errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000019](../../apis-ability-kit/errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000071](../../apis-ability-kit/errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000076](../../apis-ability-kit/errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../../apis-ability-kit/errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../../apis-ability-kit/errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../../apis-ability-kit/errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../../apis-ability-kit/errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../../apis-ability-kit/errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

**Examples**

```TypeScript
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const abilityWant: Want = {
      bundleName: 'com.example.mybundle',
      abilityName: 'MainAbility'
    };
    try {
      const context = this.context; // Obtain the WebNativeMessagingExtensionContext instance.
      context.startAbility(abilityWant).then(() => {
        console.info('Ability started successfully');
      }).catch((err: BusinessError) => {
        console.error(`Failed to start ability. Code: ${(err as BusinessError).code},
          Message: ${(err as BusinessError).message}`);
      });
    } catch (err) {
      console.error(`Failed to start ability. Code: ${(err as BusinessError).code},
      Message: ${(err as BusinessError).message}`);
    }
  }
}
```

## startAbilityForResult

```TypeScript
startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
```

Starts a UIAbility. This API uses a promise to return the result when the started UIAbility exits. After the UIAbility is started, the following situations may occur: - Under normal circumstances, [terminateSelfWithResult](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md#terminateselfwithresult) can be called to terminate the UIAbility and return the result to the caller. - In abnormal cases, such as when the UIAbility is destroyed, exception information is returned to the caller, with resultCode set to -1. - Only UIAbilities of the current app can be started.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebNativeMessagingExtensionContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>--><!--Device-WebNativeMessagingExtensionContext-startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityResult](../../apis-ability-kit/arkts-apis/arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000055](../../apis-ability-kit/errorcode-ability.md#16000055-installationfree-timeout) |
| [16000080](../../apis-ability-kit/errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000019](../../apis-ability-kit/errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000004](../../apis-ability-kit/errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../../apis-ability-kit/errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000071](../../apis-ability-kit/errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../../apis-ability-kit/errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../../apis-ability-kit/errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../../apis-ability-kit/errorcode-ability.md#16000012-application-under-control) |
| [16000076](../../apis-ability-kit/errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../../apis-ability-kit/errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../../apis-ability-kit/errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../../apis-ability-kit/errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../../apis-ability-kit/errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../../apis-ability-kit/errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../../apis-ability-kit/errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../../apis-ability-kit/errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000010](../../apis-ability-kit/errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

**Examples**

```TypeScript
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { Want, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const abilityWant: Want = {
      bundleName: 'com.example.mybundle', // Replace with the actual bundleName.
      abilityName: 'MainAbility' // Replace with the actual abilityName.
    };
    try {
      const context = this.context; // Obtain the WebNativeMessagingExtensionContext instance.
      context.startAbilityForResult(abilityWant).then((result: common.AbilityResult) => {
        console.info(`Ability started successfully, result code: ${result.resultCode}`);
        if (result.want) {
          console.info(`Result data: ${JSON.stringify(result.want)}`);
        }
      }).catch((err: BusinessError) => {
        console.error(`Failed to start ability. Code: ${(err as BusinessError).code},
        Message:${(err as BusinessError).message}`);
      });
    } catch (err) {
      console.error(`Failed to start ability. Code: ${(err as BusinessError).code},
      Message: ${(err as BusinessError).message}`);
    }
  }
}
```

## stopNativeConnection

```TypeScript
stopNativeConnection(connectionId: number): Promise<void>
```

Stops the specified native connection. This API uses a promise to return the result.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebNativeMessagingExtensionContext-stopNativeConnection(connectionId: number): Promise<void>--><!--Device-WebNativeMessagingExtensionContext-stopNativeConnection(connectionId: number): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connectionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

**Examples**

```TypeScript
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const CONNECTION_ID = 12345; // Actual connection ID.
    try {
        const context = this.context;// Obtain the WebNativeMessagingExtensionContext instance.
        context.stopNativeConnection(CONNECTION_ID).then(() => {
          console.info('Native connection stopped successfully');
        }).catch((err: BusinessError) => {
          console.error(`Failed to stop native connection. Code: ${(err as BusinessError).code},
          Message: ${(err as BusinessError).message}`);
        })
    } catch (err) {
        console.error(`Failed to stop native connection. Code: ${(err as BusinessError).code},
        Message: ${(err as BusinessError).message}`);
    }
  }
}
```

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

Destroys the current native web message extension. This method returns a promise for asynchronous processing. Calling this method automatically stops all native web message connections, so there is no need to call stopNativeConnection.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebNativeMessagingExtensionContext-terminateSelf(): Promise<void>--><!--Device-WebNativeMessagingExtensionContext-terminateSelf(): Promise<void>-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000009](../../apis-ability-kit/errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000011](../../apis-ability-kit/errorcode-ability.md#16000011-context-does-not-exist) |

**Examples**

```TypeScript
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    try {
        const context = this.context; // Obtain the WebNativeMessagingExtensionContext instance.
        context.terminateSelf().then(() => {
          console.info('Extension terminated successfully');
        }).catch((err: BusinessError) => {
          console.error(`Failed to terminate extension. Code: ${(err as BusinessError).code},
          Message: ${(err as BusinessError).message}`);
        });       
    } catch (err) {
        console.error(`Failed to terminate extension. Code: ${(err as BusinessError).code},
        Message: ${(err as BusinessError).message}`);
    }
  }
}
```
