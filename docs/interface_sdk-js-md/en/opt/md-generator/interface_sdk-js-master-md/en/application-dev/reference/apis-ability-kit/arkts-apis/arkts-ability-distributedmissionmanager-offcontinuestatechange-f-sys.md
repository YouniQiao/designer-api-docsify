# offContinueStateChange (System API)

## Modules to Import

```TypeScript
```

## offContinueStateChange

```TypeScript
function offContinueStateChange(callback?: Callback<ContinueCallbackInfo>): void
```

Unregister continuable info listener to ams.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function offContinueStateChange(callback?: Callback<ContinueCallbackInfo>): void--><!--Device-distributedMissionManager-function offContinueStateChange(callback?: Callback<ContinueCallbackInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinueCallbackInfo](arkts-ability-distributedmissionmanager-continuecallbackinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
