# AvailableDeviceStatusCallback (System API)

```TypeScript
type AvailableDeviceStatusCallback = (deviceStatusList: DeviceStatus[]) => void
```

Defines the callback triggered for receiving notifications of available device status changes. When the list of available devices changes (for example, a new device goes online or a device goes offline), the system notifies the application through this callback.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceStatusList | [DeviceStatus](arkts-userauthentication-companiondeviceauth-devicestatus-i-sys.md)[] | Yes |
