# onAclStateChange

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## onAclStateChange

```TypeScript
function onAclStateChange(callback: Callback<AclStateResult>): void
```

Subscribe the event of acl state changed from a remote device.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function onAclStateChange(callback: Callback<AclStateResult>): void--><!--Device-connection-function onAclStateChange(callback: Callback<AclStateResult>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AclStateResult](arkts-connectivity-connection-aclstateresult-i.md)&gt; | Yes | Callback used to listen. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900099 | Internal system error. For example, IPC error. Detailed error messages can be used to assist in locating the problem. |

**Examples**

```TypeScript
function AclStateChangeEvent(aclStateResult: connection.AclStateResult) {
    console.info('acl state changed:'+ JSON.stringify(aclStateResult));
}
try {
    connection.onAclStateChange(AclStateChangeEvent);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```
