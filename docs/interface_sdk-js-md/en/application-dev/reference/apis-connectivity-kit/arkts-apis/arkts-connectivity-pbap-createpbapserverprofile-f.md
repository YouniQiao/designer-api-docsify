# createPbapServerProfile

## Modules to Import

```TypeScript
import { pbap } from '@kit.ConnectivityKit';
```

## createPbapServerProfile

```TypeScript
function createPbapServerProfile(): PbapServerProfile
```

create the instance of PBAP server profile.

**Since:** 11

<!--Device-pbap-function createPbapServerProfile(): PbapServerProfile--><!--Device-pbap-function createPbapServerProfile(): PbapServerProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| [PbapServerProfile](arkts-connectivity-pbap-pbapserverprofile-i-sys.md) | Returns the instance of pbap profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes:         1. The hardware does not support the capability;         2. The chip does not support the capability;         3. A dependent service feature is not supported. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let pbapServerProfile = pbap.createPbapServerProfile();
    console.info('pbapServer success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
