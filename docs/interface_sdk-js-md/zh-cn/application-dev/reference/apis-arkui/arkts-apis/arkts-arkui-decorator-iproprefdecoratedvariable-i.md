# IPropRefDecoratedVariable

Define PropRef decoration variable interface.

**继承/实现关系：** IPropRefDecoratedVariable extends IDecoratedMutableVariable<T>, IDecoratedUpdatableVariable<T>, IDecoratedV1Variable<T>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## resetOnReuse

```TypeScript
resetOnReuse(newValue: T): void
```

当组件被复用时，重置状态变量。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newValue | T | 是 |
