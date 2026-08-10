# DeviceKey (System API)

设备标识。用于唯一标识一个设备及其用户，包含设备ID类型、设备ID和设备用户ID等信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-companionDeviceAuth-interface DeviceKey--><!--Device-companionDeviceAuth-interface DeviceKey-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { companionDeviceAuth } from 'kits/@kit.UserAuthenticationKit';
```

## deviceId

```TypeScript
deviceId: string
```

设备ID。设备的唯一标识字符串，具体格式由deviceIdType决定。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKey-deviceId: string--><!--Device-DeviceKey-deviceId: string-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

## deviceIdType

```TypeScript
deviceIdType: int
```

设备ID类型。用于指定设备业务标识的类型，可在[DeviceIdType](arkts-userauthentication-companiondeviceauth-deviceidtype-e-sys.md)基础上自定义扩展，如使用UNIFIED_DEVICE_ID(1)表示统一设备ID，或使用厂商自定义值（≥10000）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKey-deviceIdType: int--><!--Device-DeviceKey-deviceIdType: int-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

## deviceUserId

```TypeScript
deviceUserId: int
```

设备用户ID。设备上的用户标识，为非负整数，用于区分设备上的不同用户。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKey-deviceUserId: int--><!--Device-DeviceKey-deviceUserId: int-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

