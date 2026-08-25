# getMissionInfos（系统接口）

## 导入模块

```TypeScript
import { missionManager } from '@kit.AbilityKit';
```

## getMissionInfos

```TypeScript
function getMissionInfos(deviceId: string, numMax: int, callback: AsyncCallback<Array<MissionInfo>>): void
```

获取所有任务信息。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| numMax | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | AsyncCallback & lt;Array & lt;MissionInfo & gt; & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 获取所有任务信息
  missionManager.getMissionInfos('', 10,
    (error: BusinessError | null, missions: Array<missionManager.MissionInfo> | undefined) => {
      if (error) {
        console.error(`getMissionInfos failed, error.code: ${error.code}, error.message: ${error.message}`);
      } else {
        console.info(`size = ${missions?.length}`);
        console.info(`missions = ${JSON.stringify(missions)}`);
      }
    });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`error: ${code}, ${message} `);
}
```

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 获取所有任务信息
  missionManager.getMissionInfos('', 10).then((data: Array<missionManager.MissionInfo>) => {
    console.info(`getMissionInfos successfully. Data: ${JSON.stringify(data)}`);
  }).catch((err: Error) => {
    let error: BusinessError = err as BusinessError;
    console.error(`getMissionInfos failed. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getMissionInfos failed. Code: ${err.code}, message: ${err.message}`);
}
```


## getMissionInfos

```TypeScript
function getMissionInfos(deviceId: string, numMax: int): Promise<Array<MissionInfo>>
```

获取所有任务信息。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.MANAGE_MISSIONS

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | string | 是 |
| numMax | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;MissionInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

参见 [getMissionInfos](#getmissioninfos)
