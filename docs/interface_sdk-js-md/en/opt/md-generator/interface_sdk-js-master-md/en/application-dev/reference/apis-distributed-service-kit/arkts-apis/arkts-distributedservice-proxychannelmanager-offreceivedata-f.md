# offReceiveData

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## offReceiveData

```TypeScript
function offReceiveData(channelId: number, callback?: Callback<DataInfo>): void
```

Unsubscribes from data receiving events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void--><!--Device-proxyChannelManager-function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| channelId | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-call-restricted) |
