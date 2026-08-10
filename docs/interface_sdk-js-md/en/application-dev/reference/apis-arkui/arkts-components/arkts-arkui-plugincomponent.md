# PluginComponent

提供外部应用组件嵌入式显示功能，即外部应用提供的UI可在本应用内显示。适用于需要跨应用复用UI组件的场景，如嵌入其他应用的页面或卡片，实现应用间的界面协同与数据交互。如需通过跨进程通信实现更新，请参考[@ohos.pluginComponent]{@link @ohos.pluginComponent}。

## 子组件

不支持

## PluginComponent

```TypeScript
PluginComponent(options: PluginComponentOptions)
```

创建插件组件，用于显示外部应用提供的UI。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-PluginComponentInterface-(options: PluginComponentOptions): PluginComponentAttribute--><!--Device-PluginComponentInterface-(options: PluginComponentOptions): PluginComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PluginComponentOptions](arkts-arkui-plugincomponentoptions-i-sys.md) | Yes | 插件组件选项 |

## Summary

- [PluginComponentOptions](arkts-arkui-plugincomponent-plugincomponentoptions-i-sys.md)
- [PluginComponentTemplate](arkts-arkui-plugincomponent-plugincomponenttemplate-i-sys.md)
- [PluginErrorData](arkts-arkui-plugincomponent-pluginerrordata-i-sys.md)
- [PluginErrorCallback](arkts-arkui-plugincomponent-pluginerrorcallback-t-sys.md)
