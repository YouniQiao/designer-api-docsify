# wrapBuilder

## wrapBuilder

```TypeScript
declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>
```

`wrapBuilder`用于封装全局[@Builder](../arkts-apis/arkts-arkui-builder-builder-i.md/arkts-arkui-builder-builder-i.md)，可以将全局`@Builder`函数作为参数传递，实现按引用传递和动态调用，提升代码复用性。开发指南见：[wrapBuilder：封装全局@Builder](../../../ui/state-management/arkts-wrapBuilder.md)。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>--><!--Device-unnamed-declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | (...args: Args) =&gt; void | Yes | `@Builder`装饰的全局函数，传入后将被封装为`WrappedBuilder`对象。该函数必须是无返回值（`void`）的函数，其参数列表`...args`的类型和顺序 由泛型`Args`定义。当需要在组件间按引用传递或复用某个全局`@Builder`函数时传入此参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [WrappedBuilder](arkts-arkui-wrappedbuilder-c.md)&lt;Args&gt; | `WrappedBuilder&lt;Args&gt;`的实例，用于在组件之间复用或传递全局` |

