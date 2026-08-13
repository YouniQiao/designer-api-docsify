# getMediaKeySystemUuid

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## getMediaKeySystemUuid

```TypeScript
function getMediaKeySystemUuid(name: string): string
```

Obtains the UUID of the DRM content protection system supported by the specified DRM solution.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function getMediaKeySystemUuid(name: string): string--><!--Device-drm-function getMediaKeySystemUuid(name: string): string-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | DRM solution name. You can check whether the solution name is supported by calling [isMediaKeySystemSupported](arkts-drm-drm-ismediakeysystemsupported-f.md#isMediaKeySystemSupported-2). |

**Return value:**

| Type | Description |
| --- | --- |
| string | UUID of the DRM content protection system. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The parameter check failed.Possibly because: &lt;br&gt;1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [24700201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let uuid: string = drm.getMediaKeySystemUuid("com.clearplay.drm");
  console.info("getMediaKeySystemUuid: ", uuid);
} catch (err) {
  let error = err as BusinessError;
  console.error(`getMediaKeySystemUuid ERROR: ${error}`);  
}
```

