# InteractionModalUIExtension (System API)

Defines the information of the modal UIExtension to be displayed as the interaction UI after the current intent execution completes. Does not support distributed scenarios.

**Inheritance/Implementation:** InteractionModalUIExtension extends [InteractionUI](arkts-ability-insightintent-interactionui-i-sys.md#interactionui-system-api)

**Since:** 26.1.0

<!--Device-insightIntent-interface InteractionModalUIExtension--><!--Device-insightIntent-interface InteractionModalUIExtension-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## abilityName

```TypeScript
abilityName: string
```

Ability name of the target UIExtension ability.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-abilityName: string--><!--Device-InteractionModalUIExtension-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the target UIExtension ability.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-bundleName: string--><!--Device-InteractionModalUIExtension-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## interactionUIType

```TypeScript
interactionUIType: 'MODAL_UIEXTENSION'
```

Type of the interaction UI. The value is fixed to 'MODAL_UIEXTENSION'.

**Type:** 'MODAL_UIEXTENSION'

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-interactionUIType: 'MODAL_UIEXTENSION'--><!--Device-InteractionModalUIExtension-interactionUIType: 'MODAL_UIEXTENSION'-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName: string
```

Module name of the target UIExtension ability.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-moduleName: string--><!--Device-InteractionModalUIExtension-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## parameters

```TypeScript
parameters: Record<string, RecordData>
```

Parameters passed to the target UIExtension ability.

**Type:** [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-parameters: Record<string, RecordData>--><!--Device-InteractionModalUIExtension-parameters: Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uiExtensionType

```TypeScript
uiExtensionType: string
```

Type of the UIExtension ability.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-uiExtensionType: string--><!--Device-InteractionModalUIExtension-uiExtensionType: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## uri

```TypeScript
uri: string
```

URI information passed to the target UIExtension ability for data processing.

**Type:** string

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionModalUIExtension-uri: string--><!--Device-InteractionModalUIExtension-uri: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.
