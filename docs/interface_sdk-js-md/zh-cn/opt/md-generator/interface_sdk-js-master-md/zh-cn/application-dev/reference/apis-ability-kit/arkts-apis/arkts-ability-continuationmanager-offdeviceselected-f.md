# off_deviceSelected

## off_deviceSelected

```TypeScript
function off(type: 'deviceSelected', token: number): void
```

取消监听设备连接状态。

**起始版本：** 9

**废弃版本：** 22

**替代接口：** [off](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#off_deviceStateChange)(type: 'deviceStateChange', callback?: Callback&lt;{ action: DeviceStateChange; device: DeviceBasicInfo; }&gt;)

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16600004](../errorcode-DistributedSchedule.md#16600004-指定的callback已注册) |
| [16600001](../errorcode-DistributedSchedule.md#16600001-系统服务工作异常) |
| [16600002](../errorcode-DistributedSchedule.md#16600002-指定的token或callback未注册) |

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
