# offAclStateChange

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## offAclStateChange

```TypeScript
function offAclStateChange(callback?: Callback<AclStateResult>): void
```

Unsubscribe the event of acl state changed from a remote device. If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function offAclStateChange(callback?: Callback<AclStateResult>): void--><!--Device-connection-function offAclStateChange(callback?: Callback<AclStateResult>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AclStateResult](arkts-connectivity-connection-aclstateresult-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900099 |

## Examples

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
