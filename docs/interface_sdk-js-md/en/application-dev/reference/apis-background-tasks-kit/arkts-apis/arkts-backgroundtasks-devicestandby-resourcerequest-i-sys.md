# ResourceRequest (System API)

The request of standby resources.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-deviceStandby-export interface ResourceRequest--><!--Device-deviceStandby-export interface ResourceRequest-End-->

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

The exemption duration.&lt;br&gt;Unit:s

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceRequest-duration: int--><!--Device-ResourceRequest-duration: int-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## name

```TypeScript
name: string
```

The application name.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceRequest-name: string--><!--Device-ResourceRequest-name: string-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## reason

```TypeScript
reason: string
```

The reason for the request.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceRequest-reason: string--><!--Device-ResourceRequest-reason: string-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## resourceTypes

```TypeScript
resourceTypes: int
```

The set of resource types that an application requests.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceRequest-resourceTypes: int--><!--Device-ResourceRequest-resourceTypes: int-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## uid

```TypeScript
uid: int
```

The application uid.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceRequest-uid: int--><!--Device-ResourceRequest-uid: int-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

