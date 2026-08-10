# PluginErrorCallback (System API)

```TypeScript
export type PluginErrorCallback = (info: PluginErrorData) => void
```

发生错误时触发事件回调。AnonyMous Object Rectification

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type PluginErrorCallback = (info: PluginErrorData) => void--><!--Device-unnamed-export type PluginErrorCallback = (info: PluginErrorData) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| info | [PluginErrorData](arkts-arkui-plugincomponent-pluginerrordata-i-sys.md) | Yes | 发生错误时提供的数据。 |

