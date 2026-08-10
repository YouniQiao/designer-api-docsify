# CompatibleInitCallback

```TypeScript
export type CompatibleInitCallback = (parent: ESValue) => CompatibleComponentInfo
```

初始化占位组件的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

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
| [CompatibleComponentInfo](arkts-arkui-interop-compatiblecomponentinfo-i.md) | 占位组件的信息。 |

