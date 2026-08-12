# CaptureSession

**CaptureSession** implements a capture session, which saves all [CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput) and   
[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput) instances required to run the camera and requests the camera to complete shooting or video recording.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [VideoSession](arkts-camera-camera-videosession-i.md#VideoSession)

<!--Device-camera-interface CaptureSession--><!--Device-camera-interface CaptureSession-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getBeauty

```TypeScript
getBeauty(type: BeautyType): number
```

Obtains the level of the beauty type in use.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getBeauty](arkts-camera-camera-beauty-i-sys.md#getBeauty)

<!--Device-CaptureSession-getBeauty(type: BeautyType): number--><!--Device-CaptureSession-getBeauty(type: BeautyType): number-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |

## Examples

```TypeScript
function getBeauty(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let beautyTypes: Array<camera.BeautyType> = captureSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return invalidValue;
  }
  let beautyLevels: Array<number> = captureSession.getSupportedBeautyRange(beautyTypes[0]);
  if (beautyLevels === undefined || beautyLevels.length <= 0) {
    return invalidValue;
  }
  captureSession.setBeauty(beautyTypes[0], beautyLevels[0]);
  let beautyLevel: number = captureSession.getBeauty(beautyTypes[0]);
  return beautyLevel;
}
```

## getSupportedBeautyRange

```TypeScript
getSupportedBeautyRange(type: BeautyType): Array<number>
```

Obtains the levels that can be set a beauty type. The beauty levels vary according to the device type. The following table is only an example.  
| Input Parameter | Example Return Value | Return Value Description |
| ----------------| ---- | ---------|
| AUTO | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |Beauty levels supported when **type** is set to **AUTO**. The value **0** means that beauty mode is disabled, and other positive values mean the corresponding automatic beauty levels. |
| [SKIN_SMOOTH](arkts-camera-camera-beautytype-e-sys.md) | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | Beauty levels supported when **type** is set to **SKIN_SMOOTH**. The value **0** means that the skin smoothing feature is disabled, and other positive values mean the corresponding skin smoothing levels. |
| [FACE_SLENDER](arkts-camera-camera-beautytype-e-sys.md) | [0, 1, 2, 3, 4, 5] | Beauty levels supported when **type** is set to **FACE_SLENDER**. The value **0** means that the face slimming feature is disabled, and other positive values mean the corresponding face slimming levels. |
| [SKIN_TONE](arkts-camera-camera-beautytype-e-sys.md) | [-1, 16242611] |

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getSupportedBeautyRange](arkts-camera-camera-beautyquery-i-sys.md#getSupportedBeautyRange)

<!--Device-CaptureSession-getSupportedBeautyRange(type: BeautyType): Array<number>--><!--Device-CaptureSession-getSupportedBeautyRange(type: BeautyType): Array<number>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |

## Examples

```TypeScript
function getSupportedBeautyRange(captureSession: camera.CaptureSession): Array<number> {
  let beautyTypes: Array<camera.BeautyType> = captureSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return [];
  }
  let beautyLevels: Array<number> = captureSession.getSupportedBeautyRange(beautyTypes[0]);
  return beautyLevels;
}
```

## getSupportedBeautyTypes

```TypeScript
getSupportedBeautyTypes(): Array<BeautyType>
```

Obtains the supported beauty types.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getSupportedBeautyTypes](arkts-camera-camera-beautyquery-i-sys.md#getSupportedBeautyTypes)

<!--Device-CaptureSession-getSupportedBeautyTypes(): Array<BeautyType>--><!--Device-CaptureSession-getSupportedBeautyTypes(): Array<BeautyType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[BeautyType](arkts-camera-camera-beautytype-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |

## Examples

```TypeScript
function getSupportedBeautyTypes(captureSession: camera.CaptureSession): Array<camera.BeautyType> {
  let beautyTypes: Array<camera.BeautyType> = captureSession.getSupportedBeautyTypes();
  return beautyTypes;
}
```

## setBeauty

```TypeScript
setBeauty(type: BeautyType, value: number): void
```

Sets a beauty type and its level. Beauty mode is turned off only when all the  
[beauty types](arkts-camera-camera-beautytype-e-sys.md#BeautyType) obtained through  
[getSupportedBeautyTypes](#getSupportedBeautyTypes) are disabled.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [setBeauty](arkts-camera-camera-beauty-i-sys.md#setBeauty)

<!--Device-CaptureSession-setBeauty(type: BeautyType, value: number): void--><!--Device-CaptureSession-setBeauty(type: BeautyType, value: number): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | Yes |
| value | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |

## Examples

```TypeScript
function setBeauty(captureSession: camera.CaptureSession): void {
  let beautyTypes: Array<camera.BeautyType> = captureSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return;
  }
  let beautyLevels: Array<number> = captureSession.getSupportedBeautyRange(beautyTypes[0]);
  if (beautyLevels === undefined || beautyLevels.length <= 0) {
    return;
  }
  captureSession.setBeauty(beautyTypes[0], beautyLevels[0]);
}
```
