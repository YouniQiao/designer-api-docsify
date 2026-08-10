# mutableBuilder

## mutableBuilder

```TypeScript
declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>
```

`mutableBuilder`是一个泛型函数，它返回一个`MutableBuilder`对象，只接受一个全局的`@Builder`函数作为其参数。

`mutableBuilder`函数返回的[MutableBuilder](arkts-arkui-mutablebuilder-c.md)对象，其`builder`属性方法只能在自定义组件的`build`函数或`@Builder`装饰的函数内部被调用。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>--><!--Device-unnamed-declare function mutableBuilder<Args extends Object[]>(builder: BuilderCallback): MutableBuilder<Args>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | [BuilderCallback](arkts-arkui-buildercallback-t.md) | Yes | `@Builder`装饰的全局函数，作为`mutableBuilder`封装的目标构建函数。该函数需符合`BuilderCallback`类型，即 `(...args: Args) => void`，是一个无返回值的函数，其参数列表`...args`的类型由泛型`Args`指定。 |

**Return value:**

| Type | Description |
| --- | --- |
| [MutableBuilder](arkts-arkui-mutablebuilder-c.md)&lt;Args&gt; | `MutableBuilder&lt;Args&gt;`的实例，用于封装全局` |

