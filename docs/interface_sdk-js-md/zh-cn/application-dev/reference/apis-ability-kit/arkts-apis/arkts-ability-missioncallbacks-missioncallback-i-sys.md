# MissionCallback（系统接口）

任务回调已注册@interface MissionCallback

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

## notifyMissionsChanged

```TypeScript
notifyMissionsChanged: NotifyMissionsChangedCallback
```

任务变更时由系统调用。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**示例**

ArkTS-Dyn示例:

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';

// 注册任务监听器
distributedMissionManager.registerMissionListener(
  {
    deviceId: '123456'
  },
  {
    // 任务变化时的回调，接收设备ID
    notifyMissionsChanged: (deviceId: string) => {
      console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
    },
    // 快照变化时的回调，接收设备ID和任务ID
    notifySnapshot: (deviceId: string, mission: number) => {
      console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
    },
    // 网络断开时的回调，接收设备ID和网络状态
    notifyNetDisconnect: (deviceId: string, state: number) => {
      console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
    }
  }
);
```

ArkTS-Sta示例：

```TypeScript
import distributedMissionManager from '@ohos.distributedMissionManager';

// 任务变化时的回调，接收设备ID
function notifyMissionsChanged(deviceId: string)  {
  console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
}
// 快照变化时的回调，接收设备ID和任务ID
function notifySnapshot(deviceId: string, mission: int)  {
  console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
  console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
}
// 网络断开时的回调，接收设备ID和网络状态
function notifyNetDisconnect(deviceId: string, state: int)  {
  console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
  console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
}

let deviceId: distributedMissionManager.MissionDeviceInfo = { deviceId: "123456" }
let parm:distributedMissionManager.MissionCallback = {
  notifyMissionsChanged: notifyMissionsChanged,
  notifySnapshot: notifySnapshot,
  notifyNetDisconnect: notifyNetDisconnect
}
// 注册任务监听器
distributedMissionManager.registerMissionListener(deviceId, parm);
```

## notifyNetDisconnect

```TypeScript
notifyNetDisconnect: NotifyNetDisconnectCallback
```

Called by system when network disconnect.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**示例**

ArkTS-Dyn示例:

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';

// 注册任务监听器
distributedMissionManager.registerMissionListener(
  {
    deviceId: '123456'
  },
  {
    // 任务变化时的回调，接收设备ID
    notifyMissionsChanged: (deviceId: string) => {
      console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
    },
    // 快照变化时的回调，接收设备ID和任务ID
    notifySnapshot: (deviceId: string, mission: number) => {
      console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
    },
    // 网络断开时的回调，接收设备ID和网络状态
    notifyNetDisconnect: (deviceId: string, state: number) => {
      console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
    }
  }
);
```

ArkTS-Sta示例：

```TypeScript
import distributedMissionManager from '@ohos.distributedMissionManager';

// 任务变化时的回调，接收设备ID
function notifyMissionsChanged(deviceId: string)  {
  console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
}
// 快照变化时的回调，接收设备ID和任务ID
function notifySnapshot(deviceId: string, mission: int)  {
  console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
  console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
}
// 网络断开时的回调，接收设备ID和网络状态
function notifyNetDisconnect(deviceId: string, state: int)  {
  console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
  console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
}

let deviceId: distributedMissionManager.MissionDeviceInfo = { deviceId: "123456" }
let parm:distributedMissionManager.MissionCallback = {
  notifyMissionsChanged: notifyMissionsChanged,
  notifySnapshot: notifySnapshot,
  notifyNetDisconnect: notifyNetDisconnect
}
// 注册任务监听器
distributedMissionManager.registerMissionListener(deviceId, parm);
```

## notifySnapshot

```TypeScript
notifySnapshot: NotifySnapshotCallback
```

快照发生更改时，系统会调用此函数。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**示例**

ArkTS-Dyn示例:

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';

// 注册任务监听器
distributedMissionManager.registerMissionListener(
  {
    deviceId: '123456'
  },
  {
    // 任务变化时的回调，接收设备ID
    notifyMissionsChanged: (deviceId: string) => {
      console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
    },
    // 快照变化时的回调，接收设备ID和任务ID
    notifySnapshot: (deviceId: string, mission: number) => {
      console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
    },
    // 网络断开时的回调，接收设备ID和网络状态
    notifyNetDisconnect: (deviceId: string, state: number) => {
      console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
    }
  }
);
```

ArkTS-Sta示例：

```TypeScript
import distributedMissionManager from '@ohos.distributedMissionManager';

// 任务变化时的回调，接收设备ID
function notifyMissionsChanged(deviceId: string)  {
  console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
}
// 快照变化时的回调，接收设备ID和任务ID
function notifySnapshot(deviceId: string, mission: int)  {
  console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
  console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
}
// 网络断开时的回调，接收设备ID和网络状态
function notifyNetDisconnect(deviceId: string, state: int)  {
  console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
  console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
}

let deviceId: distributedMissionManager.MissionDeviceInfo = { deviceId: "123456" }
let parm:distributedMissionManager.MissionCallback = {
  notifyMissionsChanged: notifyMissionsChanged,
  notifySnapshot: notifySnapshot,
  notifyNetDisconnect: notifyNetDisconnect
}
// 注册任务监听器
distributedMissionManager.registerMissionListener(deviceId, parm);
```
