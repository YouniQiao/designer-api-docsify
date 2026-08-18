# DeviceSelectCallback (System API)

```TypeScript
type DeviceSelectCallback = (selectPurpose: number) => DeviceSelectResult
```

Defines the callback triggered for the companion device selection. When the system requires the user to select a companion device (for example, when adding a template or performing authentication), this callback is triggered. The application needs to return the information about the selected device.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-companionDeviceAuth-type DeviceSelectCallback = (selectPurpose: int) => DeviceSelectResult--><!--Device-companionDeviceAuth-type DeviceSelectCallback = (selectPurpose: int) => DeviceSelectResult-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| selectPurpose | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceSelectResult](arkts-userauthentication-companiondeviceauth-deviceselectresult-i-sys.md) |
