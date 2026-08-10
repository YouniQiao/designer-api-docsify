# getConnectOwnerUidSync

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getConnectOwnerUidSync

```TypeScript
function getConnectOwnerUidSync(protocol: ProtocolType, local: NetAddress, remote: NetAddress): int
```

Obtains the data network that is activated by default.You can only call this method in VPN application.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function getConnectOwnerUidSync(protocol: ProtocolType, local: NetAddress, remote: NetAddress): int--><!--Device-connection-function getConnectOwnerUidSync(protocol: ProtocolType, local: NetAddress, remote: NetAddress): int-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| protocol | [ProtocolType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-hid-protocoltype-e.md) | 是 | Protocol type. |
| local | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 | Local net address. |
| remote | [NetAddress](arkts-network-connection-netaddress-i.md) | 是 | Remote net address. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | The owner uid of the specified connection. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 2100301 | Incorrect usage in non-VPN application. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let protocol = connection.ProtocolType.PROTO_TYPE_TCP;
let local: connection.NetAddress = { address: '192.168.1.100', family: 1, port: 6666 };
let remote: connection.NetAddress = { address: '192.168.1.200', family: 1, port: 8888 };
try {
  let uid = connection.getConnectOwnerUidSync(protocol, local, remote);
  console.info(`Succeeded to get uid: ${uid}`);
} catch (e) {
  let err = e as BusinessError;
  console.error(`Failed to get ConnectOwnerUid. errorCode: ${err.code} message:${err.message}`);
}
```

