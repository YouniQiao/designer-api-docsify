# ModifierKeyStateGetter

```TypeScript
export type ModifierKeyStateGetter = (keys: Array<string>) => boolean
```

The modifier key state query function block.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ModifierKeyStateGetter = (keys: Array<string>) => boolean--><!--Device-unnamed-export type ModifierKeyStateGetter = (keys: Array<string>) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | Yes | Indicate the modifier keys to query.  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - the query result |

