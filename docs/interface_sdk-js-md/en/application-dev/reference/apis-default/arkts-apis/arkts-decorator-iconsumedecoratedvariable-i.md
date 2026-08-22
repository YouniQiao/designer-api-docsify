# IConsumeDecoratedVariable

Define Consume decoration variable interface.

**Inheritance/Implementation:** IConsumeDecoratedVariable extends IDecoratedMutableVariable<T>, IDecoratedV1Variable<T>

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface IConsumeDecoratedVariable--><!--Device-unnamed-export declare interface IConsumeDecoratedVariable-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): void
```

Reset Consume variable when the @Reusable Component instance is reused.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IConsumeDecoratedVariable-resetOnReuse(provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): void--><!--Device-IConsumeDecoratedVariable-resetOnReuse(provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| provideAlias | string | Yes | alias |
| watchFunc | [WatchFuncType](arkts-watchfunctype-t.md) | No | watch function type |
| consumeOptions | [ConsumeOptions](arkts-decorator-consumeoptions-i.md)&lt;T&gt; | No | options with default value |

