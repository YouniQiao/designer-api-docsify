# getDialogSessionInfo (System API)

## Modules to Import

```TypeScript
import { dialogSession } from '@kit.AbilityKit';
```

## getDialogSessionInfo

```TypeScript
function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo
```

Obtains the session information based on the session ID.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-dialogSession-function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo--><!--Device-dialogSession-function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dialogSessionId | string | Yes | Session ID. |

**Return value:**

| Type | Description |
| --- | --- |
| [DialogSessionInfo](arkts-ability-dialogsession-dialogsessioninfo-i-sys.md) | Session information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
import { dialogSession, Want, UIExtensionAbility, UIExtensionContentSession } from '@kit.AbilityKit';

const TAG: string = '[testTag] UIExtAbility';

export default class UIExtAbility extends UIExtensionAbility {
  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    // want is specified by the system. dialogSessionId is a built-in parameter.
    let dialogSessionId = want?.parameters?.dialogSessionId.toString();

    // Obtain DialogSessionInfo.
    let dialogSessionInfo: dialogSession.DialogSessionInfo = dialogSession.getDialogSessionInfo(dialogSessionId);
    console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
  }
}
```


## getDialogSessionInfo

```TypeScript
function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo | null
```

Query the session info of dialog.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-dialogSession-function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo | null--><!--Device-dialogSession-function getDialogSessionInfo(dialogSessionId: string): DialogSessionInfo | null-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dialogSessionId | string | Yes | Query information by dialog session id. |

**Return value:**

| Type | Description |
| --- | --- |
| [DialogSessionInfo](arkts-ability-dialogsession-dialogsessioninfo-i-sys.md) \| null | Returns the session info when the target DialogSessionInfo of dialogSessionId exists. Returns null if the target DialogSessionInfo of dialogSessionId not exist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not system-app, can not use system-api. |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) | The specified process does not have the permission. |
| [16000006](../errorcode-ability.md#16000006-cross-user-operation-is-not-allowed) | Cross-user operations are not allowed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

See [getDialogSessionInfo](#getdialogsessioninfo)

