# wrapBuilder

## wrapBuilder

```TypeScript
declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>
```

`wrapBuilder`用于封装全局@Builder，可以将全局`@Builder`函数作为参数传递，实现按引用传递和动态调用，提升代码复用性。 开发指南见：[wrapBuilder：封装全局@Builder](../../../ui/state-management/arkts-wrapBuilder.md)。

**起始版本：** 11

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>--><!--Device-unnamed-declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>-End-->

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| builder | (...args: Args) = & gt; void | 是 |

**返回值：**

| 类型 |
| --- |
| [WrappedBuilder](arkts-arkui-wrappedbuilder-c.md)&lt;Args&gt; |
