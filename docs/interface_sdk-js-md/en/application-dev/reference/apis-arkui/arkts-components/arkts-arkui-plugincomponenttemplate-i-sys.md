# PluginComponentTemplate (System API)

定义插件组件模板信息，用于与提供方定义的组件绑定。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-unnamed-interface PluginComponentTemplate--><!--Device-unnamed-interface PluginComponentTemplate-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

提供方应用的bundleName。使用绝对路径提供模板时不需要填写，使用应用包提供模板时需要填写。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-PluginComponentTemplate-bundleName: string--><!--Device-PluginComponentTemplate-bundleName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## source

```TypeScript
source: string
```

组件模板，取值可为模板绝对路径（不建议）、相对HAP包的相对路径（多HAP场景使用"相对路径&模块名称"格式）或FA模型下的AbilityName。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-PluginComponentTemplate-source: string--><!--Device-PluginComponentTemplate-source: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

