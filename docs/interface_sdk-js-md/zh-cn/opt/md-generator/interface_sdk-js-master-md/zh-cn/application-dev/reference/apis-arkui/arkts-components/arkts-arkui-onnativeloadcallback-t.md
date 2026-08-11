# OnNativeLoadCallback

```TypeScript
declare type OnNativeLoadCallback = (event?: object) => void
```

XComponent的Native加载完成后回调事件，用于向开发者传递XComponent实例对象的context。与[onSurfaceCreated](arkts-arkui-xcomponentcontroller-c.md#onsurfacecreated)的区别：onLoad回调参数为context对象，适用于设置libraryname参数的场景；onSurfaceCreated回调参数为surfaceId，适用于未设置libraryname参数的场景。onLoad触发时机早于onSurfaceCreated。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type OnNativeLoadCallback = (event?: object) => void--><!--Device-unnamed-declare type OnNativeLoadCallback = (event?: object) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | object | 否 |
