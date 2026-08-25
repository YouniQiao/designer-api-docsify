# ErrorHandler

```TypeScript
export type ErrorHandler = (errObject: Error) => void
```

当ArkTS运行时抛出用户未捕获异常时，将调用ErrorHandler。

**起始版本：** 21

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| errObject | Error | 是 |
