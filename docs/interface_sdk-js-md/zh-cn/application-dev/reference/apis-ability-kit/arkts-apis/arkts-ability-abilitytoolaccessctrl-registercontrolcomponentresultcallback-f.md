# registerControlComponentResultCallback

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## registerControlComponentResultCallback

```TypeScript
export function registerControlComponentResultCallback(callback: ResultCallback): void
```

注册控制组件模拟点击结果回调。注册后，控制组件每次模拟点击的结果通过该回调返回。同一进程内仅支持注册一个回调，重复注册将覆盖先前注册的回调。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-abilityToolAccessCtrl-export function registerControlComponentResultCallback(callback: ResultCallback): void--><!--Device-abilityToolAccessCtrl-export function registerControlComponentResultCallback(callback: ResultCallback): void-End-->

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ResultCallback](arkts-ability-abilitytoolaccessctrl-resultcallback-t.md) | 是 | 用于接收模拟点击操作结果的回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [24010000](../errorcode-abilityToolAccessCtrl-sys.md#24010000-入参错误) | Invalid parameter. callback is invalid. |
| [24010001](../errorcode-abilityToolAccessCtrl-sys.md#24010001-系统服务工作异常) | Service is abnormal. Possible cause: IPC failed. |
| [24010002](../errorcode-abilityToolAccessCtrl-sys.md#24010002-服务内部错误) | Common internal error. Possible cause: dependent service unavailable, resource access failure, etc. |
