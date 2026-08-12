# CameraOutput

CameraOutput implements output information used in [Session](arkts-camera-camera-session-i.md#Session). It is the base class of   
**output**.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-camera-interface CameraOutput--><!--Device-camera-interface CameraOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases output resources. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraOutput-release(callback: AsyncCallback<void>): void--><!--Device-CameraOutput-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the output resources are released successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in [CameraErrorCode](arkts-camera-camera-cameraerrorcode-e.md#CameraErrorCode). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

## release

```TypeScript
release(): Promise<void>
```

Releases output resources. This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraOutput-release(): Promise<void>--><!--Device-CameraOutput-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |

