# CompatibleInitCallback

```TypeScript
export type CompatibleInitCallback = (parent: ESValue) => CompatibleComponentInfo
```

Defines the callback for initializing compatible custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type CompatibleInitCallback = (parent: ESValue) => CompatibleComponentInfo--><!--Device-unnamed-export type CompatibleInitCallback = (parent: ESValue) => CompatibleComponentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| parent | ESValue | Yes | the parent of compatible custom component |

**Return value:**

| Type | Description |
| --- | --- |
| [CompatibleComponentInfo](arkts-na-interop-compatiblecomponentinfo-i.md) | the info of compatible custom component |

