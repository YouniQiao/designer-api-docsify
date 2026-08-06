# offDidLayout

## offDidLayout

```TypeScript
export function offDidLayout(context: UIContext, callback?: Callback<void>): void
```

Removes a callback function that was previously registered with \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offDidLayout(context: UIContext, callback?: Callback<void>): void--><!--Device-uiObserver-export function offDidLayout(context: UIContext, callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The context scope of the observer. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

