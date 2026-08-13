# offReceiveData

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## offReceiveData

```TypeScript
function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void
```

Unsubscribes from data receiving events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void--><!--Device-proxyChannelManager-function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channelId | int | Yes | Channel ID obtained when the proxy channel is opened. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md)&gt; | No | Registered callback, If the value is empty, **undefined**, or **null**, all callbacks of data receiving events are unregistered. If the value is not empty, the last registered callback is used. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-parameter-verification-error) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) | ChannelId is invalid or unavailable. |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-internal-error) | Internal error. |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-call-restricted) | Call is restricted. |

