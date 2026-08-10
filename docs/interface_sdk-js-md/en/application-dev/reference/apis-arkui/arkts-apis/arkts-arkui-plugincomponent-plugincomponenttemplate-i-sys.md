# PluginComponentTemplate (System API)

定义插件组件模板信息，用于与提供方定义的组件绑定。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface PluginComponentTemplate--><!--Device-unnamed-export interface PluginComponentTemplate-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string | undefined
```

提供方应用的bundleName。使用绝对路径提供模板时不需要填写，使用应用包提供模板时需要填写。

**Type:** string \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PluginComponentTemplate-bundleName: string | undefined--><!--Device-PluginComponentTemplate-bundleName: string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## source

```TypeScript
source: string | undefined
```

组件模板，取值可为模板绝对路径（不建议）、相对HAP包的相对路径（多HAP场景使用“相对路径&模块名称”格式）或FA模型下的AbilityName。

**Type:** string \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PluginComponentTemplate-source: string | undefined--><!--Device-PluginComponentTemplate-source: string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

