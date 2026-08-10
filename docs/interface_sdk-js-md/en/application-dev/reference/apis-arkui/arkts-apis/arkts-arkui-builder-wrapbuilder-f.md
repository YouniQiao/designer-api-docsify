# wrapBuilder

## wrapBuilder

```TypeScript
export declare function wrapBuilder<T>(builder: T): WrappedBuilder<T>
```

wrapBuilder是一个模板函数，返回一个`WrappedBuilder`对象。模板参数`T`是@Builder的函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function wrapBuilder<T>(builder: T): WrappedBuilder<T>--><!--Device-unnamed-export declare function wrapBuilder<T>(builder: T): WrappedBuilder<T>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | T | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [WrappedBuilder](../arkts-components/arkts-arkui-wrappedbuilder-c.md)&lt;T&gt; | WrappedBuilder对象。 |

