# AutoDeviceSwitchQuery

**AutoDeviceSwitchQuery** is used to check whether a device supports automatic camera switch.

[Automatic Camera Switching](arkts-camera-camera-autodeviceswitch-i.md#enableAutoDeviceSwitch) is supported only on foldable devices. For details about how to enable this capability, see   
[enableAutoDeviceSwitch](arkts-camera-camera-autodeviceswitch-i.md#enableAutoDeviceSwitch).

**Since:** 13

<!--Device-camera-interface AutoDeviceSwitchQuery--><!--Device-camera-interface AutoDeviceSwitchQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## isAutoDeviceSwitchSupported

```TypeScript
isAutoDeviceSwitchSupported(): boolean
```

Checks whether the device supports automatic camera switch.

**Since:** 13

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoDeviceSwitchQuery-isAutoDeviceSwitchSupported(): boolean--><!--Device-AutoDeviceSwitchQuery-isAutoDeviceSwitchSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
