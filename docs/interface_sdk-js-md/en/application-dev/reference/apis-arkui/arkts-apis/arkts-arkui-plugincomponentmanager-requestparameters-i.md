# RequestParameters

使用pluginComponentManager.request方法时需要传递的参数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-pluginComponentManager-export interface RequestParameters--><!--Device-pluginComponentManager-export interface RequestParameters-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## data

```TypeScript
data: KVObject
```

组件数据，以键值对形式存储，用于传递给组件提供方的业务数据，键和值类型由业务定义。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameters-data: KVObject--><!--Device-RequestParameters-data: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## jsonPath

```TypeScript
jsonPath?: string
```

存放模板路径的external.json文件的路径。当需要通过外部配置文件直接加载模板而非通过request通信获取时传入此参数；当jsonPath字段不为空时不触发request通信，直接从external.json中读取模板路径。不传入或为空时，触发request通信向组件提供方请求模板。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameters-jsonPath?: string--><!--Device-RequestParameters-jsonPath?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: string
```

请求组件名称。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameters-name: string--><!--Device-RequestParameters-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## want

```TypeScript
want: Want
```

组件提供方Ability信息。

**Type:** [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestParameters-want: Want--><!--Device-RequestParameters-want: Want-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

