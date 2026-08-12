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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-a2dp-function createA2dpSrcProfile(): A2dpSourceProfile--><!--Device-a2dp-function createA2dpSrcProfile(): A2dpSourceProfile-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Return value:**

| Type | Description |
| --- | --- |
| A2dpSourceProfile | Returns the instance of profile. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Invalid parameter.Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |

