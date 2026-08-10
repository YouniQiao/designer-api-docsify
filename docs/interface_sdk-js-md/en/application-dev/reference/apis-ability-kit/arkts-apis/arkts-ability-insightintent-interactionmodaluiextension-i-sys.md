# InteractionModalUIExtension (System API)

定义当意图执行完成时模态UIExtension要显示为交互界面的信息，不支持分布式。

**Inheritance/Implementation:** InteractionModalUIExtension extends [InteractionUI](arkts-ability-insightintent-interactionui-i-sys.md)

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

<!--Device-insightIntent-interface InteractionModalUIExtension extends InteractionUI--><!--Device-insightIntent-interface InteractionModalUIExtension extends InteractionUI-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntent } from 'kits/@kit.AbilityKit';
```

## abilityName

```TypeScript
abilityName: string
```

目标UIExtension能力的Ability名称。

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-abilityName: string--><!--Device-InteractionModalUIExtension-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

目标UIExtension能力的Bundle名称。

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-bundleName: string--><!--Device-InteractionModalUIExtension-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## interactionUIType

```TypeScript
interactionUIType: 'MODAL_UIEXTENSION'
```

交互界面的类型，固定为'MODAL_UIEXTENSION'。

**Type:** 'MODAL_UIEXTENSION'

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-interactionUIType: 'MODAL_UIEXTENSION'--><!--Device-InteractionModalUIExtension-interactionUIType: 'MODAL_UIEXTENSION'-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName: string
```

目标UIExtension能力的模块名称。

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-moduleName: string--><!--Device-InteractionModalUIExtension-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## parameters

```TypeScript
parameters: Record<string, Object>
```

传递给目标UIExtension的参数。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-parameters: Record<string, Object>--><!--Device-InteractionModalUIExtension-parameters: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uiExtensionType

```TypeScript
uiExtensionType: string
```

UIExtension的类型。

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-uiExtensionType: string--><!--Device-InteractionModalUIExtension-uiExtensionType: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uri

```TypeScript
uri: string
```

传递给目标UIExtension的URI信息。

**Type:** string

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-uri: string--><!--Device-InteractionModalUIExtension-uri: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

