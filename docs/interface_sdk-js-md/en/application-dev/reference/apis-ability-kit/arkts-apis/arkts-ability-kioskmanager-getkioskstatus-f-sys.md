# getKioskStatus (System API)

## Modules to Import

```TypeScript
import { kioskManager } from 'kits/@kit.AbilityKit';
```

## getKioskStatus

```TypeScript
function getKioskStatus(): Promise<KioskStatus>
```

Obtains the Kiosk mode status information, including whether the system is in kiosk mode, and the name and UID of the application that has entered Kiosk mode. This API uses a promise to return the result.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;KioskStatus & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
