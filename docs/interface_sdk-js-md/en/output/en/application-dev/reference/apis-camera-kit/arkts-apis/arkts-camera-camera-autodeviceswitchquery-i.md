# AutoDeviceSwitchQuery

**AutoDeviceSwitchQuery** is used to check whether a device supports automatic camera switch. [Automatic Camera Switching]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ is supported only on foldable devices. For details about how to enable this capability, see [enableAutoDeviceSwitch]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

<!--Device-camera-interface AutoDeviceSwitchQuery--><!--Device-camera-interface AutoDeviceSwitchQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

## isAutoDeviceSwitchSupported

```TypeScript
isAutoDeviceSwitchSupported(): boolean
```

Checks whether the device supports automatic camera switch.

**Since:** 13

**ArkTS mode:** ArkTS-Dyn since version 13; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-AutoDeviceSwitchQuery-isAutoDeviceSwitchSupported(): boolean--><!--Device-AutoDeviceSwitchQuery-isAutoDeviceSwitchSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for the support of automatic camera switch. **true** if supported, **false** |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 13 - 17 |

