# sendDialogResult (System API)

## Modules to Import

```TypeScript
import { dialogSession } from '@kit.AbilityKit';
```

## sendDialogResult

```TypeScript
function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean): Promise<void>
```

Sends a request for a dialog box. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dialogSessionId | string | Yes |
| targetWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| isAllowed | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

**Examples**

```TypeScript
import { dialogSession, Want, UIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class UIExtAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // want is specified by the system. dialogSessionId is a built-in parameter.
    let dialogSessionId = want?.parameters?.dialogSessionId.toString();

    // Obtain DialogSessionInfo.
    let dialogSessionInfo: dialogSession.DialogSessionInfo =
      dialogSession.getDialogSessionInfo(dialogSessionId);

    let isAllow: boolean = true;

    let targetWant: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    try {
      dialogSession.sendDialogResult(dialogSessionId, targetWant, isAllow, (err, data) => {
        if (err) {
          console.error(`sendDialogResult error, errorCode: ${err.code}`);
        } else {
          console.info(`sendDialogResult success`);
        }
      });
    } catch (err) {
      console.error(`sendDialogResult error, errorCode: ${(err as BusinessError).code}`);
    }
  }
}
```

```TypeScript
import { dialogSession, Want, UIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class UIExtAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // want is specified by the system. dialogSessionId is a built-in parameter.
    let dialogSessionId = want?.parameters?.dialogSessionId.toString();

    // Obtain DialogSessionInfo.
    let dialogSessionInfo: dialogSession.DialogSessionInfo = dialogSession.getDialogSessionInfo(dialogSessionId);

    let isAllow: boolean = true;

    let targetWant: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    try {
      dialogSession.sendDialogResult(dialogSessionId, targetWant, isAllow)
        .then((data) => {
          console.info(`sendDialogResult success, pid: ${data}`);
        }, (err: BusinessError) => {
          console.error(`sendDialogResult error, errorCode: ${err.code}`);
        });
    } catch (err) {
      console.error(`sendDialogResult error, errorCode: ${(err as BusinessError).code}`);
    }
  }
}
```


## sendDialogResult

```TypeScript
function sendDialogResult(dialogSessionId: string, targetWant: Want, isAllowed: boolean, callback: AsyncCallback<void>): void
```

Sends a request for a dialog box. This API uses an asynchronous callback to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dialogSessionId | string | Yes |
| targetWant | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
| isAllowed | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

**Examples**

See [sendDialogResult](#senddialogresult)
