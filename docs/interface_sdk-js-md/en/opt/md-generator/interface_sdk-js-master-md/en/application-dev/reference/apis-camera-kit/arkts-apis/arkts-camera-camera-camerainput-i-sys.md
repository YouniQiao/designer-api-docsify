# CameraInput

**CameraInput** defines the camera input object. It provides camera device information used in [Session](arkts-camera-camera-session-i.md#Session).

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface CameraInput--><!--Device-camera-interface CameraInput-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## closeDelayed

```TypeScript
closeDelayed(time: number): Promise<void>
```

Delay close camera.

**Since:** 23

**Deprecated since:** -1

<!--Device-CameraInput-closeDelayed(time: int): Promise<void>--><!--Device-CameraInput-closeDelayed(time: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| time | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## controlAuxiliary

```TypeScript
controlAuxiliary(auxiliaryType: AuxiliaryType, auxiliaryStatus: AuxiliaryStatus): Promise<void>
```

Control auxiliary.

**Since:** 23

**Deprecated since:** -1

<!--Device-CameraInput-controlAuxiliary(auxiliaryType: AuxiliaryType, auxiliaryStatus: AuxiliaryStatus): Promise<void>--><!--Device-CameraInput-controlAuxiliary(auxiliaryType: AuxiliaryType, auxiliaryStatus: AuxiliaryStatus): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| auxiliaryType | [AuxiliaryType](arkts-camera-camera-auxiliarytype-e-sys.md) | Yes |
| auxiliaryStatus | [AuxiliaryStatus](arkts-camera-camera-auxiliarystatus-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## off_cameraOcclusionDetection

```TypeScript
off(type: 'cameraOcclusionDetection', callback?: AsyncCallback<CameraOcclusionDetectionResult>): void
```

Unsubscribes from **CameraInput** occlusion events. This API uses an asynchronous callback to return the result.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraInput-off(type: 'cameraOcclusionDetection', callback?: AsyncCallback<CameraOcclusionDetectionResult>): void--><!--Device-CameraInput-off(type: 'cameraOcclusionDetection', callback?: AsyncCallback<CameraOcclusionDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cameraOcclusionDetection' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CameraOcclusionDetectionResult](arkts-camera-camera-cameraocclusiondetectionresult-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## on_cameraOcclusionDetection

```TypeScript
on(type: 'cameraOcclusionDetection', callback: AsyncCallback<CameraOcclusionDetectionResult>): void
```

Subscribes to **CameraInput** occlusion events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-CameraInput-on(type: 'cameraOcclusionDetection', callback: AsyncCallback<CameraOcclusionDetectionResult>): void--><!--Device-CameraInput-on(type: 'cameraOcclusionDetection', callback: AsyncCallback<CameraOcclusionDetectionResult>): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cameraOcclusionDetection' | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[CameraOcclusionDetectionResult](arkts-camera-camera-cameraocclusiondetectionresult-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## usedAsPosition

```TypeScript
usedAsPosition(position: CameraPosition): void
```

Sets the camera to be used as a camera at the specified position.

**Since:** 23

**Deprecated since:** -1

<!--Device-CameraInput-usedAsPosition(position: CameraPosition): void--><!--Device-CameraInput-usedAsPosition(position: CameraPosition): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
