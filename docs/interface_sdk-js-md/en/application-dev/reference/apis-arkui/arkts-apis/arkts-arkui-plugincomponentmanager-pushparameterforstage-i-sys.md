# PushParameterForStage (System API)

用于设置Stage模型下使用pluginComponentManager.push方法时需要传递的参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-pluginComponentManager-export interface PushParameterForStage--><!--Device-pluginComponentManager-export interface PushParameterForStage-End-->

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

组件数据，以键值对形式存储。用于向组件使用方传递业务数据，如页面路径（key为'js'，value为模板路径字符串）及自定义数据字段。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameterForStage-data: KVObject--><!--Device-PushParameterForStage-data: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## extraData

```TypeScript
extraData: KVObject
```

附加数据，用于在发送组件时传递额外的自定义数据，与组件数据（data）区分，可根据业务需要设置。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameterForStage-extraData: KVObject--><!--Device-PushParameterForStage-extraData: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## jsonPath

```TypeScript
jsonPath?: string
```

存放模板路径的external.json文件的路径。当需要从external.json文件加载模板路径而非通过Push通信发送模板时传入此参数。当jsonPath字段不为空时不触发Push通信，组件模板路径从external.json文件中读取；当jsonPath为空（默认）时，通过Push通信向组件使用方发送组件模板。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameterForStage-jsonPath?: string--><!--Device-PushParameterForStage-jsonPath?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## name

```TypeScript
name: string
```

组件名称，当jsonPath不为空时需与external.json文件中的键名一致。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameterForStage-name: string--><!--Device-PushParameterForStage-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## owner

```TypeScript
owner: Want
```

组件提供方Ability信息。

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameterForStage-owner: Want--><!--Device-PushParameterForStage-owner: Want-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## target

```TypeScript
target: Want
```

组件使用方Ability信息。

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameterForStage-target: Want--><!--Device-PushParameterForStage-target: Want-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

