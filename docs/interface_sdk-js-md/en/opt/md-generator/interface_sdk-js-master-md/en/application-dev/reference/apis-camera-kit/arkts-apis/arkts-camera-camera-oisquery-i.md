# OISQuery

OIS (Optical Image Stabilization) query interface.

**Since:** 24

**Deprecated since:** -1

<!--Device-camera-interface OISQuery--><!--Device-camera-interface OISQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getCurrentCustomOISBias

```TypeScript
getCurrentCustomOISBias(oisAxis: OISAxes): number
```

Gets the current custom bias value for the specified OIS axis.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-OISQuery-getCurrentCustomOISBias(oisAxis: OISAxes): double--><!--Device-OISQuery-getCurrentCustomOISBias(oisAxis: OISAxes): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oisAxis | [OISAxes](arkts-camera-camera-oisaxes-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getCurrentOISMode

```TypeScript
getCurrentOISMode(): OISMode
```

Gets the current OIS mode.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-OISQuery-getCurrentOISMode(): OISMode--><!--Device-OISQuery-getCurrentOISMode(): OISMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OISMode](arkts-camera-camera-oismode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getSupportedOISBiasRange

```TypeScript
getSupportedOISBiasRange(oisAxis: OISAxes): Array<number>
```

Gets the supported bias range for the specified OIS axis.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-OISQuery-getSupportedOISBiasRange(oisAxis: OISAxes): Array<double>--><!--Device-OISQuery-getSupportedOISBiasRange(oisAxis: OISAxes): Array<double>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oisAxis | [OISAxes](arkts-camera-camera-oisaxes-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## getSupportedOISBiasStep

```TypeScript
getSupportedOISBiasStep(oisAxis: OISAxes): number
```

Gets the bias step for the specified OIS axis.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-OISQuery-getSupportedOISBiasStep(oisAxis: OISAxes): double--><!--Device-OISQuery-getSupportedOISBiasStep(oisAxis: OISAxes): double-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oisAxis | [OISAxes](arkts-camera-camera-oisaxes-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |

## isOISModeSupported

```TypeScript
isOISModeSupported(mode: OISMode): boolean
```

Checks if the specified OIS mode is supported.

**Since:** 24

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-OISQuery-isOISModeSupported(mode: OISMode): boolean--><!--Device-OISQuery-isOISModeSupported(mode: OISMode): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [OISMode](arkts-camera-camera-oismode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
