# PluginErrorCallback (System API)

```TypeScript
declare type PluginErrorCallback = (info: PluginErrorData) => void
```

发生错误时触发的回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type PluginErrorCallback = (info: PluginErrorData) => void--><!--Device-unnamed-declare type PluginErrorCallback = (info: PluginErrorData) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [PluginErrorData](../arkts-apis/arkts-arkui-plugincomponent-pluginerrordata-i-sys.md) | Yes | 插件错误数据 |

