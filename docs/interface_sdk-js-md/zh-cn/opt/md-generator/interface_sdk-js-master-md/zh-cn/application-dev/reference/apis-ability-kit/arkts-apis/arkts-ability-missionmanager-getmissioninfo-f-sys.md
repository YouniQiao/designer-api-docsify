# getMissionInfo（系统接口）

## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: number, callback: AsyncCallback<MissionInfo>): void
```

获取任务信息。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int, callback: AsyncCallback<MissionInfo>): void--><!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int, callback: AsyncCallback<MissionInfo>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| missionId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;MissionInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let testMissionId = 1;

// 获取所有任务信息
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
    console.error(`getMissionInfos failed, Code: ${error.code}, message: ${error.message}.`);
  });
```


## getMissionInfo

```TypeScript
function getMissionInfo(deviceId: string, missionId: number): Promise<MissionInfo>
```

获取任务信息。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int): Promise<MissionInfo>--><!--Device-missionManager-function getMissionInfo(deviceId: string, missionId: int): Promise<MissionInfo>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| missionId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;MissionInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
      console.error(`getMissionInfo failed. Code: ${error.code}, message: ${error.message}`);
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getMissionInfo failed. Code: ${err.code}, message: ${err.message}`);
}
```
