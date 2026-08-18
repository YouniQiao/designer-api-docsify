# offMission (System API)

## Modules to Import

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { missionManager } from '@kit.AbilityKit';
```

## offMission

```TypeScript
function offMission(listenerId: long, callback: AsyncCallback<void>): void
```

Unregister the missionListener to ams.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function offMission(listenerId: long, callback: AsyncCallback<void>): void--><!--Device-missionManager-function offMission(listenerId: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listenerId | long | Yes | Indicates the listener id to be unregistered. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | The callback of off. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) | The specified mission listener does not exist. |


## offMission

```TypeScript
function offMission(listenerId: long): Promise<void>
```

Unregister the missionListener to ams.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function offMission(listenerId: long): Promise<void>--><!--Device-missionManager-function offMission(listenerId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listenerId | long | Yes | Indicates the listener id to be unregistered. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) | The specified mission listener does not exist. |

