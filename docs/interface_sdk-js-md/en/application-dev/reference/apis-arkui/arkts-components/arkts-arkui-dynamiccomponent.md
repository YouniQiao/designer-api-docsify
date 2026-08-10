# DynamicComponent

**DynamicComponent**用于支持在本页面内嵌入显示独立Abc（.abc文件）提供的UI，展示的内容在Worker线程中运行。

通常用于动态加载Abc页面的模块化开发场景。通过Worker线程隔离运行Abc UI，避免阻塞主线程，提升应用流畅度。

## 子组件

无

## DynamicComponent

```TypeScript
DynamicComponent(options: DynamicOptions)
```

创建DynamicComponent组件，用于显示Worker线程中运行的Abc UI。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DynamicComponentInterface-(options: DynamicOptions): DynamicComponentAttribute--><!--Device-DynamicComponentInterface-(options: DynamicOptions): DynamicComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DynamicOptions](arkts-arkui-dynamicoptions-i-sys.md) | Yes | DynamicComponent的构造配置参数，用于配置要加载的Abc页面入口、运行Worker及显示选项。 |

## Summary

- [DynamicOptions](arkts-arkui-dynamiccomponent-dynamicoptions-i-sys.md)
- [ErrorCallback](arkts-arkui-dynamiccomponent-errorcallback-t-sys.md)
- [Worker](arkts-arkui-dynamiccomponent-worker-t-sys.md)
