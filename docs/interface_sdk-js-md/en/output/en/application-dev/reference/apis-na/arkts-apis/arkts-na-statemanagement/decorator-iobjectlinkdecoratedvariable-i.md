# IObjectLinkDecoratedVariable

Define ObjectLink decoration variable interface.

**Inheritance/Implementation:** IObjectLinkDecoratedVariable extends [IDecoratedImmutableVariable<T>](IDecoratedImmutableVariable<T>), [IDecoratedUpdatableVariable<T>](IDecoratedUpdatableVariable<T>), [IDecoratedV1Variable<T>](IDecoratedV1Variable<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IObjectLinkDecoratedVariable<T> extends IDecoratedImmutableVariable<T>,    IDecoratedUpdatableVariable<T>, IDecoratedV1Variable<T>--><!--Device-unnamed-export declare interface IObjectLinkDecoratedVariable<T> extends IDecoratedImmutableVariable<T>,    IDecoratedUpdatableVariable<T>, IDecoratedV1Variable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(newValue: T): void
```

Reset ObjectLink variable when the @Reusable Component instance is reused.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IObjectLinkDecoratedVariable-resetOnReuse(newValue: T): void--><!--Device-IObjectLinkDecoratedVariable-resetOnReuse(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | default value |

