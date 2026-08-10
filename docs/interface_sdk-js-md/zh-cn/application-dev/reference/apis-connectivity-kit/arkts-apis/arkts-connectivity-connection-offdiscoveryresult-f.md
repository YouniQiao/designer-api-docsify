# offDiscoveryResult

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## offDiscoveryResult

```TypeScript
function offDiscoveryResult(callback?: Callback<Array<DiscoveryResult>>): void
```

Unsubscribe the event reported when a remote Bluetooth device is discovered.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function offDiscoveryResult(callback?: Callback<Array<DiscoveryResult>>): void--><!--Device-connection-function offDiscoveryResult(callback?: Callback<Array<DiscoveryResult>>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;DiscoveryResult&gt;&gt; | 否 | Callback used to listen for the discovering event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

