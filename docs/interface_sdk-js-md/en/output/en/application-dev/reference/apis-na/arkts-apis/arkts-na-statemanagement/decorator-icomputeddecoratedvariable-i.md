# IComputedDecoratedVariable

Defines computed decoration variable interface.

**Inheritance/Implementation:** IComputedDecoratedVariable extends [IDecoratedReadableVariable<T>](IDecoratedReadableVariable<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IComputedDecoratedVariable<T> extends IDecoratedReadableVariable<T>--><!--Device-unnamed-export declare interface IComputedDecoratedVariable<T> extends IDecoratedReadableVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(): void
```

Reset Computed when the ComponentV2 instance is reused.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IComputedDecoratedVariable-resetOnReuse(): void--><!--Device-IComputedDecoratedVariable-resetOnReuse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setOwner

```TypeScript
setOwner(owner: IVariableOwner): void
```

Set owner for the computed variable. Used to detect component freezing.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IComputedDecoratedVariable-setOwner(owner: IVariableOwner): void--><!--Device-IComputedDecoratedVariable-setOwner(owner: IVariableOwner): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | owner of this variable |

