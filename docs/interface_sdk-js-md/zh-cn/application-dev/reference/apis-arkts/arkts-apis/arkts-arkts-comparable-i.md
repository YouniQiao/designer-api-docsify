# Comparable

可由任何支持比较的类型实现。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## compareTo

```TypeScript
compareTo(to: T): int
```

将当前实例与另一个按`T`处理的对象进行比较。如果当前实例小于给定对象，则结果小于0； 如果两者相等，则结果为0；否则结果大于0。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| to | T | 是 |

**返回值：**

| 类型 |
| --- |
| int |
