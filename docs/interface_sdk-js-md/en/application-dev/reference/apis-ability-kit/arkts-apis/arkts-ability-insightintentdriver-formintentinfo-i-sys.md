# FormIntentInfo (System API)

FormIntentInfo用于描述  
[@InsightIntentForm](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentform)装饰器支持的参数，例如卡片名称。同时，该接口也可用于描述[使用配置文件开发的意图](../../../application-models/insight-intent-config-development.md)所绑定的卡片信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-insightIntentDriver-interface FormIntentInfo--><!--Device-insightIntentDriver-interface FormIntentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## abilityName

```TypeScript
readonly abilityName: string
```

Ability名称。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormIntentInfo-readonly abilityName: string--><!--Device-FormIntentInfo-readonly abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## formName

```TypeScript
readonly formName: string
```

表示[FormExtensionAbility](../../apis-form-kit/arkts-apis/arkts-app-form-formextensionability.md/arkts-app-form-formextensionability.md)绑定的卡片名称。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormIntentInfo-readonly formName: string--><!--Device-FormIntentInfo-readonly formName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

