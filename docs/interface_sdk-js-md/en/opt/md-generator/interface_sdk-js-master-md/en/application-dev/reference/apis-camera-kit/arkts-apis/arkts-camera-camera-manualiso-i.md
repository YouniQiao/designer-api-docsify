# ManualIso

ManualIso object.

**Inheritance/Implementation:** ManualIso extends [ManualIsoQuery](arkts-camera-camera-manualisoquery-i.md#ManualIsoQuery)

**Since:** 24

<!--Device-camera-interface ManualIso extends ManualIsoQuery--><!--Device-camera-interface ManualIso extends ManualIsoQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getIso

```TypeScript
getIso(): number
```

Gets current ISO.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualIso-getIso(): int--><!--Device-ManualIso-getIso(): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setIso

```TypeScript
setIso(iso: number): void
```

Sets ISO sensitivity value, within the range of getSupportedIsoRange. This control can not be effective if ExposureMode is set to EXPOSURE_MODE_LOCKED.

**Since:** 24

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-ManualIso-setIso(iso: int): void--><!--Device-ManualIso-setIso(iso: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [iso](arkts-camera-camera-isoinfo-i.md) | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
