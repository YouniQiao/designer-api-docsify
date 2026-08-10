# DeviceProfileInfoFilterOptions (System API)

设备信息过滤器选项。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-distributedDeviceManager-interface DeviceProfileInfoFilterOptions--><!--Device-distributedDeviceManager-interface DeviceProfileInfoFilterOptions-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { distributedDeviceManager } from 'kits/@kit.DistributedServiceKit';
```

## deviceIdList

```TypeScript
deviceIdList?: Array<string>
```

表示获取指定deviceId的设备信息，deviceId一般为设备的UDID，如设备无UDID，则取其MAC或SN作为deviceId。默认为空。

**Type:** Array&lt;string&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-DeviceProfileInfoFilterOptions-deviceIdList?: Array<string>--><!--Device-DeviceProfileInfoFilterOptions-deviceIdList?: Array<string>-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## isCloud

```TypeScript
isCloud : boolean
```

表示是否需要实时从云端获取设备列表。

- false：表示从设备获取。  
- true：表示从云端获取。

**Type:** boolean

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-DeviceProfileInfoFilterOptions-isCloud : boolean--><!--Device-DeviceProfileInfoFilterOptions-isCloud : boolean-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

