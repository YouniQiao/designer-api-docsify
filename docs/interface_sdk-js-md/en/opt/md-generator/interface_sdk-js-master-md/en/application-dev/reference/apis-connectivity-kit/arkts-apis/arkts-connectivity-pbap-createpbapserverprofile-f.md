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

**Since:** 26.0.0

**Deprecated since:** -1

<!--Device-pbap-function createPbapServerProfile(): PbapServerProfile--><!--Device-pbap-function createPbapServerProfile(): PbapServerProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PbapServerProfile](arkts-connectivity-pbap-pbapserverprofile-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let pbapServerProfile = pbap.createPbapServerProfile();
    console.info('pbapServer success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
