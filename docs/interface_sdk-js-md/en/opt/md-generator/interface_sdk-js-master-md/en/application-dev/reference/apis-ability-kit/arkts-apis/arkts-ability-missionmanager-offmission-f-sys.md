# offMission (System API)

## Modules to Import

```TypeScript
```

## offMission

```TypeScript
function offMission(listenerId: number, callback: AsyncCallback<void>): void
```

Unregister the missionListener to ams.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function offMission(listenerId: long, callback: AsyncCallback<void>): void--><!--Device-missionManager-function offMission(listenerId: long, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| listenerId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) |


## offMission

```TypeScript
function offMission(listenerId: number): Promise<void>
```

Unregister the missionListener to ams.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function offMission(listenerId: long): Promise<void>--><!--Device-missionManager-function offMission(listenerId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| listenerId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16300002](../errorcode-ability.md#16300002-nonexistent-mission-listener) |
