# OnNativeLoadCallback

```TypeScript
declare type OnNativeLoadCallback = (event?: object) => void
```

XComponent的Native加载完成后回调事件，用于向开发者传递XComponent实例对象的context。与[onSurfaceCreated](arkts-arkui-xcomponentcontroller-c.md#onsurfacecreated)的区别：onLoad回调参数为context对象，适用于设置libraryname参数的场景；onSurfaceCreated回调参数为surfaceId，适用于未设置libraryname参数的场景。onLoad触发时机早于onSurfaceCreated。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnNativeLoadCallback = (event?: object) => void--><!--Device-unnamed-declare type OnNativeLoadCallback = (event?: object) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | object | No | 获取XComponent实例对象的context，context上挂载的方法由开发者在Native层定义。不传该参数时无法获取context。 当需要在回调中使用Native层定义的方法时传入此参数；不传入时，回调中无法获取context对象。 |

