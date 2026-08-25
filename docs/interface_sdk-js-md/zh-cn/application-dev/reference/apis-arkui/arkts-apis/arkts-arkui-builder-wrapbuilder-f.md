# wrapBuilder

## wrapBuilder

```TypeScript
export declare function wrapBuilder<T>(builder: T): WrappedBuilder<T>
```

wrapBuilder是一个模板函数，返回一个`WrappedBuilder`对象。模板参数`T`是@Builder的函数类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | T | 是 |

**返回值：**

| 类型 |
| --- |
| [WrappedBuilder](arkts-arkui-builder-wrappedbuilder-c.md)&lt;T&gt; |
