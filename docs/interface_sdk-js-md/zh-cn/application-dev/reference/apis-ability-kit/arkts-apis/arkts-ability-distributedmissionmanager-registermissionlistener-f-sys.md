# registerMissionListener（系统接口）

## 导入模块

```TypeScript
import { distributedMissionManager } from 'kits/@kit.AbilityKit';
```

## registerMissionListener

```TypeScript
function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback, callback: AsyncCallback<void>): void
```

注册任务状态监听。使用callback异步回调。调用成功后，系统将开始监听指定设备上的任务状态变化，该监听需与unRegisterMissionListener成对使用，注册后应在不需要监听任务状态时及时取消。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [MissionDeviceInfo](arkts-ability-missiondeviceinfo-i-sys.md) | 是 |
| options | [MissionCallback](arkts-ability-missioncallbacks-missioncallback-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## registerMissionListener

```TypeScript
function registerMissionListener(parameter: MissionDeviceInfo, options: MissionCallback): Promise<void>
```

注册任务状态监听。使用promise异步回调。调用成功后，系统将开始监听指定设备上的任务状态变化，该监听需与unRegisterMissionListener成对使用，注册后应在不需要监听任务状态时及时取消。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
