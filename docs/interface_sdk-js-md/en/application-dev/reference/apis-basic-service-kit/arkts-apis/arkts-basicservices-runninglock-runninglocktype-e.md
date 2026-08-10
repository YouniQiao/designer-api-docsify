# RunningLockType

RunningLock锁的类型。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-runningLock-export enum RunningLockType--><!--Device-runningLock-export enum RunningLockType-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

## BACKGROUND

```TypeScript
BACKGROUND = 1
```

阻止系统睡眠的锁。

**说明：** 从API version 7开始支持，从API version 10开始废弃。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 10

<!--Device-RunningLockType-BACKGROUND = 1--><!--Device-RunningLockType-BACKGROUND = 1-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

## PROXIMITY_SCREEN_CONTROL

```TypeScript
PROXIMITY_SCREEN_CONTROL = 2
```

接近光锁，使能接近光传感器，并根据传感器与障碍物的距离远近发起亮灭屏流程。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-RunningLockType-PROXIMITY_SCREEN_CONTROL = 2--><!--Device-RunningLockType-PROXIMITY_SCREEN_CONTROL = 2-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

## BACKGROUND_USER_IDLE

```TypeScript
BACKGROUND_USER_IDLE = 129
```

阻止系统自动睡眠的后台闲时任务锁，持锁能保证一段时间用户不活动后系统不进入自动睡眠。注意：不能阻止如PC合盖等场景系统进入强制睡眠，使用方必须监听  
[进入强制睡眠公共事件](../../../reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_enter_force_sleep12)，监听到事件后释放该锁。该类型锁行为存在设备差异，使用该类型锁请参考  
[阻止系统闲时进入睡眠开发指南](../../../basic-services/powermgr/runningLock/runningLock-dev.md)。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-RunningLockType-BACKGROUND_USER_IDLE = 129--><!--Device-RunningLockType-BACKGROUND_USER_IDLE = 129-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

