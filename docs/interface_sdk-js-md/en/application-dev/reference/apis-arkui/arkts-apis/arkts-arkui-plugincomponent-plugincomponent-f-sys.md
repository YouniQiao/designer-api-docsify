# PluginComponent (System API)

## PluginComponent

```TypeScript
export declare function PluginComponent(
    options: PluginComponentOptions
): PluginComponentAttribute
```

Defines PluginComponent Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function PluginComponent(    options: PluginComponentOptions): PluginComponentAttribute--><!--Device-unnamed-export declare function PluginComponent(    options: PluginComponentOptions): PluginComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PluginComponentOptions](../arkts-components/arkts-arkui-plugincomponentoptions-i-sys.md) | Yes | The options |

**Return value:**

| Type | Description |
| --- | --- |
| [PluginComponentAttribute](../arkts-components/arkts-arkui-plugincomponent-attribute.md) |  |


## PluginComponent

```TypeScript
export declare function PluginComponent(
    style: CustomBuilderT<PluginComponentAttribute>
): PluginComponentAttribute
```

Defines PluginComponent Component.It requires call setPluginComponentOptions at start of the component attribute set-up,and it requires call applyAttributeFinish at the end of the component attribute set-up.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function PluginComponent(    style: CustomBuilderT<PluginComponentAttribute>): PluginComponentAttribute--><!--Device-unnamed-export declare function PluginComponent(    style: CustomBuilderT<PluginComponentAttribute>): PluginComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;PluginComponentAttribute&gt; | Yes | the callback to set up plugincomponent's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [PluginComponentAttribute](../arkts-components/arkts-arkui-plugincomponent-attribute.md) | The attribute of the PluginComponent. |

