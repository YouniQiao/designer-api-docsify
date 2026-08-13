# CalleeCallback

Defines the callback of the registration message notification of the UIAbility.

**Since:** 9

**Deprecated since:** -1

<!--Device-unnamed-export interface CalleeCallback--><!--Device-unnamed-export interface CalleeCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { Callee, Caller, OnReleaseCallback, OnRemoteStateChangeCallback, CalleeCallback } from '@kit.AbilityKit';
```

## constructor

```TypeScript
(indata: rpc.MessageSequence): rpc.Parcelable
```

Defines the callback of Callee.

**Since:** 9

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-CalleeCallback-(indata: rpc.MessageSequence): rpc.Parcelable--><!--Device-CalleeCallback-(indata: rpc.MessageSequence): rpc.Parcelable-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| indata | rpc.MessageSequence | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rpc.Parcelable |
