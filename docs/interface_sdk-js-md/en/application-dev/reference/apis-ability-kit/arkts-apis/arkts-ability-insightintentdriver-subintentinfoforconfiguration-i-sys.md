# SubIntentInfoForConfiguration (System API)

用于描述[使用配置文件开发的意图](../../../application-models/insight-intent-config-development.md)的特有信息。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-insightIntentDriver-interface SubIntentInfoForConfiguration--><!--Device-insightIntentDriver-interface SubIntentInfoForConfiguration-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## entities

```TypeScript
readonly entities?: Record<string, Object>
```

表示意图包含的实体信息。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubIntentInfoForConfiguration-readonly entities?: Record<string, Object>--><!--Device-SubIntentInfoForConfiguration-readonly entities?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## form

```TypeScript
readonly form?: FormIntentInfo
```

表示意图绑定的卡片信息。

**Type:** [FormIntentInfo](arkts-ability-insightintentdriver-formintentinfo-i-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubIntentInfoForConfiguration-readonly form?: FormIntentInfo--><!--Device-SubIntentInfoForConfiguration-readonly form?: FormIntentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## inputParams

```TypeScript
readonly inputParams?: Array<Record<string, Object>>
```

表示意图参数的数据格式声明，用于意图调用时定义入参的数据格式。

**Type:** Array&lt;Record&lt;string, Object&gt;&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubIntentInfoForConfiguration-readonly inputParams?: Array<Record<string, Object>>--><!--Device-SubIntentInfoForConfiguration-readonly inputParams?: Array<Record<string, Object>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## outputParams

```TypeScript
readonly outputParams?: Array<Record<string, Object>>
```

表示意图调用返回结果的数据格式声明，用于定义意图调用返回结果的数据格式。

**Type:** Array&lt;Record&lt;string, Object&gt;&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubIntentInfoForConfiguration-readonly outputParams?: Array<Record<string, Object>>--><!--Device-SubIntentInfoForConfiguration-readonly outputParams?: Array<Record<string, Object>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## serviceExtension

```TypeScript
readonly serviceExtension?: ServiceExtensionIntentInfo
```

表示意图绑定的ServiceExtensionAbility组件信息。

**Type:** [ServiceExtensionIntentInfo](arkts-ability-insightintentdriver-serviceextensionintentinfo-i-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubIntentInfoForConfiguration-readonly serviceExtension?: ServiceExtensionIntentInfo--><!--Device-SubIntentInfoForConfiguration-readonly serviceExtension?: ServiceExtensionIntentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## srcEntry

```TypeScript
readonly srcEntry: string
```

表示意图执行文件的相对路径，取值为长度不超过127字节的字符串。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubIntentInfoForConfiguration-readonly srcEntry: string--><!--Device-SubIntentInfoForConfiguration-readonly srcEntry: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uiAbility

```TypeScript
readonly uiAbility?: UIAbilityIntentInfo
```

表示意图绑定的UIAbility组件信息，包含"ability"字段和"executeMode"字段。

**Type:** [UIAbilityIntentInfo](arkts-ability-insightintentdriver-uiabilityintentinfo-i-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubIntentInfoForConfiguration-readonly uiAbility?: UIAbilityIntentInfo--><!--Device-SubIntentInfoForConfiguration-readonly uiAbility?: UIAbilityIntentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uiExtension

```TypeScript
readonly uiExtension?: UIExtensionIntentInfo
```

表示意图绑定的UIExtensionAbility组件信息。

**Type:** [UIExtensionIntentInfo](arkts-ability-insightintentdriver-uiextensionintentinfo-i-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SubIntentInfoForConfiguration-readonly uiExtension?: UIExtensionIntentInfo--><!--Device-SubIntentInfoForConfiguration-readonly uiExtension?: UIExtensionIntentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

