# offPrepareContinue

## offPrepareContinue

```TypeScript
function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void
```

Unregister prepareContinue event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void--><!--Device-continueManager-function offPrepareContinue(context: Context, callback?: AsyncCallback<ContinueResultInfo>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the ability context. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ContinueResultInfo&gt; | No | Used to handle ('prepareContinue') command. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16300501](../errorcode-DistributedSchedule.md#16300501-the-system-ability-works-abnormally) | the system ability work abnormally. |

