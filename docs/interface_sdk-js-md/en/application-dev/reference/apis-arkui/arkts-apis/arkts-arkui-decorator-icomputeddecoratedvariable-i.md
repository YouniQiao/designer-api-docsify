# IComputedDecoratedVariable

定义@Computed状态变量的接口

**Inheritance/Implementation:** IComputedDecoratedVariable extends [IDecoratedReadableVariable<T>](IDecoratedReadableVariable<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IComputedDecoratedVariable<T> extends IDecoratedReadableVariable<T>--><!--Device-unnamed-export declare interface IComputedDecoratedVariable<T> extends IDecoratedReadableVariable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(): void
```

ComponentV2被重用时重置Computed变量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IComputedDecoratedVariable-resetOnReuse(): void--><!--Device-IComputedDecoratedVariable-resetOnReuse(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setOwner

```TypeScript
setOwner(owner: IVariableOwner): void
```

设置状态变量的所有者，用于检测所在自定义组件是否冻结

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IComputedDecoratedVariable-setOwner(owner: IVariableOwner): void--><!--Device-IComputedDecoratedVariable-setOwner(owner: IVariableOwner): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| owner | [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md) | Yes | 状态变量的所有者 |

