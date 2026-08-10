# IPropRefDecoratedVariable

Define PropRef decoration variable interface.

**Inheritance/Implementation:** IPropRefDecoratedVariable extends [IDecoratedMutableVariable<T>](IDecoratedMutableVariable<T>), [IDecoratedUpdatableVariable<T>](IDecoratedUpdatableVariable<T>), [IDecoratedV1Variable<T>](IDecoratedV1Variable<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IPropRefDecoratedVariable<T> extends IDecoratedMutableVariable<T>,    IDecoratedUpdatableVariable<T>, IDecoratedV1Variable<T>--><!--Device-unnamed-export declare interface IPropRefDecoratedVariable<T> extends IDecoratedMutableVariable<T>,    IDecoratedUpdatableVariable<T>, IDecoratedV1Variable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(newValue: T): void
```

当组件被复用时，重置状态变量。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IPropRefDecoratedVariable-resetOnReuse(newValue: T): void--><!--Device-IPropRefDecoratedVariable-resetOnReuse(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes | 默认值 |

