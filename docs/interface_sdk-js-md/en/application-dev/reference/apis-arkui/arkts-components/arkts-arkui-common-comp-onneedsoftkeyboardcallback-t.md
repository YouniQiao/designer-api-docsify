# OnNeedSoftkeyboardCallback

```TypeScript
declare type OnNeedSoftkeyboardCallback = () => boolean
```

This callback is triggered when the component bound to this method determines whether a keyboard is required. Prerequisite: The component must be focusable; otherwise, this API does not take effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-unnamed-declare type OnNeedSoftkeyboardCallback = () => boolean--><!--Device-unnamed-declare type OnNeedSoftkeyboardCallback = () => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether the component needs a keyboard. <br>If the return value of this callback is `true`, the component needs a keyboard; if the return value is `false`, the component does not need a keyboard. |
