# DeviceSelectCallback (System API)

```TypeScript
type DeviceSelectCallback = (selectPurpose: int) => DeviceSelectResult
```

Defines the callback triggered for the companion device selection. When the system requires the user to select a companion device (for example, when adding a template or performing authentication), this callback is triggered. The application needs to return the information about the selected device.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-type DeviceSelectCallback = (selectPurpose: int) => DeviceSelectResult--><!--Device-companionDeviceAuth-type DeviceSelectCallback = (selectPurpose: int) => DeviceSelectResult-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectPurpose | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Selection purpose. It identifies the purpose of the current device selection. For details about the value, see [SelectPurpose]\_\_\_JSDOC\_LINK\_USD\_0\_\_\_. **SELECT\_ADD\_DEVICE(1)** means to select the device for adding a template, and **SELECT\_AUTH\_DEVICE(2)** means to select the device for authentication. Vendors can customize the extended value (greater than or equal to 10000). The application should return the corresponding device list based on the selection purpose.  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Device selection result. It contains the device information list (**deviceKeys**) |

