# MissionCallback (System API)

MissionCallback registered by app.

@interface MissionCallback

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## notifyMissionsChanged

```TypeScript
notifyMissionsChanged: NotifyMissionsChangedCallback
```

Called by system when mission changed.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Examples**

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';

distributedMissionManager.registerMissionListener(
  {
    deviceId: '123456'
  },
  {
    notifyMissionsChanged: (deviceId: string) => {
      console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
    },
    notifySnapshot: (deviceId: string, mission: number) => {
      console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
    },
    notifyNetDisconnect: (deviceId: string, state: number) => {
      console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
    }
  }
);
```

## notifyNetDisconnect

```TypeScript
notifyNetDisconnect: NotifyNetDisconnectCallback
```

Called by system when network disconnect.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Examples**

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';

distributedMissionManager.registerMissionListener(
  {
    deviceId: '123456'
  },
  {
    notifyMissionsChanged: (deviceId: string) => {
      console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
    },
    notifySnapshot: (deviceId: string, mission: number) => {
      console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
    },
    notifyNetDisconnect: (deviceId: string, state: number) => {
      console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
    }
  }
);
```

## notifySnapshot

```TypeScript
notifySnapshot: NotifySnapshotCallback
```

Called by system when snapshot changed.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Examples**

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';

distributedMissionManager.registerMissionListener(
  {
    deviceId: '123456'
  },
  {
    notifyMissionsChanged: (deviceId: string) => {
      console.info(`notifyMissionsChanged deviceId: ${JSON.stringify(deviceId)}`);
    },
    notifySnapshot: (deviceId: string, mission: number) => {
      console.info(`notifySnapshot deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifySnapshot mission: ${JSON.stringify(mission)}`);
    },
    notifyNetDisconnect: (deviceId: string, state: number) => {
      console.info(`notifyNetDisconnect deviceId: ${JSON.stringify(deviceId)}`);
      console.info(`notifyNetDisconnect state: ${JSON.stringify(state)}`);
    }
  }
);
```
