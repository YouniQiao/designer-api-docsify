# TriggerInfo

The module defines the information required for triggering the WantAgent. The information is used as an input parameter of \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface TriggerInfo--><!--Device-unnamed-export interface TriggerInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## code

```TypeScript
code: int
```

Common event code. This field is valid only when \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ of the WantAgent instance is **'SEND\_COMMON\_EVENT'**. The meaning of this field is the same as that of the **code** field set in \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_ when the publisher uses [commonEventManager.publish]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to publish common events.

**Type:** int

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-code: int--><!--Device-TriggerInfo-code: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extraInfo

```TypeScript
extraInfo?: { [key: string]: any }
```

Extra information.

**Type:** { [key: string]: any }

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-extraInfo?: { [key: string]: any }--><!--Device-TriggerInfo-extraInfo?: { [key: string]: any }-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## extraInfos

```TypeScript
extraInfos?: Record<string, Object>
```

Extra information. You are advised to use this property to replace **extraInfo**. When this property is set, **extraInfo** does not take effect.

**Type:** Record&lt;string, Object&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-extraInfos?: Record<string, Object>--><!--Device-TriggerInfo-extraInfos?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## permission

```TypeScript
permission?: string
```

Permission required for a subscriber to receive the common event. This field is valid only when \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ of the WantAgent instance is **'SEND\_COMMON\_EVENT'**.

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-permission?: string--><!--Device-TriggerInfo-permission?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## want

```TypeScript
want?: Want
```

Carrier for information transfer between objects (application components).

**Type:** Want

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TriggerInfo-want?: Want--><!--Device-TriggerInfo-want?: Want-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

