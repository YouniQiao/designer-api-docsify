# DeviceInfo (System API)

Defines device information.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)

<!--Device-deviceManager-interface DeviceInfo--><!--Device-deviceManager-interface DeviceInfo-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DistributedServiceKit';
```

## authForm

```TypeScript
authForm: AuthForm
```

Authentication type of the device.

**Type:** [AuthForm](arkts-distributedservice-devicemanager-authform-e-sys.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 11

<!--Device-DeviceInfo-authForm: AuthForm--><!--Device-DeviceInfo-authForm: AuthForm-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## deviceId

```TypeScript
deviceId: string
```

Unique identifier of the device.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo.deviceId](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md#deviceid)

<!--Device-DeviceInfo-deviceId: string--><!--Device-DeviceInfo-deviceId: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## deviceName

```TypeScript
deviceName: string
```

Device name.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo.deviceName](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md#devicename)

<!--Device-DeviceInfo-deviceName: string--><!--Device-DeviceInfo-deviceName: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## deviceType

```TypeScript
deviceType: DeviceType
```

Device type.

**Type:** [DeviceType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-devicetype-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo.deviceType](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md#devicetype)

<!--Device-DeviceInfo-deviceType: DeviceType--><!--Device-DeviceInfo-deviceType: DeviceType-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## networkId

```TypeScript
networkId: string
```

Network ID of the device.

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 11

**Substitutes:** [@ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo.networkId](arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md#networkid)

<!--Device-DeviceInfo-networkId: string--><!--Device-DeviceInfo-networkId: string-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## range

```TypeScript
range: number
```

Distance between the discovered device and the device that initiates device discovery.

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 11

<!--Device-DeviceInfo-range: number--><!--Device-DeviceInfo-range: number-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

