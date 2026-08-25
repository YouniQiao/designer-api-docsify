# IConsumeDecoratedVariable

Define Consume decoration variable interface.

**继承/实现关系：** IConsumeDecoratedVariable extends IDecoratedMutableVariable<T>, IDecoratedV1Variable<T>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(provideAlias: string, watchFunc?: WatchFuncType, consumeOptions?: ConsumeOptions<T>): void
```

当@Reusable Component实例被重用时，重置Consume变量。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| provideAlias | string | 是 |
| watchFunc | [WatchFuncType](arkts-arkui-watchfunctype-t.md) | 否 |
| consumeOptions | [ConsumeOptions](arkts-arkui-decorator-consumeoptions-i.md)&lt;T&gt; | 否 |
