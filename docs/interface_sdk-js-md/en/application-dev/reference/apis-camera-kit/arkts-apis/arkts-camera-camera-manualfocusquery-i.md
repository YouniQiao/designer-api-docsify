# ManualFocusQuery

Manual Focus Query object.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-camera-interface ManualFocusQuery--><!--Device-camera-interface ManualFocusQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## isFocusDistanceSupported

```TypeScript
isFocusDistanceSupported(): boolean
```

Checks whether a focus distance is supported.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualFocusQuery-isFocusDistanceSupported(): boolean--><!--Device-ManualFocusQuery-isFocusDistanceSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Is focus distance supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

