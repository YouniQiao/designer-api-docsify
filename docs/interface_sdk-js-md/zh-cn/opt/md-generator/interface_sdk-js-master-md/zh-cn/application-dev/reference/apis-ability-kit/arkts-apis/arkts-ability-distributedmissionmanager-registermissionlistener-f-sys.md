# registerMissionListener（系统接口）

## registerMissionListener

```TypeScript
function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback, callback: AsyncCallback<void>): void
```

注册任务状态监听。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-distributedMissionManager-function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback, callback: AsyncCallback<void>): void--><!--Device-distributedMissionManager-function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | 是 |
| options | [MissionCallback](arkts-ability-missioncallbacks-missioncallback-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 实现回调函数
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
  // 调用registerMissionListener接口
  distributedMissionManager.registerMissionListener(
    { deviceId: "" },
    {
      notifyMissionsChanged: NotifyMissionsChanged,
      notifySnapshot: NotifySnapshot,
      notifyNetDisconnect: NotifyNetDisconnect
    },
    (error: BusinessError) => {
      if (error) {
        console.error(`Failed to register mission listener. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      console.info('registerMissionListener finished');
    });
   } catch (error) {
  console.error(`Failed to register mission listener. Code: ${error.code}, message: ${error.message}`);
}
```


## registerMissionListener

```TypeScript
function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback): Promise<void>
```

注册任务状态监听。使用promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-distributedMissionManager-function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback): Promise<void>--><!--Device-distributedMissionManager-function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | 是 |
| options | [MissionCallback](arkts-ability-missioncallbacks-missioncallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 实现回调函数
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
    // 调用registerMissionListener接口
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
