# stopSyncRemoteMissions（系统接口）

## stopSyncRemoteMissions

```TypeScript
function stopSyncRemoteMissions(parameter: MissionDeviceInfo, callback: AsyncCallback<void>): void
```

停止同步远端设备的任务列表。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-distributedMissionManager-function stopSyncRemoteMissions(parameter: MissionDeviceInfo, callback: AsyncCallback<void>): void--><!--Device-distributedMissionManager-function stopSyncRemoteMissions(parameter: MissionDeviceInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 停止同步远端设备的任务列表
  distributedMissionManager.stopSyncRemoteMissions(
    {
      deviceId: ""
    },
    (error: BusinessError) => {
      if (error) {
        console.error(`stopSyncRemoteMissions failed. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      console.info('stopSyncRemoteMissions finished');}
  )
} catch (error) {
  console.error(`stopSyncRemoteMissions failed. Code: ${error.code}, message: ${error.message}`);
}
```


## stopSyncRemoteMissions

```TypeScript
function stopSyncRemoteMissions(parameter: MissionDeviceInfo): Promise<void>
```

停止同步远端设备的任务列表。使用promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-distributedMissionManager-function stopSyncRemoteMissions(parameter: MissionDeviceInfo): Promise<void>--><!--Device-distributedMissionManager-function stopSyncRemoteMissions(parameter: MissionDeviceInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  distributedMissionManager.stopSyncRemoteMissions(
    {
      deviceId: ""
    }).then(() => {
      console.info('stopSyncRemoteMissions finished successfully');
    }).catch((error: BusinessError) => {
    console.error(`stopSyncRemoteMissions failed. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`stopSyncRemoteMissions failed. Code: ${error.code}, message: ${error.message}`);
}
```
