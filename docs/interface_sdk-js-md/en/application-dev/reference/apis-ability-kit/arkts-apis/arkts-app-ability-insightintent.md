# @ohos.app.ability.insightIntent

This module provides basic definitions of the  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace insightIntent--><!--Device-unnamed-declare namespace insightIntent-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AppIntentEntity](arkts-ability-insightintent-appintententity-c.md) | Define AppIntentEntity. |

### Interfaces

| Name | Description |
| --- | --- |
| [ExecuteResult](arkts-ability-insightintent-executeresult-i.md) | Enumerates the return results of intent execution. |
| [IntentEntity](arkts-ability-insightintent-intententity-i.md) | Defines the struct of an intent entity. It represents key information objects involved during intent execution,including intent parameters and execution results.  You can define intent entities by inheriting this class. The child class must be decorated with  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| [IntentResult](arkts-ability-insightintent-intentresult-i.md) | Defines the return result of intent execution. The  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is supported. |
| [QueryEntityParam](arkts-ability-insightintent-queryentityparam-i.md) | Parameter for query entity. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ExecuteResult](arkts-ability-insightintent-executeresult-i-sys.md) | Enumerates the return results of intent execution. |
| [IntentResult](arkts-ability-insightintent-intentresult-i-sys.md) | Defines the return result of intent execution. The  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is supported. |
| [InteractionInfo](arkts-ability-insightintent-interactioninfo-i-sys.md) | Defines the interaction information returned after the current intent execution completes, including the next intent to be triggered and the interaction UI to be displayed. |
| [InteractionModalUIExtension](arkts-ability-insightintent-interactionmodaluiextension-i-sys.md) | Defines the information of the modal UIExtension to be displayed as the interaction UI after the current intent execution completes. Does not support distributed scenarios. |
| [InteractionUI](arkts-ability-insightintent-interactionui-i-sys.md) | Defines the base information of the interaction UI to be displayed after the current intent execution completes.This is a base class. Use its subclasses such as \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ in practice. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ExecuteMode](arkts-ability-insightintent-executemode-e.md) | Enumerates the intent execution modes. It specifies the mode of execution passed when the intent is triggered by a system entry point. The supported execution modes for each intent are defined during intent development. |
| [QueryType](arkts-ability-insightintent-querytype-e.md) | Enum for query entity mode. |
| [ReturnMode](arkts-ability-insightintent-returnmode-e.md) | Enumerates the modes that define how the execution result of an intent is returned to the intent initiator. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ExecuteMode](arkts-ability-insightintent-executemode-e-sys.md) | Enumerates the intent execution modes. It specifies the mode of execution passed when the intent is triggered by a system entry point. The supported execution modes for each intent are defined during intent development. |
<!--DelEnd-->

