# getMediaKeySystems

## Modules to Import

```TypeScript
import { drm } from 'drm';
```

## getMediaKeySystems

```TypeScript
function getMediaKeySystems(): MediaKeySystemDescription[]
```

Obtains the list of plugins supported by the device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function getMediaKeySystems(): MediaKeySystemDescription[]--><!--Device-drm-function getMediaKeySystems(): MediaKeySystemDescription[]-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| Type | Description |
| --- | --- |
| [MediaKeySystemDescription](arkts-drm-drm-mediakeysystemdescription-i.md)[] | Array of supported plugins. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [24700201](../errorcode-drm.md#24700201-service-exception) | Fatal service error, for example, service died. |
| [24700101](../errorcode-drm.md#24700101-unknown-error) | All unknown errors. |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getMediaKeySystems ERROR: ${error}`);  
}
```

