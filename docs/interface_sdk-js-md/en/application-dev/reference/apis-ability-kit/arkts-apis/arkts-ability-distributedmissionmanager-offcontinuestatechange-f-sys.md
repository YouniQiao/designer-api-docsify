# offContinueStateChange (System API)

## Modules to Import

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';
```

## offContinueStateChange

```TypeScript
function offContinueStateChange(callback?: Callback<ContinueCallbackInfo>): void
```

Unregister continuable info listener to ams.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function offContinueStateChange(callback?: Callback<ContinueCallbackInfo>): void--><!--Device-distributedMissionManager-function offContinueStateChange(callback?: Callback<ContinueCallbackInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ContinueCallbackInfo](arkts-ability-distributedmissionmanager-continuecallbackinfo-i-sys.md)&gt; | No | The callback of continueStateChange. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

