# acquireShareData (System API)

## Modules to Import

```TypeScript
import { abilityManager } from '@kit.AbilityKit';
```

## acquireShareData

```TypeScript
function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, Object>>): void
```

Called by a system dialog box to obtain shared data, which is set by the target UIAbility through [onShare](arkts-ability-app-ability-uiability-uiability-c.md#onshare). This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, Object>>): void--><!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, Object>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionId | int | Yes | Mission ID on the target application. The maximum value is 2&lt;sup&gt;31&lt;/sup&gt;-1. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Record&lt;string, Object&gt;&gt; | Yes | Callback used to return the result. If the API call is successful, **err** is **undefined** and **data** is the shared data obtained. Otherwise, **err** is an error object. You can perform error handling or other custom processing.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |


## acquireShareData

```TypeScript
function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, RecordData>>): void
```

Acquire the shared data from target ability.

**Since:** 23

<!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, RecordData>>): void--><!--Device-abilityManager-function acquireShareData(missionId: int, callback: AsyncCallback<Record<string, RecordData>>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionId | int | Yes | The missionId of target ability. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;&gt; | Yes | The callback is used to return the params of sharing data and result code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Connect to system service failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |


## acquireShareData

```TypeScript
function acquireShareData(missionId: int): Promise<Record<string, Object>>
```

Called by a system dialog box to obtain shared data, which is set by the target UIAbility through [onShare](arkts-ability-app-ability-uiability-uiability-c.md#onshare). This API uses a promise to return the result.

**Since:** 10

<!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, Object>>--><!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, Object>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionId | int | Yes | Mission ID on the target application. The maximum value is 2&lt;sup&gt;31&lt;/sup&gt;-1. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;{ [key: string]: Object | > } The promise returned by the function.<br>**Applicable version:** 10 and later |
| Promise&lt;Record&lt;string, Object&gt;&gt; | Promise used to return the API call result and the shared data. You can perform error handling or other custom processing.<br>**Applicable version:** 11 and later |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |


## acquireShareData

```TypeScript
function acquireShareData(missionId: int): Promise<Record<string, RecordData>>
```

Acquire the shared data from target ability.

**Since:** 23

<!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, RecordData>>--><!--Device-abilityManager-function acquireShareData(missionId: int): Promise<Record<string, RecordData>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| missionId | int | Yes | The missionId of target ability. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Record&lt;string, [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Connect to system server failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. Interface caller is not a system app. |

