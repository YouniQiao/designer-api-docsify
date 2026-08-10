# RequestParameterForStage (System API)

用于设置Stage模型下使用pluginComponentManager.request方法时需要传递的参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-pluginComponentManager-export interface RequestParameterForStage--><!--Device-pluginComponentManager-export interface RequestParameterForStage-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## data

```TypeScript
data: KVObject
```

附加数据，以键值对形式存储。用于向组件提供方传递请求时的自定义业务参数，以便提供方根据这些数据返回合适的组件模板。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameterForStage-data: KVObject--><!--Device-RequestParameterForStage-data: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## jsonPath

```TypeScript
jsonPath?: string
```

存放模板路径的external.json文件的路径。当需要从external.json文件加载模板路径而非通过Request通信获取模板时传入此参数。当jsonPath字段不为空时不触发Request通信；当jsonPath为空（默认）时，通过Request通信向组件提供方请求组件模板。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameterForStage-jsonPath?: string--><!--Device-RequestParameterForStage-jsonPath?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## name

```TypeScript
name: string
```

请求组件名称，当jsonPath不为空时需与external.json文件中的键名一致。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameterForStage-name: string--><!--Device-RequestParameterForStage-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## owner

```TypeScript
owner: Want
```

组件使用方Ability信息。

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameterForStage-owner: Want--><!--Device-RequestParameterForStage-owner: Want-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## target

```TypeScript
target: Want
```

组件提供方Ability信息。

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameterForStage-target: Want--><!--Device-RequestParameterForStage-target: Want-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

