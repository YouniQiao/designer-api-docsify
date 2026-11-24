# ReuseIdCallback

```TypeScript
declare type ReuseIdCallback = () => string
```

Triggered to obtain the reuse ID.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type ReuseIdCallback = () => string--><!--Device-unnamed-declare type ReuseIdCallback = () => string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | Reuse ID specified by the developer. <br>If no reuse ID is specified or an empty string `''` is used, the custom component name is used by default. <br>Before API version 26.0.0, when the callback does not explicitly return a string literal, the actual reuse ID is the custom component name and the callback return value does not take effect. Since API version 26.0.0, the actual return value of the callback is used as the reuse ID. |
