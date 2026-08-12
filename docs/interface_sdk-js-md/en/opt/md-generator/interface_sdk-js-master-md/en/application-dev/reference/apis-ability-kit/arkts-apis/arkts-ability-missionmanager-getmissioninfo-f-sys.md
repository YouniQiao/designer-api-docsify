# getMissionInfo (System API)

## Modules to Import

```TypeScript
import { missionManager } from '@kit.AbilityKit';
```

## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: number, callback: AsyncCallback<MissionInfo>): void
```

Obtains the mission information. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int, callback: AsyncCallback<MissionInfo>): void--><!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int, callback: AsyncCallback<MissionInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| missionId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;MissionInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
function getMissionInfo(deviceId: string, missionId: number): Promise<MissionInfo>
```

Obtains the mission information. This API uses a promise to return the result.

**Since:** 9

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int): Promise<MissionInfo>--><!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int): Promise<MissionInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| missionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;MissionInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
