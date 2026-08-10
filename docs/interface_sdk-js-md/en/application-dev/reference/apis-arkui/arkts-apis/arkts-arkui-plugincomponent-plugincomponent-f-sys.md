# PluginComponent (System API)

## PluginComponent

```TypeScript
export declare function PluginComponent(
    options: PluginComponentOptions
): PluginComponentAttribute
```

创建插件组件，用于显示外部应用提供的UI。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function PluginComponent(    options: PluginComponentOptions): PluginComponentAttribute--><!--Device-unnamed-export declare function PluginComponent(    options: PluginComponentOptions): PluginComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PluginComponentOptions](../arkts-components/arkts-arkui-plugincomponentoptions-i-sys.md) | Yes | 定义用于构造插件组件的选项。 |

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

定义PluginComponent组件。它要求在组件属性设置开始时调用setPluginComponentOptions，并在组件属性设置结束时调用applyAttributeFinish。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function PluginComponent(    style: CustomBuilderT<PluginComponentAttribute>): PluginComponentAttribute--><!--Device-unnamed-export declare function PluginComponent(    style: CustomBuilderT<PluginComponentAttribute>): PluginComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;PluginComponentAttribute&gt; | Yes | 用于设置plugincomponent属性的回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PluginComponentAttribute](../arkts-components/arkts-arkui-plugincomponent-attribute.md) | PluginComponent的属性。 |

