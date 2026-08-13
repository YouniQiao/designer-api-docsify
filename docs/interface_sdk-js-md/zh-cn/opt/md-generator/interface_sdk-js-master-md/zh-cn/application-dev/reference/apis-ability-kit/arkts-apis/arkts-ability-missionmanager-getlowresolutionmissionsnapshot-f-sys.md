# getLowResolutionMissionSnapShot（系统接口）

## getLowResolutionMissionSnapShot

```TypeScript
function getLowResolutionMissionSnapShot(
    deviceId: string,
    missionId: number,
    callback: AsyncCallback<MissionSnapshot>
  ): void
```

获取任务低分辨率快照。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getLowResolutionMissionSnapShot(    deviceId: string,    missionId: int,    callback: AsyncCallback<MissionSnapshot>  ): void--><!--Device-missionManager-function getLowResolutionMissionSnapShot(    deviceId: string,    missionId: int,    callback: AsyncCallback<MissionSnapshot>  ): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| missionId | number | 是 |
| callback | AsyncCallback & lt;MissionSnapshot & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// testMissionId为任务ID，可通过getMissionInfos接口获取真实有效的任务ID
let testMissionId = 2;

try {
  missionManager.getLowResolutionMissionSnapShot('', testMissionId,
    (err: BusinessError, data: missionManager.MissionSnapshot) => {
      if (err) {
        console.error(`getLowResolutionMissionSnapShot failed. Code: ${err.code}, message: ${err.message}.`);
      } else {
        console.info(`getLowResolutionMissionSnapShot successfully: ${JSON.stringify(data)}`);
      }
    });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getLowResolutionMissionSnapShot failed. Code: ${err.code}, message: ${err.message}.`);
}
```


## getLowResolutionMissionSnapShot

```TypeScript
function getLowResolutionMissionSnapShot(deviceId: string, missionId: number): Promise<MissionSnapshot>
```

获取任务低分辨率快照。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function getLowResolutionMissionSnapShot(deviceId: string, missionId: int): Promise<MissionSnapshot>--><!--Device-missionManager-function getLowResolutionMissionSnapShot(deviceId: string, missionId: int): Promise<MissionSnapshot>-End-->

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
| Promise & lt;MissionSnapshot & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// testMissionId为任务ID，可通过getMissionInfos接口获取真实有效的任务ID
let testMissionId = 2;

try {
  missionManager.getLowResolutionMissionSnapShot('', testMissionId).then((data: missionManager.MissionSnapshot) => {
    console.info(`getLowResolutionMissionSnapShot successfully. Data: ${JSON.stringify(data)}`);
  }).catch((error: BusinessError) => {
    console.error(`getLowResolutionMissionSnapShot failed. Code: ${error.code}, message: ${error.message}.`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getLowResolutionMissionSnapShot failed. Code: ${err.code}, message: ${err.message}.`);
}
```
