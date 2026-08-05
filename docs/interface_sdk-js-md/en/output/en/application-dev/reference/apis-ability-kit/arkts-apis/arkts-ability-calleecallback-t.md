# CalleeCallback

```TypeScript
export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable
```

Defines the callback of the registration message notification of the UIAbility.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable--><!--Device-unnamed-export type CalleeCallback = (indata: rpc.MessageSequence) => rpc.Parcelable-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indata | rpc.MessageSequence | Yes | Data to be transferred.  |

**Return value:**

| Type | Description |
| --- | --- |
| rpc.Parcelable | Returned data object. |

