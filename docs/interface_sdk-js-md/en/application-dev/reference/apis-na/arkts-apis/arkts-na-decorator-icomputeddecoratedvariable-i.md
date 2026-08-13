# IComputedDecoratedVariable

Defines computed decoration variable interface.

**Inheritance/Implementation:** IComputedDecoratedVariable extends IDecoratedReadableVariable<T>

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface IComputedDecoratedVariable--><!--Device-unnamed-export declare interface IComputedDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(): void
```

Reset Computed when the ComponentV2 instance is reused.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-IComputedDecoratedVariable-setOwner(owner: IVariableOwner): void--><!--Device-IComputedDecoratedVariable-setOwner(owner: IVariableOwner): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-na-decorator-ivariableowner-i.md) | Yes | owner of this variable |

