# registerMissionListener (System API)

## Modules to Import

```TypeScript
import { distributedMissionManager } from 'kits/@kit.AbilityKit';
```

## registerMissionListener

```TypeScript
function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback, callback: AsyncCallback<void>): void
```

注册任务状态监听。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback, callback: AsyncCallback<void>): void--><!--Device-distributedMissionManager-function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | Yes | 注册监听时的设备信息。 |
| options | [MissionCallback](arkts-ability-missioncallbacks-missioncallback-i-sys.md) | Yes | 注册的回调方法。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数，注册监听成功，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Implement a callback function.
function NotifyMissionsChanged(deviceId: string): void {
  console.info('NotifyMissionsChanged deviceId ' + JSON.stringify(deviceId));
}
function NotifySnapshot(deviceId: string, missionId: number): void {
  console.info('NotifySnapshot deviceId ' + JSON.stringify(deviceId));
  console.info('NotifySnapshot missionId ' + JSON.stringify(missionId));
}
function NotifyNetDisconnect(deviceId: string, state: number): void {
  console.info('NotifyNetDisconnect deviceId ' + JSON.stringify(deviceId));
  console.info('NotifyNetDisconnect state ' + JSON.stringify(state));
}
try {
  // Call registerMissionListener.
  distributedMissionManager.registerMissionListener(
    { deviceId: "" },
    {
      notifyMissionsChanged: NotifyMissionsChanged,
      notifySnapshot: NotifySnapshot,
      notifyNetDisconnect: NotifyNetDisconnect
    },
    (error: BusinessError) => {
      if (error) {
        console.error('registerMissionListener failed, cause: ' + JSON.stringify(error));
        return;
      }
      console.info('registerMissionListener finished');
    });
} catch (error) {
  console.error('registerMissionListener failed, cause: ' + JSON.stringify(error));
}
```


## registerMissionListener

```TypeScript
function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback): Promise<void>
```

注册任务状态监听。使用promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback): Promise<void>--><!--Device-distributedMissionManager-function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | Yes | 注册监听时的设备信息。 |
| options | [MissionCallback](arkts-ability-missioncallbacks-missioncallback-i-sys.md) | Yes | 注册的回调方法。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Implement a callback function.
function NotifyMissionsChanged(deviceId: string): void {
  console.info('NotifyMissionsChanged deviceId ' + JSON.stringify(deviceId));
}
function NotifySnapshot(deviceId: string, missionId: number): void {
  console.info('NotifySnapshot deviceId ' + JSON.stringify(deviceId));
  console.info('NotifySnapshot missionId ' + JSON.stringify(missionId));
}
function NotifyNetDisconnect(deviceId: string, state: number): void {
  console.info('NotifyNetDisconnect deviceId ' + JSON.stringify(deviceId));
  console.info('NotifyNetDisconnect state ' + JSON.stringify(state));
}
try {
    // Call registerMissionListener.
    distributedMissionManager.registerMissionListener(
      { deviceId: "" },
      {
        notifyMissionsChanged: NotifyMissionsChanged,
        notifySnapshot: NotifySnapshot,
        notifyNetDisconnect: NotifyNetDisconnect
      }).then(() => {
        console.info('registerMissionListener finished. ');
    }).catch((error: BusinessError) => {
        console.error('registerMissionListener failed, cause: ' + JSON.stringify(error));
    })
} catch (error) {
    console.error('registerMissionListener failed, cause: ' + JSON.stringify(error));
}
```

