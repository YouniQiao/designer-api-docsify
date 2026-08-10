# AutoDeviceSwitch

自动切换镜头类，继承自[AutoDeviceSwitchQuery](arkts-camera-camera-autodeviceswitchquery-i.md)，用于使能或去使能自动切换镜头。自动切换镜头能力仅支持折叠屏设备使用，详细开发指导请参考  
[自动切换摄像头实践](../../../media/camera/camera-auto-switch.md)。

使用建议：自动切换镜头功能由系统自动完成输入设备切换、会话配置和参数接续。如系统发现镜头切换时，两颗镜头的变焦范围不一致，则会通过  
[AutoDeviceSwitchStatus](arkts-camera-camera-autodeviceswitchstatus-i.md)中的isDeviceCapabilityChanged字段告知应用，但仍需要应用自己处理UX的变更（如变焦范围的调整，需要重新通过[getZoomRatioRange](arkts-camera-camera-zoomquery-i.md#getzoomratiorange)接口获取数据并更新UX），因此更适用于极简UX交互的场景。

**Inheritance/Implementation:** AutoDeviceSwitch extends [AutoDeviceSwitchQuery](arkts-camera-camera-autodeviceswitchquery-i.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-camera-interface AutoDeviceSwitch extends AutoDeviceSwitchQuery--><!--Device-camera-interface AutoDeviceSwitch extends AutoDeviceSwitchQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## Modules to Import

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## enableAutoDeviceSwitch

```TypeScript
enableAutoDeviceSwitch(enabled: boolean): void
```

使能或去使能自动切换镜头。可以先通过[isAutoDeviceSwitchSupported](arkts-camera-camera-autodeviceswitchquery-i.md#isautodeviceswitchsupported)获取当前设备是否支持自动切换镜头。

> **说明：**
> 
> 该接口仅用于有多个前置镜头的折叠设备，在不同的折叠状态下可自动切换到当前可使用的前置镜头。无法实现前后置镜头的切换。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoDeviceSwitch-enableAutoDeviceSwitch(enabled: boolean): void--><!--Device-AutoDeviceSwitch-enableAutoDeviceSwitch(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | 使能或去使能自动切换镜头。true表示使能，false表示不使能。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 7400101 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameters verification failed.<br>**Applicable version:** 19 and later |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

