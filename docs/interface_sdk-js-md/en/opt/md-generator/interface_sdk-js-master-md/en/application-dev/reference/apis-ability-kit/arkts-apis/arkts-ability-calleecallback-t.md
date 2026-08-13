# CalleeCallback

```TypeScript
export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable
```

Defines the callback of the registration message notification of the UIAbility.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable--><!--Device-unnamed-export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| indata | rpc.MessageSequence | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| rpc.Parcelable |
