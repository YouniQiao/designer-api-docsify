# PluginComponentOptions (System API)

定义用于构造插件组件的选项。

> **说明：**
> 
> 为了规范化匿名对象定义，此处的元素定义已在API版本18中进行修订。
> 虽然为匿名对象保留了历史版本信息，但可能会出现外层元素的@since版本号高于内层元素的情况。这不影响接口的可用性。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-declare interface PluginComponentOptions--><!--Device-unnamed-declare interface PluginComponentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## data

```TypeScript
data: any
```

传给插件组件提供方使用的数据，类型不限（支持对象、字符串等）。具体数据格式由使用方与提供方协商定义。

**Type:** any

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-PluginComponentOptions-data: any--><!--Device-PluginComponentOptions-data: any-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## template

```TypeScript
template: PluginComponentTemplate
```

插件组件模板。

**Type:** [PluginComponentTemplate](../arkts-apis/arkts-arkui-plugincomponent-plugincomponenttemplate-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-PluginComponentOptions-template: PluginComponentTemplate--><!--Device-PluginComponentOptions-template: PluginComponentTemplate-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

