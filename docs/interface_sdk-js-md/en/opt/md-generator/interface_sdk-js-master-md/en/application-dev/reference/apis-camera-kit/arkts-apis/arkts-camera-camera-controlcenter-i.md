# ControlCenter

**ControlCenter** inherits from [ControlCenterQuery](arkts-camera-camera-controlcenterquery-i.md#ControlCenterQuery). It is used to enable the camera controller.

**Inheritance/Implementation:** ControlCenter extends [ControlCenterQuery](arkts-camera-camera-controlcenterquery-i.md#ControlCenterQuery)

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface ControlCenter--><!--Device-camera-interface ControlCenter-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## enableControlCenter

```TypeScript
enableControlCenter(enabled: boolean): void
```

Enables the camera controller.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ControlCenter-enableControlCenter(enabled: boolean): void--><!--Device-ControlCenter-enableControlCenter(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
