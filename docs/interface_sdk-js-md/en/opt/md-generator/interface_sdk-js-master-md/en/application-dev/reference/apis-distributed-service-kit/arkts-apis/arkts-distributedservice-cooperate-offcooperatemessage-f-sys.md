# offCooperateMessage (System API)

## Modules to Import

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
```

## offCooperateMessage

```TypeScript
function offCooperateMessage(callback?: Callback<CooperateMessage>): void
```

Disables listening for screen hopping status change events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function offCooperateMessage(callback?: Callback<CooperateMessage>): void--><!--Device-cooperate-function offCooperateMessage(callback?: Callback<CooperateMessage>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CooperateMessage](arkts-distributedservice-cooperate-cooperatemessage-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
