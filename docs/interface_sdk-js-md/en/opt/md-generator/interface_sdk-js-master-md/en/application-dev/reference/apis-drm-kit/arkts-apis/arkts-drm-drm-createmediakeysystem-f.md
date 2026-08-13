# createMediaKeySystem

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## createMediaKeySystem

```TypeScript
function createMediaKeySystem(name: string): MediaKeySystem
```

Creates a MediaKeySystem instance.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem--><!--Device-drm-function createMediaKeySystem(name: string): MediaKeySystem-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [MediaKeySystem](arkts-drm-drm-mediakeysystem-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [24700201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700201-service-exception) |
| [24700101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700101-unknown-error) |
| [24700103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-drm-kit/errorcode-drm.md#24700103-too-many-mediakeysystem-instances) |

## Examples

```TypeScript
import { drm } from '@kit.DrmKit';
// name indicates the DRM solution name. You can obtain the DRM solution name supported by the device through the drm.getMediaKeySystems API, for example, **com.clearplay.drm**.
let name = 'com.clearplay.drm';
let mediaKeySystem: drm.MediaKeySystem = drm.createMediaKeySystem(name);
console.info(`createMediaKeySystem success, name: ${name}`);
```
