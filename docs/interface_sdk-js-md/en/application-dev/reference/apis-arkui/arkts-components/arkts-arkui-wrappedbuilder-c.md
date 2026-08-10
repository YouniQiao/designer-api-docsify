# WrappedBuilder

`WrappedBuilder`是`@Builder`函数的包装类，用于封装全局`@Builder`函数及其参数，实现按引用传递和动态调用。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare class WrappedBuilder<Args extends Object[]>--><!--Device-unnamed-declare class WrappedBuilder<Args extends Object[]>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder: (...args: Args) => void
```

`@Builder`装饰的全局函数，用于生成对应的自定义构建内容。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WrappedBuilder-builder: (...args: Args) => void--><!--Device-WrappedBuilder-builder: (...args: Args) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| args | Args | Yes |  |

## constructor

```TypeScript
constructor(builder: (...args: Args) => void)
```

`WrappedBuilder`的构造函数。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WrappedBuilder-constructor(builder: (...args: Args) => void)--><!--Device-WrappedBuilder-constructor(builder: (...args: Args) => void)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | (...args: Args) =&gt; void | Yes | `@Builder`装饰的全局函数，作为构造参数用于初始化`WrappedBuilder`实例。函数参数`args`为该`@Builder`函数所需的参数列表。 |

