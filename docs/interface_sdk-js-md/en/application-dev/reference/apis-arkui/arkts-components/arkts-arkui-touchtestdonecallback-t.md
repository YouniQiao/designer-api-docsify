# TouchTestDoneCallback

```TypeScript
declare type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void
```

Represents the callback type for dynamically specifying gesture recognizer participation in gesture processing.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-unnamed-declare type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void--><!--Device-unnamed-declare type TouchTestDoneCallback = (event: BaseGestureEvent, recognizers: Array<GestureRecognizer>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Basic gesture event information after \_\_\_MD\_LINK\_USD\_0\_\_\_ completes.\_\_\_HTML\_TAG\_USD\_1\_\_\_**NOTE**\_\_\_HTML\_TAG\_USD\_2\_\_\_Only **BaseGestureEvent** information is contained, excluding child class extensions.\_\_\_HTML\_TAG\_USD\_3\_\_\_The values of **axisHorizontal** and **axisVertical** are **0**.  |
| recognizers | Array&lt;GestureRecognizer&gt; | Yes | All gesture recognizers after \_\_\_MD\_LINK\_USD\_0\_\_\_ completes.  |

