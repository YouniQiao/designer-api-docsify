# CameraOutput

CameraOutput implements output information used in [Session](arkts-camera-camera-session-i.md). It is the base class of   
**output**.

**Since:** 10

<!--Device-camera-interface CameraOutput--><!--Device-camera-interface CameraOutput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

Releases output resources. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraOutput-release(callback: AsyncCallback<void>): void--><!--Device-CameraOutput-release(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |

## release

```TypeScript
release(): Promise<void>
```

Releases output resources. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-CameraOutput-release(): Promise<void>--><!--Device-CameraOutput-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
