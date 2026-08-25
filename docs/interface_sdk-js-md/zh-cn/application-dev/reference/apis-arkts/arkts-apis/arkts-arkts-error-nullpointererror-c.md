# NullPointerError

表示解引用空指针时发生的错误。

**继承/实现关系：** NullPointerError extends [Error](arkts-arkts-error-c.md)

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(message?: string, options?: ErrorOptions)
```

使用给定的错误信息和错误特定信息构造一个NullPointerError实例。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| message | string | 否 |
| options | [ErrorOptions](arkts-arkts-error-erroroptions-i.md) | 否 |
