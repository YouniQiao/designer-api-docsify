# onChangeSceneAnimationState (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
import { formHost } from '@kit.FormKit';
```

## onChangeSceneAnimationState

```TypeScript
function onChangeSceneAnimationState(callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void
```

Listens to the event of change scene animation state. You can use this method to listen to the event of change scene animation state.

**Since:** 23

<!--Device-formHost-function onChangeSceneAnimationState(callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void--><!--Device-formHost-function onChangeSceneAnimationState(callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.ChangeSceneAnimationStateRequest&gt; | Yes | The callback of change scene animation state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

