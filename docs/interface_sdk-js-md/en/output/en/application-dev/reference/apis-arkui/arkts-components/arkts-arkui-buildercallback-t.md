# BuilderCallback

```TypeScript
declare type BuilderCallback<Args extends Object[] = any[]> = (...args: Args) => void
```

Defines the callback type used in mutableBuilder.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-declare type BuilderCallback<Args extends Object[] = any[]> = (...args: Args) => void--><!--Device-unnamed-declare type BuilderCallback<Args extends Object[] = any[]> = (...args: Args) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | Args | Yes | The parameter of MutableBuilder.  |

