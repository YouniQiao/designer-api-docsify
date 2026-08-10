# ParameterDecorator

```TypeScript
declare type ParameterDecorator = (target: Object, propertyKey: string | symbol, parameterIndex: number) => void
```

**ArkTS模式：** 仅支持ArkTS-Dyn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | Object | 是 |  |
| propertyKey | string \| symbol | 是 |  |
| parameterIndex | number | 是 |  |

