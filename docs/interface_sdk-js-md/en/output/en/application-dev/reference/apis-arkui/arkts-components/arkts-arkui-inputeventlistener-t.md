# InputEventListener

```TypeScript
declare type InputEventListener = (
  event: RawInputEventWrapper
) => InputEventInterceptResult
```

Input event listener callback type. > **NOTE** > > - **RawInputEventWrapper** is an abstract class. Developers cannot create instances using the \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ operator. > > - The system automatically creates instances when an event is triggered and passes them to the callback through > this parameter. > > - The current callback parameter **event** only encapsulates the following raw input event types: > [MouseEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, [TouchEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_, [KeyEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. Developers can obtain > the corresponding event objects using [asMouseEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_, > [asTouchEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_, and [asKeyEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_6\_\_\_. > > - Do not perform time-consuming operations (such as complex calculations or network requests) in the callback, as > this may cause application lag. > > - The listener executes synchronously on the UI thread, which directly blocks the event processing flow. It is > recommended to only perform simple judgment and calculation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type InputEventListener = (  event: RawInputEventWrapper) => InputEventInterceptResult--><!--Device-unnamed-declare type InputEventListener = (  event: RawInputEventWrapper) => InputEventInterceptResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Input event wrapper. The system automatically creates and passes it. Developers do not need to create it manually.  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Event interception result. |

