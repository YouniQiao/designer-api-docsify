# RequestEventResult

注册request监听方法后，接收到请求事件时回应请求的数据类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-pluginComponentManager-export interface RequestEventResult--><!--Device-pluginComponentManager-export interface RequestEventResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## data

```TypeScript
data?: KVObject
```

组件数据，以键值对形式存储，用于回应请求时传递的业务数据，键和值类型由业务定义。该字段为可选字段，不提供时默认不包含在返回结果中。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestEventResult-data?: KVObject--><!--Device-RequestEventResult-data?: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extraData

```TypeScript
extraData?: KVObject
```

request事件中传递的附加数据。该字段为可选字段，不提供时默认不包含在返回结果中。

**Type:** [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestEventResult-extraData?: KVObject--><!--Device-RequestEventResult-extraData?: KVObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## template

```TypeScript
template?: string
```

组件模板。该字段为可选字段，不提供时默认不包含在返回结果中。当需要返回组件模板信息时设置此字段；不需要返回模板时可省略。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RequestEventResult-template?: string--><!--Device-RequestEventResult-template?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

