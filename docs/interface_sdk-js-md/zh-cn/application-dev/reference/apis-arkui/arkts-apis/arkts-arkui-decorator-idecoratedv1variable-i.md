# IDecoratedV1Variable

Define V1 decorated variable interface.

**继承/实现关系：** IDecoratedV1Variable extends [IDecoratedVariable](arkts-arkui-decorator-idecoratedvariable-i.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## registerWatchToSource

```TypeScript
registerWatchToSource(decoratedVar: IDecoratedV1Variable<T>): void
```

Registers the watch callback function with the data source.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| decoratedVar | [IDecoratedV1Variable](arkts-arkui-decorator-idecoratedv1variable-i.md)&lt;T&gt; | 是 |
