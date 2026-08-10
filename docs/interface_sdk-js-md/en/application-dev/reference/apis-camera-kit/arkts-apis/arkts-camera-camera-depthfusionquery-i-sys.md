# DepthFusionQuery (System API)

A class for querying depth fusion capabilities.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-camera-interface DepthFusionQuery--><!--Device-camera-interface DepthFusionQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getDepthFusionThreshold

ArkTS-Dyn:
```TypeScript
getDepthFusionThreshold(): Array<number>
```

ArkTS-Sta:
```TypeScript
getDepthFusionThreshold(): Array<double>
```

Obtains the depth fusion threshold.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-DepthFusionQuery-getDepthFusionThreshold(): Array<double>--><!--Device-DepthFusionQuery-getDepthFusionThreshold(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;double&gt; | Depth fusion threshold. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |
| 202 | Not System Application. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getDepthFusionThreshold(DepthFusionQuery: camera.DepthFusionQuery): void {
  try {
    let threshold: Array<number> = DepthFusionQuery.getDepthFusionThreshold();
    console.info('Promise returned to indicate that getDepthFusionThreshold method execution success.');
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to depth fusion query  getDepthFusionThreshold, error code: ${err.code}.`);
  }
}
```

## isDepthFusionSupported

```TypeScript
isDepthFusionSupported(): boolean
```

Checks whether depth fusion is supported.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-DepthFusionQuery-isDepthFusionSupported(): boolean--><!--Device-DepthFusionQuery-isDepthFusionSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of depth fusion. **true** if supported, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |
| 202 | Not System Application. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function isDepthFusionSupported(DepthFusionQuery: camera.DepthFusionQuery): void {
  try {
    let isSupported: boolean = DepthFusionQuery.isDepthFusionSupported();
    console.info('Indicate that isDepthFusionSupported method execution success.');
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to depth fusion query  isDepthFusionSupported, error code: ${err.code}.`);
  }
}
```

