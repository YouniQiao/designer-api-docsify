# OnReleaseCallback

```TypeScript
export type OnReleaseCallback = (msg: string) => void
```

Defines the callback that is invoked when the stub on the target UIAbility is disconnected.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnReleaseCallback = (msg: string) => void--><!--Device-unnamed-export type OnReleaseCallback = (msg: string) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msg | string | Yes | Message used for disconnection. |

