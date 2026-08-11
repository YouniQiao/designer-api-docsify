# RemoteDeviceDriver

Represents information about a remote device driver.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-deviceManager-interface RemoteDeviceDriver--><!--Device-deviceManager-interface RemoteDeviceDriver-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DriverDevelopmentKit';
```

## deviceId

```TypeScript
deviceId: long
```

ID of the peripheral device.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RemoteDeviceDriver-deviceId: long--><!--Device-RemoteDeviceDriver-deviceId: long-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

## remote

```TypeScript
remote: rpc.IRemoteObject
```

Remote driver object.

**Type:** rpc.IRemoteObject

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RemoteDeviceDriver-remote: rpc.IRemoteObject--><!--Device-RemoteDeviceDriver-remote: rpc.IRemoteObject-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

