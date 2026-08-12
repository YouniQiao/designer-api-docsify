# off

## off('deviceSelected')

```TypeScript
function off(type: 'deviceSelected', token: number): void
```

取消监听设备连接状态。

**起始版本：** 9

**废弃版本：** 22

**替代接口：** [off](@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-continuationManager-function off(type: 'deviceSelected', token: number): void--><!--Device-continuationManager-function off(type: 'deviceSelected', token: number): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceSelected' | 是 |
| token | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [16600004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600004-指定的callback已注册) |
| [16600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600002-指定的token或callback未注册) |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.off("deviceSelected", token);
} catch (err) {
  console.error('off failed, cause: ' + JSON.stringify(err));
}
```


## off('deviceUnselected')

```TypeScript
function off(type: 'deviceUnselected', token: number): void
```

取消监听设备断开状态。

**起始版本：** 9

**废弃版本：** 22

**替代接口：** [off](@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:)

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-continuationManager-function off(type: 'deviceUnselected', token: number): void--><!--Device-continuationManager-function off(type: 'deviceUnselected', token: number): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceUnselected' | 是 |
| token | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [16600004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600004-指定的callback已注册) |
| [16600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-ability-kit/errorcode-DistributedSchedule.md#16600002-指定的token或callback未注册) |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.off("deviceUnselected", token);
} catch (err) {
  console.error('off failed, cause: ' + JSON.stringify(err));
}
```


## off('deviceConnect')

```TypeScript
function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void
```

异步方法，取消监听设备连接状态，使用Callback形式返回连接的设备信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continuationManager-function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void--><!--Device-continuationManager-function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceConnect' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ContinuationResult&gt; | 否 |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceConnect", (data) => {
  console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
  console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
  console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
});
```


## off('deviceDisconnect')

```TypeScript
function off(type: 'deviceDisconnect', callback?: Callback<string>): void
```

异步方法，取消监听设备断开状态，使用Callback形式返回连接的设备信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [off](@ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type:)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-continuationManager-function off(type: 'deviceDisconnect', callback?: Callback<string>): void--><!--Device-continuationManager-function off(type: 'deviceDisconnect', callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceDisconnect' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

## 示例

```TypeScript
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```
