# AvailableDeviceStatusCallback（系统接口）

```TypeScript
type AvailableDeviceStatusCallback = (deviceStatusList: DeviceStatus[]) => void
```

回调函数，用于接收可添加的设备列表变化通知。当可添加的伴随设备列表发生变化（如新设备上线、设备离线等）时，系统会通过此回调通知应用。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-companionDeviceAuth-type AvailableDeviceStatusCallback = (deviceStatusList: DeviceStatus[]) => void--><!--Device-companionDeviceAuth-type AvailableDeviceStatusCallback = (deviceStatusList: DeviceStatus[]) => void-End-->

**系统能力：** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceStatusList | [DeviceStatus](arkts-userauthentication-companiondeviceauth-devicestatus-i-sys.md)[] | 是 |
