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

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function offCooperateMessage(callback?: Callback<CooperateMessage>): void--><!--Device-cooperate-function offCooperateMessage(callback?: Callback<CooperateMessage>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[CooperateMessage](arkts-distributedservice-cooperate-cooperatemessage-i-sys.md)&gt; | No | Callback for which listening <br> is disabled. If this parameter is not specified, listening will be disabled for all registered callbacks. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. <br> verification failed. |

