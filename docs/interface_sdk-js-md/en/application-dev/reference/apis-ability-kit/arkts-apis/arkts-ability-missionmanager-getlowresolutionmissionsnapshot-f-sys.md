# getLowResolutionMissionSnapShot (System API)

## Modules to Import

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## getLowResolutionMissionSnapShot

```TypeScript
function getLowResolutionMissionSnapShot(
    deviceId: string,
    missionId: int,
    callback: AsyncCallback<MissionSnapshot>
  ): void
```

获取任务低分辨率快照。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getLowResolutionMissionSnapShot(    deviceId: string,    missionId: int,    callback: AsyncCallback<MissionSnapshot>  ): void--><!--Device-missionManager-function getLowResolutionMissionSnapShot(    deviceId: string,    missionId: int,    callback: AsyncCallback<MissionSnapshot>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 设备ID，本机默认为空字符串。 |
| missionId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 任务ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;MissionSnapshot&gt; | Yes | 执行结果回调函数，返回任务快照信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Not system application. |

## Examples

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testMissionId = 2;

try {
  missionManager.getLowResolutionMissionSnapShot('', testMissionId,
    (err: BusinessError, data: missionManager.MissionSnapshot) => {
      if (err) {
        console.error(`getLowResolutionMissionSnapShot failed: ${err.message}`);
      } else {
        console.info(`getLowResolutionMissionSnapShot successfully: ${JSON.stringify(data)}`);
      }
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getLowResolutionMissionSnapShot failed: ${err.message}`);
}
```


## getLowResolutionMissionSnapShot

```TypeScript
function getLowResolutionMissionSnapShot(deviceId: string, missionId: int): Promise<MissionSnapshot>
```

获取任务低分辨率快照。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getLowResolutionMissionSnapShot(deviceId: string, missionId: int): Promise<MissionSnapshot>--><!--Device-missionManager-function getLowResolutionMissionSnapShot(deviceId: string, missionId: int): Promise<MissionSnapshot>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 设备ID，本机默认为空字符串。 |
| missionId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 任务ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;MissionSnapshot&gt; | Promise对象，返回任务快照信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Not system application. |

## Examples

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testMissionId = 2;

try {
  missionManager.getLowResolutionMissionSnapShot('', testMissionId).then((data: missionManager.MissionSnapshot) => {
    console.info(`getLowResolutionMissionSnapShot successfully. Data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`getLowResolutionMissionSnapShot failed. Cause: ${error.message}`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getLowResolutionMissionSnapShot failed. Cause: ${err.message}`);
}
```

