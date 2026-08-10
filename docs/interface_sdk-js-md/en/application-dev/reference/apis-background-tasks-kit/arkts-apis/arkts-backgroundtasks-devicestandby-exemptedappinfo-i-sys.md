# ExemptedAppInfo (System API)

豁免应用信息，未进入待机管控的应用信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-deviceStandby-export interface ExemptedAppInfo--><!--Device-deviceStandby-export interface ExemptedAppInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceStandby } from 'kits/@kit.BackgroundTasksKit';
```

## duration

```TypeScript
duration: int
```

豁免时长。单位：s

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ExemptedAppInfo-duration: int--><!--Device-ExemptedAppInfo-duration: int-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## name

```TypeScript
name: string
```

应用名。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ExemptedAppInfo-name: string--><!--Device-ExemptedAppInfo-name: string-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## resourceTypes

```TypeScript
resourceTypes: int
```

资源类型，类型具体说明请参考[ResourceType](arkts-backgroundtasks-devicestandby-resourcetype-e-sys.md)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ExemptedAppInfo-resourceTypes: int--><!--Device-ExemptedAppInfo-resourceTypes: int-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

