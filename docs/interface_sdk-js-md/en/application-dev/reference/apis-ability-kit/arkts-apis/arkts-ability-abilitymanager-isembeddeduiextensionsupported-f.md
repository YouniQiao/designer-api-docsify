# isEmbeddedUIExtensionSupported

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## isEmbeddedUIExtensionSupported

```TypeScript
function isEmbeddedUIExtensionSupported(): boolean
```

开发者通过调用该接口判断[EmbeddedUIExtensionAbility](../../../application-models/embeddeduiextensionability.md)是否可以在当前设备上使用。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityManager-function isEmbeddedUIExtensionSupported(): boolean--><!--Device-abilityManager-function isEmbeddedUIExtensionSupported(): boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前设备是否支持[EmbeddedUIExtensionAbility](../../../application-models/embeddeduiextensionability.md)。返回 true表示当前设备支持；返回false表示当前设备不支持。 |

