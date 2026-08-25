# continueMission（系统接口）

## 导入模块

```TypeScript
import { distributedMissionManager } from 'kits/@kit.AbilityKit';
```

## continueMission

```TypeScript
function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback, callback: AsyncCallback<void>): void
```

通过指定任务ID（missionId）的方式进行迁移任务。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [ContinueDeviceInfo](arkts-ability-continuedeviceinfo-i-sys.md) | 是 |
| options | [ContinueCallback](arkts-ability-continuecallback-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16300501](../errorcode-DistributedSchedule.md#16300501-系统服务工作异常) |
| [16300502](../errorcode-DistributedSchedule.md#16300502-获取指定的missionid的missioninfo失败) |
| [16300503](../errorcode-DistributedSchedule.md#16300503-远端未安装应用且不支持免安装) |
| [16300504](../errorcode-DistributedSchedule.md#16300504-远端未安装应用但支持免安装需使用免安装标识重试) |
| [16300505](../errorcode-DistributedSchedule.md#16300505-操作设备必须是迁移的应用所在的设备或需迁移到的目标设备) |
| [16300506](../errorcode-DistributedSchedule.md#16300506-本地迁移任务已在进行中) |


## continueMission

```TypeScript
function continueMission(parameter: ContinueDeviceInfo, options: ContinueCallback): Promise<void>
```

通过指定任务ID（missionId）的方式进行迁移任务。使用promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [ContinueDeviceInfo](arkts-ability-continuedeviceinfo-i-sys.md) | 是 |
| options | [ContinueCallback](arkts-ability-continuecallback-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16300501](../errorcode-DistributedSchedule.md#16300501-系统服务工作异常) |
| [16300502](../errorcode-DistributedSchedule.md#16300502-获取指定的missionid的missioninfo失败) |
| [16300503](../errorcode-DistributedSchedule.md#16300503-远端未安装应用且不支持免安装) |
| [16300504](../errorcode-DistributedSchedule.md#16300504-远端未安装应用但支持免安装需使用免安装标识重试) |
| [16300505](../errorcode-DistributedSchedule.md#16300505-操作设备必须是迁移的应用所在的设备或需迁移到的目标设备) |
| [16300506](../errorcode-DistributedSchedule.md#16300506-本地迁移任务已在进行中) |


## continueMission

```TypeScript
function continueMission(parameter: ContinueMissionInfo, callback: AsyncCallback<void>): void
```

通过指定包名（bundleName）的方式进行迁移任务。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [ContinueMissionInfo](arkts-ability-continuemissioninfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16300501](../errorcode-DistributedSchedule.md#16300501-系统服务工作异常) |
| [16300503](../errorcode-DistributedSchedule.md#16300503-远端未安装应用且不支持免安装) |
| [16300504](../errorcode-DistributedSchedule.md#16300504-远端未安装应用但支持免安装需使用免安装标识重试) |
| [16300505](../errorcode-DistributedSchedule.md#16300505-操作设备必须是迁移的应用所在的设备或需迁移到的目标设备) |
| [16300506](../errorcode-DistributedSchedule.md#16300506-本地迁移任务已在进行中) |
| [16300507](../errorcode-DistributedSchedule.md#16300507-获取指定的bundlename的missioninfo失败) |


## continueMission

```TypeScript
function continueMission(parameter: ContinueMissionInfo): Promise<void>
```

通过指定包名（bundleName）的方式进行迁移任务。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.MANAGE_MISSIONS and ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Mission

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| parameter | [ContinueMissionInfo](arkts-ability-continuemissioninfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16300501](../errorcode-DistributedSchedule.md#16300501-系统服务工作异常) |
| [16300503](../errorcode-DistributedSchedule.md#16300503-远端未安装应用且不支持免安装) |
| [16300504](../errorcode-DistributedSchedule.md#16300504-远端未安装应用但支持免安装需使用免安装标识重试) |
| [16300505](../errorcode-DistributedSchedule.md#16300505-操作设备必须是迁移的应用所在的设备或需迁移到的目标设备) |
| [16300506](../errorcode-DistributedSchedule.md#16300506-本地迁移任务已在进行中) |
| [16300507](../errorcode-DistributedSchedule.md#16300507-获取指定的bundlename的missioninfo失败) |
