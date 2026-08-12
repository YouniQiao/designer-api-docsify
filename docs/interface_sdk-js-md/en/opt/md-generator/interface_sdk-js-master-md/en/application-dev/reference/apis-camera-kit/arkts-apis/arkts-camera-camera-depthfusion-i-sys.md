# DepthFusion (System API)

Depth fusion class. It inherits from [DepthFusionQuery](arkts-camera-camera-depthfusionquery-i-sys.md#DepthFusionQuery).

**Inheritance/Implementation:** DepthFusion extends [DepthFusionQuery](arkts-camera-camera-depthfusionquery-i-sys.md#DepthFusionQuery)

**Since:** 14

<!--Device-camera-interface DepthFusion extends DepthFusionQuery--><!--Device-camera-interface DepthFusion extends DepthFusionQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## enableDepthFusion

```TypeScript
enableDepthFusion(enabled: boolean): void
```

Enables depth fusion.

**Since:** 14

<!--Device-DepthFusion-enableDepthFusion(enabled: boolean): void--><!--Device-DepthFusion-enableDepthFusion(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400201-camera-service-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function enableDepthFusion(DepthFusion: camera.DepthFusion): void {
  try {
    let enabled: boolean = true;
    DepthFusion.enableDepthFusion(enabled);
    console.info('Promise returned to indicate that enableDepthFusion method execution success.');
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to depth fusion enableDepthFusion, error code: ${err.code}.`);
  };
}
```

## isDepthFusionEnabled

```TypeScript
isDepthFusionEnabled(): boolean
```

Checks whether depth fusion is enabled.

**Since:** 14

<!--Device-DepthFusion-isDepthFusionEnabled(): boolean--><!--Device-DepthFusion-isDepthFusionEnabled(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function isDepthFusionEnabled(DepthFusion: camera.DepthFusion): boolean {
  let isEnable: boolean = false;
  try {
    isEnable = DepthFusion.isDepthFusionEnabled();
    console.info('Promise returned to indicate that isDepthFusionEnabled method execution success.');
  } catch (error) {
    let err = error as BusinessError;
    console.error(`Failed to depth fusion isDepthFusionEnabled, error code: ${err.code}.`);
  };
  return isEnable;
}
```
