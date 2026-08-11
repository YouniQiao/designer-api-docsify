# IConsumeDecoratedVariable

Define Consume decoration variable interface.

**Inheritance/Implementation:** IConsumeDecoratedVariable extends [IDecoratedMutableVariable<T>](IDecoratedMutableVariable<T>), [IDecoratedV1Variable<T>](IDecoratedV1Variable<T>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IConsumeDecoratedVariable<T> extends IDecoratedMutableVariable<T>, IDecoratedV1Variable<T>--><!--Device-unnamed-export declare interface IConsumeDecoratedVariable<T> extends IDecoratedMutableVariable<T>, IDecoratedV1Variable<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): void
```

Reset Consume variable when the @Reusable Component instance is reused.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IConsumeDecoratedVariable-resetOnReuse(provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): void--><!--Device-IConsumeDecoratedVariable-resetOnReuse(provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| provideAlias | string | Yes | alias |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | No | watch function type |
| consumeOptions | [ConsumeOptions](arkts-arkui-decorator-consumeoptions-i.md)&lt;T&gt; | No | options with default value |

