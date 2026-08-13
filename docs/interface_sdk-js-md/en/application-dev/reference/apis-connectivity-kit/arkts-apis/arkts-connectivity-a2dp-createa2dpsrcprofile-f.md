# createA2dpSrcProfile

## Modules to Import

```TypeScript
import { a2dp } from '@kit.ConnectivityKit';
```

## createA2dpSrcProfile

```TypeScript
function createA2dpSrcProfile(): A2dpSourceProfile
```

create the instance of a2dp profile.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-a2dp-function createA2dpSrcProfile(): A2dpSourceProfile--><!--Device-a2dp-function createA2dpSrcProfile(): A2dpSourceProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| A2dpSourceProfile | Returns the instance of profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter.Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |

