# getMissionInfo (System API)

## Modules to Import

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: int, callback: AsyncCallback<MissionInfo>): void
```

获取任务信息。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int, callback: AsyncCallback<MissionInfo>): void--><!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int, callback: AsyncCallback<MissionInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 设备ID，本机默认为空字符串。 |
| missionId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 任务ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;MissionInfo&gt; | Yes | 执行结果回调函数，返回任务信息。 |

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

let testMissionId = 1;

missionManager.getMissionInfos('', 10)
  .then((allMissions: Array<missionManager.MissionInfo>) => {
    try {
      if (allMissions && allMissions.length > 0) {
        testMissionId = allMissions[0].missionId;
      }

      missionManager.getMissionInfo('', testMissionId, (error: BusinessError, mission: missionManager.MissionInfo) => {
        if (error) {
          console.error(`getMissionInfo failed, error.code: ${error.code}, error.message: ${error.message}`);
        } else {
          console.info(`mission.missionId = ${mission.missionId}`);
          console.info(`mission.runningState = ${mission.runningState}`);
          console.info(`mission.lockedState = ${mission.lockedState}`);
          console.info(`mission.timestamp = ${mission.timestamp}`);
          console.info(`mission.label = ${mission.label}`);
          console.info(`mission.iconPath = ${mission.iconPath}`);
        }
      });
    } catch (paramError) {
      let code = (paramError as BusinessError).code;
      let message = (paramError as BusinessError).message;
      console.error(`error: ${code}, ${message} `);
    }
  })
  .catch((error: BusinessError) => {
    console.error(`getMissionInfos failed, error code: ${error.code}, error msg: ${error.message}.`);
  });
```


## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: int): Promise<MissionInfo>
```

获取任务信息。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int): Promise<MissionInfo>--><!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int): Promise<MissionInfo>-End-->

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
| Promise&lt;MissionInfo&gt; | Promise对象，返回任务信息。 |

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

let testMissionId = 1;

try {
  missionManager.getMissionInfo('', testMissionId)
    .then((data: missionManager.MissionInfo) => {
      console.info(`getMissionInfo successfully. Data: ${JSON.stringify(data)}`);
    })
    .catch((error: BusinessError) => {
      console.error(`getMissionInfo failed. Cause: ${error.message}`);
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getMissionInfo failed. Cause: ${err.message}`);
}
```

