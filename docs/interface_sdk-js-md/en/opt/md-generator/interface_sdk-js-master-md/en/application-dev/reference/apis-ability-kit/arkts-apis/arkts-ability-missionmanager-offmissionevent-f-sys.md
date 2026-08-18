# off_missionEvent (System API)

## Modules to Import

```TypeScript
```

## off_missionEvent

```TypeScript
function off(type: 'missionEvent', listenerId: number, callback: AsyncCallback<void>): void
```

Deregisters a mission status listener. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [off](arkts-ability-missionmanager-offmission-f-sys.md#offmission)(type: 'mission', listenerId: long, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function off(type: 'missionEvent', listenerId: long, callback: AsyncCallback<void>): void--><!--Device-missionManager-function off(type: 'missionEvent', listenerId: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'missionEvent' | Yes |
| listenerId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) |


## off_missionEvent

```TypeScript
function off(type: 'missionEvent', listenerId: number): Promise<void>
```

Unregisters a mission status listener. This API uses a promise to return the result.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [off](arkts-ability-missionmanager-offmission-f-sys.md#offmission)(type: 'mission', listenerId: long)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function off(type: 'missionEvent', listenerId: long): Promise<void>--><!--Device-missionManager-function off(type: 'missionEvent', listenerId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'missionEvent' | Yes |
| listenerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) |
