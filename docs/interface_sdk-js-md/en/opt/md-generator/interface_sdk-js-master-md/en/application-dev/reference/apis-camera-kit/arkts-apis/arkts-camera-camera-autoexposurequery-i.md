# AutoExposureQuery

AutoExposureQuery provides APIs to query the automatic exposure feature of a camera device. > > - In this version, a compatibility change was made that preserved the initial version information of inner > elements. As a result, you might see outer element's @since version number being higher than that of the inner > elements. However, this discrepancy does not affect the functionality of the interface.

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface AutoExposureQuery--><!--Device-camera-interface AutoExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getExposureBiasRange

```TypeScript
getExposureBiasRange(): Array<number>
```

Obtains the exposure compensation values of the camera device.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposureQuery-getExposureBiasRange(): Array<double>--><!--Device-AutoExposureQuery-getExposureBiasRange(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isExposureModeSupported

```TypeScript
isExposureModeSupported(aeMode: ExposureMode): boolean
```

Checks whether an exposure mode is supported.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposureQuery-isExposureModeSupported(aeMode: ExposureMode): boolean--><!--Device-AutoExposureQuery-isExposureModeSupported(aeMode: ExposureMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aeMode | [ExposureMode](arkts-camera-camera-exposuremode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
