# IDecoratedMutableVariable

定义可读写状态变量接口

**继承/实现关系：** IDecoratedMutableVariable extends IDecoratedReadableVariable<T>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## set

```TypeScript
set(newValue: T): void
```

Set the state variable with a new Value.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| newValue | T | 是 |
