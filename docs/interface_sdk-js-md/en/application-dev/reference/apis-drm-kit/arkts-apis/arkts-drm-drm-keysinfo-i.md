# KeysInfo

Used to indicate the media key status with a key and its value.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drm-interface KeysInfo--><!--Device-drm-interface KeysInfo-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

## Modules to Import

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## keyId

```TypeScript
keyId: Uint8Array
```

Keys Id in media key.

**Type:** Uint8Array

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeysInfo-keyId: Uint8Array--><!--Device-KeysInfo-keyId: Uint8Array-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

## value

```TypeScript
value: string
```

Keys status description.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeysInfo-value: string--><!--Device-KeysInfo-value: string-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

