# onAclStateChange

## onAclStateChange

```TypeScript
function onAclStateChange(callback: Callback<AclStateResult>): void
```

Subscribe the event of acl state changed from a remote device.If the application has ohos.permission.GET\_BLUETOOTH\_PEERS\_MAC, the type of the peer device address is real.Otherwise, the type of the peer device address is virtual.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function onAclStateChange(callback: Callback<AclStateResult>): void--><!--Device-connection-function onAclStateChange(callback: Callback<AclStateResult>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;AclStateResult&gt; | Yes | Callback used to listen. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API when the short-range chip is not inserted on 2in1 device. |
| 2900099 | Internal system error. For example, IPC error. Detailed error messages can be used to assist in locating the problem. |

