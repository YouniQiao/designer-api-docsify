# getConnectOwnerUidSync

## Modules to Import

```TypeScript
```

## getConnectOwnerUidSync

```TypeScript
function getConnectOwnerUidSync(protocol: ProtocolType, local: NetAddress, remote: NetAddress): number
```

Obtains the data network that is activated by default. You can only call this method in VPN application.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getConnectOwnerUidSync(protocol: ProtocolType, local: NetAddress, remote: NetAddress): int--><!--Device-connection-function getConnectOwnerUidSync(protocol: ProtocolType, local: NetAddress, remote: NetAddress): int-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| protocol | [ProtocolType](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-hid-protocoltype-e.md) | Yes |
| local | [NetAddress](arkts-network-connection-netaddress-i.md) | Yes |
| [remote](../../apis-driver-development-kit/arkts-apis/arkts-driverdevelopment-devicemanager-remotedevicedriver-i.md) | [NetAddress](arkts-network-connection-netaddress-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2100301](../errorcode-net-connection.md#2100301-failed-to-authenticate-the-caller-nonvpn-application) |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let protocol = connection.ProtocolType.PROTO_TYPE_TCP;
let local: connection.NetAddress = { address: '192.168.1.100', family: 1, port: 6666 };
let remote: connection.NetAddress = { address: '192.168.1.200', family: 1, port: 8888 };
try {
  let uid = connection.getConnectOwnerUidSync(protocol, local, remote);
  console.info(`uid: ${uid}`);
} catch (e) {
  let err = e as BusinessError;
  console.error(`getConnectOwnerUid failed. errorCode: ${err.code} message:${err.message}`);
}
```
