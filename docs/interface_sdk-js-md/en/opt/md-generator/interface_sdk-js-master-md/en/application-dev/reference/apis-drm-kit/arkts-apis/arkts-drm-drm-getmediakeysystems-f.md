# getMediaKeySystems

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## getMediaKeySystems

```TypeScript
function getMediaKeySystems(): MediaKeySystemDescription[]
```

Obtains the list of plugins supported by the device.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function getMediaKeySystems(): MediaKeySystemDescription[]--><!--Device-drm-function getMediaKeySystems(): MediaKeySystemDescription[]-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaKeySystemDescription](arkts-drm-drm-mediakeysystemdescription-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [24700201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700201-service-exception) |
| [24700101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700101-unknown-error) |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';

let description: drm.MediaKeySystemDescription[] = drm.getMediaKeySystems();
// Verify the returned result. description indicates the plugin information list, including the plugin names and unique IDs.
if (description.length > 0) {
  console.info(`getMediaKeySystems success, count: ${description.length}`);
  for (let i = 0; i < description.length; i++) {
    console.info(`name: ${description[i].name}, uuid: ${description[i].uuid}`);
  }
} else {
  console.info('No DRM system available');
}
```
