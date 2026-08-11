# AutoExposureQuery

AutoExposureQuery provides APIs to query the automatic exposure feature of a camera device.  
> 
> - In this version, a compatibility change was made that preserved the initial version information of inner
> elements. As a result, you might see outer element's @since version number being higher than that of the inner
> elements. However, this discrepancy does not affect the functionality of the interface.

**Since:** 12

<!--Device-camera-interface AutoExposureQuery--><!--Device-camera-interface AutoExposureQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getExposureBiasRange

```TypeScript
getExposureBiasRange(): Array<number>
```

Obtains the exposure compensation values of the camera device.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoExposureQuery-getExposureBiasRange(): Array<double>--><!--Device-AutoExposureQuery-getExposureBiasRange(): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isExposureMeteringModeSupported

```TypeScript
isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean
```

Checks whether the specified exposure metering mode is supported.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-AutoExposureQuery-isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean--><!--Device-AutoExposureQuery-isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| aeMeteringMode | [ExposureMeteringMode](arkts-camera-camera-exposuremeteringmode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isExposureModeSupported

```TypeScript
isExposureModeSupported(aeMode: ExposureMode): boolean
```

Checks whether an exposure mode is supported.

**Since:** 11

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
