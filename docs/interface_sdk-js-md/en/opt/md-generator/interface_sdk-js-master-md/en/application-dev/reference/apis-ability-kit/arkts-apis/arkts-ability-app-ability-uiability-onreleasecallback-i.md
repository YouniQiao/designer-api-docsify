# OnReleaseCallback

Defines the callback that is invoked when the stub on the target UIAbility is disconnected.

**Since:** 9

<!--Device-unnamed-export interface OnReleaseCallback--><!--Device-unnamed-export interface OnReleaseCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { Callee, Caller, OnReleaseCallback, OnRemoteStateChangeCallback, CalleeCallback } from '@kit.AbilityKit';
```

## [[Call]]

```TypeScript
(msg: string): void
```

Defines the callback of OnRelease.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-OnReleaseCallback-(msg: string): void--><!--Device-OnReleaseCallback-(msg: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msg | string | Yes |
