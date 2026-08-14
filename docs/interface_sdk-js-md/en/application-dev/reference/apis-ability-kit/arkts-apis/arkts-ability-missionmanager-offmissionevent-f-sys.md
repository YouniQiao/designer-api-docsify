# off_missionEvent (System API)

## Modules to Import

```TypeScript
import { missionManager } from 'missionManager';
```

## off_missionEvent

```TypeScript
function off(type: 'missionEvent', listenerId: long, callback: AsyncCallback<void>): void
```

Deregisters a mission status listener. This API uses an asynchronous callback to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** off(type: 'mission', listenerId: long, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function off(type: 'missionEvent', listenerId: long, callback: AsyncCallback<void>): void--><!--Device-missionManager-function off(type: 'missionEvent', listenerId: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'missionEvent' | Yes | Name of the target mission. The value is fixed at **'mission'**, indicating the system mission status listener. |
| listenerId | long | Yes | Index of the mission status listener to deregister. It is returned by **on()**. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) | The specified mission listener does not exist. |


## off_missionEvent

```TypeScript
function off(type: 'missionEvent', listenerId: long): Promise<void>
```

Unregisters a mission status listener. This API uses a promise to return the result.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 10

**Substitutes:** off(type: 'mission', listenerId: long)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function off(type: 'missionEvent', listenerId: long): Promise<void>--><!--Device-missionManager-function off(type: 'missionEvent', listenerId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'missionEvent' | Yes | Name of the target mission. The value is fixed at **'missionEvent'**, indicating the system mission status listener. |
| listenerId | long | Yes | Index of the mission status listener to deregister. It is returned by **on()**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) | The specified mission listener does not exist. |

