# AppServiceExtensionContext

The AppServiceExtensionContext module provides the context environment for the [AppServiceExtensionAbility](arkts-ability-app-ability-appserviceextensionability-appserviceextensionability-c.md#AppServiceExtensionAbility). It inherits from [ExtensionContext](arkts-ability-extensioncontext-c.md#ExtensionContext). AppServiceExtensionContext provides APIs to connect to and disconnect from a ServiceExtensionAbility (an ExtensionAbility for system application background services), as well as to terminate an AppServiceExtensionAbility. Note that a ServiceExtensionAbility can only be developed by system applications and supports connections from third- party applications. > **NOTE：**> > - The APIs of this module must be used in the main thread, but not in child threads such as Worker and TaskPool.

**Inheritance/Implementation:** AppServiceExtensionContext extends ExtensionContext

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class AppServiceExtensionContext--><!--Device-unnamed-declare class AppServiceExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## connectServiceExtensionAbility

```TypeScript
connectServiceExtensionAbility(want: Want, callback: ConnectOptions): number
```

Connects this AppServiceExtensionAbility to a ServiceExtensionAbility. It enables communication with the ServiceExtensionAbility via a proxy, allowing access to the capabilities exposed by the ServiceExtensionAbility. This API can be called only by the main thread.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionContext-connectServiceExtensionAbility(want: Want, callback: ConnectOptions): long--><!--Device-AppServiceExtensionContext-connectServiceExtensionAbility(want: Want, callback: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| callback | [ConnectOptions](arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { AppServiceExtensionAbility, Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let commRemote: rpc.IRemoteObject | null = null; // Release the instance when the connection is disconnected.
const TAG: string = '[AppServiceExtensionAbility]';

export default class AppServiceExtension extends AppServiceExtensionAbility {
  connection: number = 0;

  onCreate(localWant: Want) {
    let want: Want = {
      bundleName: 'com.example.myapp',
      abilityName: 'MyAbility'
    };
    let callback: common.ConnectOptions = {
      onConnect(elementName, remote) {
        commRemote = remote;
        hilog.info(0x0000, TAG, '----------- onConnect -----------');
      },
      onDisconnect(elementName) {
        hilog.info(0x0000, TAG, '----------- onDisconnect -----------');
      },
      onFailed(code) {
        hilog.error(0x0000, TAG, '----------- onFailed -----------');
      }
    };


    try {
      this.connection = this.context.connectServiceExtensionAbility(want, callback);
    } catch (paramError) {
      commRemote = null;
      // Process input parameter errors.
      hilog.error(0x0000, TAG, `error.code: ${(paramError as BusinessError).code}, error.message: ${(paramError as BusinessError).message}`);
    }
  }

  onDestroy(): void {
    this.context.disconnectServiceExtensionAbility(this.connection).then(() => {
      commRemote = null;
      // Carry out normal service processing.
      hilog.info(0x0000, TAG, '----------- disconnectServiceExtensionAbility success -----------');
    })
      .catch((error: BusinessError) => {
        commRemote = null;
        // Process service logic errors.
        hilog.error(0x0000, TAG, `disconnectServiceExtensionAbility failed, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }
}
```

## disconnectServiceExtensionAbility

```TypeScript
disconnectServiceExtensionAbility(connection: number): Promise<void>
```

Disconnects this AppServiceExtensionAbility from a ServiceExtensionAbility. This API can be called only by the main thread. It uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>--><!--Device-AppServiceExtensionContext-disconnectServiceExtensionAbility(connection: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connection | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

For details, see [connectServiceExtensionAbility](#connectServiceExtensionAbility).

## startAbility

```TypeScript
startAbility(want: Want, options?: StartOptions): Promise<void>
```

Starts the UIAbility. This API can be called only by the main thread. It uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>--><!--Device-AppServiceExtensionContext-startAbility(want: Want, options?: StartOptions): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| options | [StartOptions](arkts-ability-app-ability-startoptions-startoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000055](../errorcode-ability.md#16000055-installationfree-timeout) |
| [16000080](../errorcode-ability.md#16000080-new-instances-cannot-be-created) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000019](../errorcode-ability.md#16000019-no-matching-ability-is-found-during-implicit-startup) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000071](../errorcode-ability.md#16000071-application-clone-is-not-supported) |
| [16000001](../errorcode-ability.md#16000001-ability-name-does-not-exist) |
| [16000002](../errorcode-ability.md#16000002-incorrect-ability-type) |
| [16000012](../errorcode-ability.md#16000012-application-under-control) |
| [16000076](../errorcode-ability.md#16000076-appinstancekey-does-not-exist) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [16000077](../errorcode-ability.md#16000077-number-of-application-instances-reaches-the-upper-limit) |
| [16000078](../errorcode-ability.md#16000078-multiinstance-mode-is-not-supported) |
| [16000079](../errorcode-ability.md#16000079-appinstancekey-cannot-be-specified) |
| [16000008](../errorcode-ability.md#16000008-crowdtesting-application-expires) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |
| [16000010](../errorcode-ability.md#16000010-continuation-flag-is-forbidden) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { AppServiceExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAppServiceExtensionAbility extends AppServiceExtensionAbility {
  onCreate(want: Want) {
    let wantInfo: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbility(wantInfo, options)
        .then(() => {
          // Carry out normal service processing.
          console.info('startAbility succeed');
        })
        .catch((err: BusinessError) => {
          // Process service logic errors.
          console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // Process input parameter errors.
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbility failed, code is ${code}, message is ${message}`);
    }
  }
}
```

## terminateSelf

```TypeScript
terminateSelf(): Promise<void>
```

Terminates this AppServiceExtensionAbility. This API can be called only by the main thread. It uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-AppServiceExtensionContext-terminateSelf(): Promise<void>--><!--Device-AppServiceExtensionContext-terminateSelf(): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000009](../errorcode-ability.md#16000009-ability-start-or-stop-failure-in-wukong-mode) |
| [16000011](../errorcode-ability.md#16000011-context-does-not-exist) |

## Examples

```TypeScript
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtensionAbility]';

export default class AppServiceExtension extends AppServiceExtensionAbility {
  onCreate(want: Want) {
    this.context.terminateSelf().then(() => {
      // Carry out normal service processing.
      hilog.info(0x0000, TAG, '----------- terminateSelf succeed -----------');
    }).catch((error: BusinessError) => {
      // Process service logic errors.
      hilog.error(0x0000, TAG, `terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
    });
  }
}
```
