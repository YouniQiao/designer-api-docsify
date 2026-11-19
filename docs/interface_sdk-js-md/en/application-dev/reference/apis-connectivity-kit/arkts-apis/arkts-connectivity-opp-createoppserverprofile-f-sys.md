# createOppServerProfile (System API)

## Modules to Import

```TypeScript
import { opp } from '@kit.ConnectivityKit';
```

## createOppServerProfile

```TypeScript
function createOppServerProfile(): OppServerProfile
```

create the instance of OPP server profile.

**Since:** 16

**Model restriction:** This API can be used only in the stage model.

<!--Device-opp-function createOppServerProfile(): OppServerProfile--><!--Device-opp-function createOppServerProfile(): OppServerProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [OppServerProfile](arkts-connectivity-opp-oppserverprofile-i-sys.md) | Returns the instance of opp profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
