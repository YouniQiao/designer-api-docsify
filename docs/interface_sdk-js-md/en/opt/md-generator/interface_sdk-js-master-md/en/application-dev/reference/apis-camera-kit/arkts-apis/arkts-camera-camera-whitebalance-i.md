# WhiteBalance

**WhiteBalance** inherits from [WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md#WhiteBalanceQuery).

It provides APIs to process white balance, including obtaining and setting the white balance mode and white balance value.

**Inheritance/Implementation:** WhiteBalance extends [WhiteBalanceQuery](arkts-camera-camera-whitebalancequery-i.md#WhiteBalanceQuery)

**Since:** 20

<!--Device-camera-interface WhiteBalance extends WhiteBalanceQuery--><!--Device-camera-interface WhiteBalance extends WhiteBalanceQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getColorTint

```TypeScript
getColorTint(): number
```

Gets current color tint.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WhiteBalance-getColorTint(): int--><!--Device-WhiteBalance-getColorTint(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |

## getWhiteBalance

```TypeScript
getWhiteBalance(): number
```

Obtains the current white balance value.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WhiteBalance-getWhiteBalance(): int--><!--Device-WhiteBalance-getWhiteBalance(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getWhiteBalanceGains

```TypeScript
getWhiteBalanceGains(): WhiteBalanceGains
```

Gets RGB white balance gain values.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WhiteBalance-getWhiteBalanceGains(): WhiteBalanceGains--><!--Device-WhiteBalance-getWhiteBalanceGains(): WhiteBalanceGains-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WhiteBalanceGains](arkts-camera-camera-whitebalancegains-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getWhiteBalanceMode

```TypeScript
getWhiteBalanceMode(): WhiteBalanceMode
```

Obtains the white balance mode in use.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WhiteBalance-getWhiteBalanceMode(): WhiteBalanceMode--><!--Device-WhiteBalance-getWhiteBalanceMode(): WhiteBalanceMode-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WhiteBalanceMode](arkts-camera-camera-whitebalancemode-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setColorTint

```TypeScript
setColorTint(colorTint: number): void
```

Sets color tint.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-WhiteBalance-setColorTint(colorTint: int): void--><!--Device-WhiteBalance-setColorTint(colorTint: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| colorTint | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |

## setWhiteBalance

```TypeScript
setWhiteBalance(whiteBalance: number): void
```

Sets a white balance value.Before the setting, run  
[getWhiteBalanceRange](arkts-camera-camera-whitebalancequery-i.md#getWhiteBalanceRange) to check the white balance value range supported by the device.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WhiteBalance-setWhiteBalance(whiteBalance: int): void--><!--Device-WhiteBalance-setWhiteBalance(whiteBalance: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [whiteBalance](../../apis-image-kit/arkts-apis/arkts-image-image-exifmetadata-c.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setWhiteBalanceGains

```TypeScript
setWhiteBalanceGains(gains: WhiteBalanceGains): void
```

Sets RGB white balance gain values.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-WhiteBalance-setWhiteBalanceGains(gains: WhiteBalanceGains): void--><!--Device-WhiteBalance-setWhiteBalanceGains(gains: WhiteBalanceGains): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| gains | [WhiteBalanceGains](arkts-camera-camera-whitebalancegains-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setWhiteBalanceMode

```TypeScript
setWhiteBalanceMode(mode: WhiteBalanceMode): void
```

Sets a white balance mode. Before the setting, run  
[isWhiteBalanceModeSupported](arkts-camera-camera-whitebalancequery-i.md#isWhiteBalanceModeSupported)to check whether the device supports the specified white balance mode.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-WhiteBalance-setWhiteBalanceMode(mode: WhiteBalanceMode): void--><!--Device-WhiteBalance-setWhiteBalanceMode(mode: WhiteBalanceMode): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [WhiteBalanceMode](arkts-camera-camera-whitebalancemode-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
