# AutoDeviceSwitch

**AutoDeviceSwitch** inherits from [AutoDeviceSwitchQuery](arkts-camera-camera-autodeviceswitchquery-i.md#AutoDeviceSwitchQuery) and is used to enable or disable automatic camera switch. This capability can be used only on foldable devices. For details about the development, see [Practices for Automatic Camera Switching (ArkTS)](../../../media/camera/camera-auto-switch.md). It is recommended that the system automatically handle input device switching, session configuration, and parameter continuity during automatic camera switch. If the system detects that the zoom ranges of the two cameras are different during camera switching, it will notify the application through the **isDeviceCapabilityChanged** field in [AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md#AutoDeviceSwitchStatus). However, the application still needs to handle the UX change. For example, for the zoom range adjustment, the application needs to call [getZoomRatioRange](arkts-camera-camera-zoomquery-i.md#getZoomRatioRange) to obtain data and update the UX. Therefore, **AutoDeviceSwitch** is more applicable to simplified UX interactions.

**Inheritance/Implementation:** AutoDeviceSwitch extends [AutoDeviceSwitchQuery](arkts-camera-camera-autodeviceswitchquery-i.md#AutoDeviceSwitchQuery)

**Since:** 23

**Deprecated since:** -1

<!--Device-camera-interface AutoDeviceSwitch--><!--Device-camera-interface AutoDeviceSwitch-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## enableAutoDeviceSwitch

```TypeScript
enableAutoDeviceSwitch(enabled: boolean): void
```

Enables or disables automatic camera switch. You can use [isAutoDeviceSwitchSupported](arkts-camera-camera-autodeviceswitchquery-i.md#isAutoDeviceSwitchSupported) to check whether the device supports automatic camera switch. > **NOTE：**> > This API is used only for foldable devices with multiple front cameras. In different fold states, the system > can automatically switch to an available front camera. It does not enable automatic switching between front and > rear cameras.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoDeviceSwitch-enableAutoDeviceSwitch(enabled: boolean): void--><!--Device-AutoDeviceSwitch-enableAutoDeviceSwitch(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) |
