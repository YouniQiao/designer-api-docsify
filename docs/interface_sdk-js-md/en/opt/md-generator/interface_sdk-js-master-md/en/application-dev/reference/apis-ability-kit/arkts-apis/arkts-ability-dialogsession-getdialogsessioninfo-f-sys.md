# getDialogSessionInfo (System API)

## Modules to Import

```TypeScript
import { dialogSession } from 'kits/@kit.AbilityKit';
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dialogSessionId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DialogSessionInfo](arkts-ability-dialogsession-dialogsessioninfo-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16000005](../errorcode-ability.md#16000005-process-permission-verification-failure) |
| [16000006](../errorcode-ability.md#16000006-crossuser-operation-is-not-allowed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
