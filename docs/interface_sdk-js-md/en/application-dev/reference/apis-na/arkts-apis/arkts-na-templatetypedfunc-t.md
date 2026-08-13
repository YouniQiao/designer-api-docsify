# TemplateTypedFunc

```TypeScript
type TemplateTypedFunc<T> = (item: T, index: int) => string
```

Function that returns typed string to render one template.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type TemplateTypedFunc<T> = (item: T, index: int) => string--><!--Device-unnamed-type TemplateTypedFunc<T> = (item: T, index: int) => string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| item | T | Yes | data item. |
| index | int | Yes | data index in array. |

**Return value:**

| Type | Description |
| --- | --- |
| string | template type. |

