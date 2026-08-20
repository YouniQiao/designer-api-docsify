# ExemptedAppInfo (System API)

Information about an exempted application.

@interface ExemptedAppInfo

**Since:** 23

<!--Device-deviceStandby-export interface ExemptedAppInfo--><!--Device-deviceStandby-export interface ExemptedAppInfo-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceStandby } from '@kit.BackgroundTasksKit';
```

## duration

```TypeScript
duration: int
```

The exemption duration. <br>Unit:s

**Type:** int

**Since:** 23

<!--Device-ExemptedAppInfo-duration: int--><!--Device-ExemptedAppInfo-duration: int-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## name

```TypeScript
name: string
```

The application name.

**Type:** string

**Since:** 23

<!--Device-ExemptedAppInfo-name: string--><!--Device-ExemptedAppInfo-name: string-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## resourceTypes

```TypeScript
resourceTypes: int
```

The set of resource types that an application requests.

**Type:** int

**Since:** 23

<!--Device-ExemptedAppInfo-resourceTypes: int--><!--Device-ExemptedAppInfo-resourceTypes: int-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

