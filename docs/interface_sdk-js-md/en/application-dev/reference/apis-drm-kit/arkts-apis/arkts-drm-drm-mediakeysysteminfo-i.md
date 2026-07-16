# MediaKeySystemInfo

Used to indicate the media key system info of media source.

**Since:** 12

<!--Device-drm-interface MediaKeySystemInfo--><!--Device-drm-interface MediaKeySystemInfo-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## pssh

```TypeScript
pssh: Uint8Array
```

PSSH(protection scheme specific header) contain drm info.

**Type:** Uint8Array

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySystemInfo-pssh: Uint8Array--><!--Device-MediaKeySystemInfo-pssh: Uint8Array-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

## uuid

```TypeScript
uuid: string
```

Drm system ID.

**Type:** string

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MediaKeySystemInfo-uuid: string--><!--Device-MediaKeySystemInfo-uuid: string-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

