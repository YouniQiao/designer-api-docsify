# IProvideDecoratedVariable

Define Provide decoration variable interface.

**Inheritance/Implementation:** IProvideDecoratedVariable extends IDecoratedMutableVariable<T>, IDecoratedV1Variable<T>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface IProvideDecoratedVariable--><!--Device-unnamed-export declare interface IProvideDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(newValue: T): void
```

Provide Link variable when the @Reusable Component instance is reused.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IProvideDecoratedVariable-resetOnReuse(newValue: T): void--><!--Device-IProvideDecoratedVariable-resetOnReuse(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | default value |

