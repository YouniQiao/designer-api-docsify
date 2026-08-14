# offChangeSceneAnimationState (System API)

## Modules to Import

```TypeScript
import { formHost } from 'formHost';
```

## offChangeSceneAnimationState

```TypeScript
function offChangeSceneAnimationState(callback?: Callback<formInfo.ChangeSceneAnimationStateRequest>): void
```

Cancels listening to the event of change scene animation state. You can use this method to cancel listening to the event of change scene animation state.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-formHost-function offChangeSceneAnimationState(callback?: Callback<formInfo.ChangeSceneAnimationStateRequest>): void--><!--Device-formHost-function offChangeSceneAnimationState(callback?: Callback<formInfo.ChangeSceneAnimationStateRequest>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.ChangeSceneAnimationStateRequest&gt; | No | The callback of change scene animation state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

