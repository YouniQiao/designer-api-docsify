# offChangeSceneAnimationState (System API)

## offChangeSceneAnimationState

```TypeScript
function offChangeSceneAnimationState(callback?: Callback<formInfo.ChangeSceneAnimationStateRequest>): void
```

Cancels listening to the event of change scene animation state. You can use this method to cancel listening to the event of change scene animation state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-formHost-function offChangeSceneAnimationState(callback?: Callback<formInfo.ChangeSceneAnimationStateRequest>): void--><!--Device-formHost-function offChangeSceneAnimationState(callback?: Callback<formInfo.ChangeSceneAnimationStateRequest>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;formInfo.ChangeSceneAnimationStateRequest&gt; | No | The callback of change scene animation state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

