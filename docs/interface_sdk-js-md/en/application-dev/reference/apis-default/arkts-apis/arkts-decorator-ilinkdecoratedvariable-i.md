# ILinkDecoratedVariable

Define Link decoration variable interface.

**Inheritance/Implementation:** ILinkDecoratedVariable extends IDecoratedMutableVariable<T>, IDecoratedV1Variable<T>

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface ILinkDecoratedVariable--><!--Device-unnamed-export declare interface ILinkDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(newValue: LinkSourceType<T>): void
```

Reset Link variable when the @Reusable Component instance is reused.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ILinkDecoratedVariable-resetOnReuse(newValue: LinkSourceType<T>): void--><!--Device-ILinkDecoratedVariable-resetOnReuse(newValue: LinkSourceType<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newValue | [LinkSourceType](arkts-linksourcetype-t.md)&lt;T&gt; | Yes | default value |

