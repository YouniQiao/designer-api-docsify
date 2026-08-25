# getMediaKeySystems

## Modules to Import

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## getMediaKeySystems

```TypeScript
function getMediaKeySystems(): MediaKeySystemDescription[]
```

Obtains the list of plugins supported by the device.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaKeySystemDescription](arkts-drm-drm-mediakeysystemdescription-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [24700101](../errorcode-drm.md#24700101-unknown-error) |
| [24700201](../errorcode-drm.md#24700201-service-exception) |
