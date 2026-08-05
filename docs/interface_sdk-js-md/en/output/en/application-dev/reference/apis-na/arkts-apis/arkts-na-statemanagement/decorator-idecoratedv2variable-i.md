# IDecoratedV2Variable

Define V2 decorated variable interface.

**Inheritance/Implementation:** IDecoratedV2Variable extends [IDecoratedVariable](decorator-idecoratedvariable-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface IDecoratedV2Variable<T> extends IDecoratedVariable--><!--Device-unnamed-export interface IDecoratedV2Variable<T> extends IDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(newValue: T): void
```

Reset V2 decorated variable when the ComponentV2 instance is reused.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IDecoratedV2Variable-resetOnReuse(newValue: T): void--><!--Device-IDecoratedV2Variable-resetOnReuse(newValue: T): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | T | Yes |  |

