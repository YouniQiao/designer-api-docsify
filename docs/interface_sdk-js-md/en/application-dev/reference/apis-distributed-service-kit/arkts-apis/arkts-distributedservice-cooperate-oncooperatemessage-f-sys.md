# onCooperateMessage (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## onCooperateMessage

```TypeScript
function onCooperateMessage(callback: Callback<CooperateMessage>): void
```

Enables listening for screen hopping status change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function onCooperateMessage(callback: Callback<CooperateMessage>): void--><!--Device-cooperate-function onCooperateMessage(callback: Callback<CooperateMessage>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CooperateMessage&gt; | Yes | Asynchronous callback used to &lt;br&gt; return the screen hopping status change event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

