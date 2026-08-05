# AutoDeviceSwitch

**AutoDeviceSwitch** inherits from [AutoDeviceSwitchQuery]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and is used to enable or disable automatic camera switch. This capability can be used only on foldable devices. For details about the development, see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. It is recommended that the system automatically handle input device switching, session configuration, and parameter continuity during automatic camera switch. If the system detects that the zoom ranges of the two cameras are different during camera switching, it will notify the application through the **isDeviceCapabilityChanged** field in [AutoDeviceSwitchStatus]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. However, the application still needs to handle the UX change. For example, for the zoom range adjustment, the application needs to call [getZoomRatioRange]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ to obtain data and update the UX. Therefore, **AutoDeviceSwitch** is more applicable to simplified UX interactions.

**Inheritance/Implementation:** AutoDeviceSwitch extends [AutoDeviceSwitchQuery](arkts-camera-camera-autodeviceswitchquery-i.md)

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-camera-interface AutoDeviceSwitch extends AutoDeviceSwitchQuery--><!--Device-camera-interface AutoDeviceSwitch extends AutoDeviceSwitchQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## enableAutoDeviceSwitch

```TypeScript
enableAutoDeviceSwitch(enabled: boolean): void
```

Enables or disables automatic camera switch. You can use [isAutoDeviceSwitchSupported]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ to check whether the device supports automatic camera switch. > **NOTE** > > This API is used only for foldable devices with multiple front cameras. In different fold states, the system > can automatically switch to an available front camera. It does not enable automatic switching between front and > rear cameras.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoDeviceSwitch-enableAutoDeviceSwitch(enabled: boolean): void--><!--Device-AutoDeviceSwitch-enableAutoDeviceSwitch(enabled: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable automatic camera switch. **true** to enable, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400102](../errorcode-camera.md#7400102-invalid-operation) | Operation not allowed. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config. |
| [7400201](../errorcode-camera.md#7400201-camera-service-error) | Camera service fatal error. |
| [7400101](../errorcode-camera.md#7400101-invalid-parameter) | Parameter error. Possible causes:1. Mandatory parameters are left unspecified; 2. Incorrect parameter types;3. Parameters verification failed.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 19 and later |

