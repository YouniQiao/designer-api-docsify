# RequestCallbackParameters

pluginComponentManager.request方法接收到的回调结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-pluginComponentManager-export interface RequestCallbackParameters--><!--Device-pluginComponentManager-export interface RequestCallbackParameters-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## componentTemplate

```TypeScript
componentTemplate: PluginComponentTemplate
```

组件模板。

**Type:** [PluginComponentTemplate](arkts-arkui-plugincomponent-plugincomponenttemplate-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestCallbackParameters-componentTemplate: PluginComponentTemplate--><!--Device-RequestCallbackParameters-componentTemplate: PluginComponentTemplate-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## data

```TypeScript
data: KVObject
```

组件数据，以键值对形式存储，键和值类型由业务定义。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestCallbackParameters-data: KVObject--><!--Device-RequestCallbackParameters-data: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraData

```TypeScript
extraData: KVObject
```

附加数据。该字段为可选字段，不提供时默认不包含在返回结果中。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestCallbackParameters-extraData: KVObject--><!--Device-RequestCallbackParameters-extraData: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

