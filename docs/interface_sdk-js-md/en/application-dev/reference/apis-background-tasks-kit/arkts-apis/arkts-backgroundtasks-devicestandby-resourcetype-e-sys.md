# ResourceType (System API)

非待机应用资源枚举。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-deviceStandby-export enum ResourceType--><!--Device-deviceStandby-export enum ResourceType-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## NETWORK

```TypeScript
NETWORK = 1
```

网络访问资源。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceType-NETWORK = 1--><!--Device-ResourceType-NETWORK = 1-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## RUNNING_LOCK

```TypeScript
RUNNING_LOCK = 1 << 1
```

cpu-runninglock资源。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceType-RUNNING_LOCK = 1 << 1--><!--Device-ResourceType-RUNNING_LOCK = 1 << 1-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## TIMER

```TypeScript
TIMER = 1 << 2
```

timer任务资源。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceType-TIMER = 1 << 2--><!--Device-ResourceType-TIMER = 1 << 2-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## WORK_SCHEDULER

```TypeScript
WORK_SCHEDULER = 1 << 3
```

work任务资源。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceType-WORK_SCHEDULER = 1 << 3--><!--Device-ResourceType-WORK_SCHEDULER = 1 << 3-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## AUTO_SYNC

```TypeScript
AUTO_SYNC = 1 << 4
```

自动同步的资源。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceType-AUTO_SYNC = 1 << 4--><!--Device-ResourceType-AUTO_SYNC = 1 << 4-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## PUSH

```TypeScript
PUSH = 1 << 5
```

pushkit资源。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceType-PUSH = 1 << 5--><!--Device-ResourceType-PUSH = 1 << 5-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

## FREEZE

```TypeScript
FREEZE = 1 << 6
```

冻结应用资源。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-ResourceType-FREEZE = 1 << 6--><!--Device-ResourceType-FREEZE = 1 << 6-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

**System API:** This is a system API.

