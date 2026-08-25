# startContinuationDeviceManager

## 导入模块

```TypeScript
import { continuationManager } from 'kits/@kit.AbilityKit';
```

## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void
```

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。

**起始版本：** 9

**废弃版本：** 22

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-指定的token或callback未注册) |


## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(
    token: number,
    options: ContinuationExtraParams,
    callback: AsyncCallback<void>
  ): void
```

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。

**起始版本：** 9

**废弃版本：** 22

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | number | 是 |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-指定的token或callback未注册) |


## startContinuationDeviceManager

```TypeScript
function startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>
```

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。

**起始版本：** 9

**废弃版本：** 22

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| token | number | 是 |
| options | [ContinuationExtraParams](arkts-ability-continuationextraparams-continuationextraparams-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-指定的token或callback未注册) |
