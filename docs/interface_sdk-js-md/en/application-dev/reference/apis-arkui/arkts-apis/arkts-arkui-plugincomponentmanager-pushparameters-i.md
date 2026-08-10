# PushParameters

使用pluginComponentManager.push方法时需要传递的参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-pluginComponentManager-export interface PushParameters--><!--Device-pluginComponentManager-export interface PushParameters-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## data

```TypeScript
data: KVObject
```

组件数据，以键值对形式存储，用于传递给组件使用方的业务数据，键和值类型由业务定义。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameters-data: KVObject--><!--Device-PushParameters-data: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraData

```TypeScript
extraData: KVObject
```

附加数据，以键值对形式存储，用于传递额外的业务信息，键和值类型由业务定义。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameters-extraData: KVObject--><!--Device-PushParameters-extraData: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## jsonPath

```TypeScript
jsonPath?: string
```

存放模板路径的external.json文件的路径。当需要通过外部配置文件直接加载模板而非通过push通信发送时传入此参数；当jsonPath字段不为空时不触发push通信，直接从external.json中读取模板路径进行加载。不传入或为空时，触发push通信向组件使用方推送组件和数据。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameters-jsonPath?: string--><!--Device-PushParameters-jsonPath?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: string
```

组件名称。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameters-name: string--><!--Device-PushParameters-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## want

```TypeScript
want: Want
```

组件使用方Ability信息。

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PushParameters-want: Want--><!--Device-PushParameters-want: Want-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

