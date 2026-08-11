# off (System API)

## Modules to Import

```TypeScript
import { distributedMissionManager } from 'kits/@kit.AbilityKit';
```

## off('continueStateChange')

```TypeScript
function off(type: 'continueStateChange', callback?: Callback<ContinueCallbackInfo>): void
```

Unsubscribes from continuation state change events of the current mission.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-distributedMissionManager-function off(type: 'continueStateChange', callback?: Callback<ContinueCallbackInfo>): void--><!--Device-distributedMissionManager-function off(type: 'continueStateChange', callback?: Callback<ContinueCallbackInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'continueStateChange' | Yes | Event type. The value **'continueStateChange'** indicates the continuation state change event of the current mission. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ContinueCallbackInfo&gt; | No | Callback used for unsubscription.&lt;br&gt;If the callback is unspecified , all subscriptions to the specified event are canceled.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { distributedMissionManager } from '@kit.AbilityKit';

  try {
    distributedMissionManager.off('continueStateChange', (data) => {
      console.info("continueStateChange off:" + JSON.stringify(data));
    });
  } catch (err) {
    console.error("continueStateChange err: " + JSON.stringify(err));
  }
```

