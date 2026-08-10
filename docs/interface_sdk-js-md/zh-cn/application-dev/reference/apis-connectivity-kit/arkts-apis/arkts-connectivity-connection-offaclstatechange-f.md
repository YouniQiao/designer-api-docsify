# offAclStateChange

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.ConnectivityKit';
```

## offAclStateChange

```TypeScript
function offAclStateChange(callback?: Callback<AclStateResult>): void
```

Unsubscribe the event of acl state changed from a remote device.If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real.Otherwise, the type of the peer device address is virtual.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function offAclStateChange(callback?: Callback<AclStateResult>): void--><!--Device-connection-function offAclStateChange(callback?: Callback<AclStateResult>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AclStateResult&gt; | 否 | Callback used to listen. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call the API when the short-range chip is not inserted on 2in1 device. |
| 201 | Permission denied. |
| 2900099 | Internal system error. For example, IPC error. Detailed error messages can be used to assist in locating the problem. |

## 示例

```TypeScript
function AclStateChangeEvent(aclStateResult: connection.AclStateResult) {
    console.info('acl state changed:'+ JSON.stringify(aclStateResult));
}
try {
    connection.offAclStateChange(AclStateChangeEvent);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

