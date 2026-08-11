# DeviceInfo（系统接口）

设备详细信息。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-deviceManager-interface DeviceInfo--><!--Device-deviceManager-interface DeviceInfo-End-->

**系统能力：** SystemCapability.Driver.ExternalDevice

**系统接口：** 此接口为系统接口。

## deviceId

```TypeScript
deviceId: long
```

设备ID。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-DeviceInfo-deviceId: long--><!--Device-DeviceInfo-deviceId: long-End-->

**系统能力：** SystemCapability.Driver.ExternalDevice

**系统接口：** 此接口为系统接口。

## driverUid

```TypeScript
driverUid?: string
```

设备匹配的驱动UID。

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-DeviceInfo-driverUid?: string--><!--Device-DeviceInfo-driverUid?: string-End-->

**系统能力：** SystemCapability.Driver.ExternalDevice

**系统接口：** 此接口为系统接口。

## isDriverMatched

```TypeScript
isDriverMatched: boolean
```

设备是否匹配到驱动。`true`：匹配到驱动；`false`：未匹配到驱动。

**类型：** boolean

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-DeviceInfo-isDriverMatched: boolean--><!--Device-DeviceInfo-isDriverMatched: boolean-End-->

**系统能力：** SystemCapability.Driver.ExternalDevice

**系统接口：** 此接口为系统接口。

