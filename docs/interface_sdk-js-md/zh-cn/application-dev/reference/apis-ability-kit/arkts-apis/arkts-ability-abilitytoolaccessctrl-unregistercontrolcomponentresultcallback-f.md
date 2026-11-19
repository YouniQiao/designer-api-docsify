# unregisterControlComponentResultCallback

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## unregisterControlComponentResultCallback

```TypeScript
export function unregisterControlComponentResultCallback(): void
```

注销控制组件模拟点击结果回调。用于在业务结束时释放回调资源。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-abilityToolAccessCtrl-export function unregisterControlComponentResultCallback(): void--><!--Device-abilityToolAccessCtrl-export function unregisterControlComponentResultCallback(): void-End-->

**系统能力：** SystemCapability.Security.Asset

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [24010001](../errorcode-abilityToolAccessCtrl-sys.md#24010001-系统服务工作异常) | Service is abnormal. Possible cause: IPC failed. |
| [24010002](../errorcode-abilityToolAccessCtrl-sys.md#24010002-服务内部错误) | Common internal error. Possible cause: dependent service unavailable, resource access failure, etc. |
