# AbilityFirstFrameStateObserver (System API)

The module defines the observer used to listen for the first frame rendering completion event of a given ability. It is used as an input parameter of  
[on](./../@ohos.app.ability.appManager:appManager.on(type: 'abilityFirstFrameState', observer: AbilityFirstFrameStateObserver, bundleName?: string))to listen for the completion event.

**Since:** 12

<!--Device-unnamed-export interface AbilityFirstFrameStateObserver--><!--Device-unnamed-export interface AbilityFirstFrameStateObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## onAbilityFirstFrameDrawn

```TypeScript
onAbilityFirstFrameDrawn(data: AbilityFirstFrameStateData): void
```

Called when the first frame of the ability is rendered.

**Since:** 12

<!--Device-AbilityFirstFrameStateObserver-onAbilityFirstFrameDrawn(data: AbilityFirstFrameStateData): void--><!--Device-AbilityFirstFrameStateObserver-onAbilityFirstFrameDrawn(data: AbilityFirstFrameStateData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [AbilityFirstFrameStateData](arkts-ability-abilityfirstframestatedata-i-sys.md) | Yes |
