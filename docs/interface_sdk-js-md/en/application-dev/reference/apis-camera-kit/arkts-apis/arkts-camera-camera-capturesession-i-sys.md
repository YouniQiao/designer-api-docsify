# CaptureSession

**CaptureSession** implements a capture session, which saves all [CameraInput](arkts-camera-camera-camerainput-i.md) and [CameraOutput](arkts-camera-camera-cameraoutput-i.md) instances required to run the camera and requests the camera to complete shooting or video recording.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [VideoSession](arkts-camera-camera-videosession-i.md)

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getBeauty

```TypeScript
getBeauty(type: BeautyType): number
```

Obtains the level of the beauty type in use.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getBeauty](arkts-camera-camera-beauty-i-sys.md#getbeauty)

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
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getSupportedBeautyRange

```TypeScript
getSupportedBeautyRange(type: BeautyType): Array<number>
```

Obtains the levels that can be set a beauty type. The beauty levels vary according to the device type. The following table is only an example. | Input Parameter | Example Return Value | Return Value Description | | ----------------| ---- | ---------| | AUTO | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |Beauty levels supported when **type** is set to **AUTO**. The value **0** means that beauty mode is disabled, and other positive values mean the corresponding automatic beauty levels. | | SKIN_SMOOTH | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | Beauty levels supported when **type** is set to **SKIN_SMOOTH**. The value **0** means that the skin smoothing feature is disabled, and other positive values mean the corresponding skin smoothing levels. | | FACE_SLENDER | [0, 1, 2, 3, 4, 5] | Beauty levels supported when **type** is set to **FACE_SLENDER**. The value **0** means that the face slimming feature is disabled, and other positive values mean the corresponding face slimming levels. | | SKIN_TONE | [-1, 16242611] | Beauty levels supported when **type** is set to **SKIN_TONE**. The value **-1** means that the skin tone perfection feature is disabled. Other non-negative values mean the skin tone perfection levels represented by RGB,for example, 16242611, which is 0xF7D7B3 in hexadecimal format, where F7, D7, and B3 represent the values of the R channel, G channel, and B channel, respectively. |

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getSupportedBeautyRange](arkts-camera-camera-beautyquery-i-sys.md#getsupportedbeautyrange)

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
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getSupportedBeautyTypes

```TypeScript
getSupportedBeautyTypes(): Array<BeautyType>
```

Obtains the supported beauty types.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [getSupportedBeautyTypes](arkts-camera-camera-beautyquery-i-sys.md#getsupportedbeautytypes)

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[BeautyType](arkts-camera-camera-beautytype-e-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## setBeauty

```TypeScript
setBeauty(type: BeautyType, value: number): void
```

Sets a beauty type and its level. Beauty mode is turned off only when all the [beauty types](arkts-camera-camera-beautytype-e-sys.md) obtained through [getSupportedBeautyTypes](#getsupportedbeautytypes) are disabled.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [setBeauty](arkts-camera-camera-beauty-i-sys.md#setbeauty)

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
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
