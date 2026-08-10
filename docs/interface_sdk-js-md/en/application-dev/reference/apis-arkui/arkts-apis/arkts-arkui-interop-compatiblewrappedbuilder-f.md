# compatibleWrappedBuilder

## compatibleWrappedBuilder

```TypeScript
export declare function compatibleWrappedBuilder(builder: Any, ...args: FixedArray<ESValue>): void
```

为ArkTS-Sta提供使用ArkTS-Dyn WrappedBuilder对象的互操作方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function compatibleWrappedBuilder(builder: Any, ...args: FixedArray<ESValue>): void--><!--Device-unnamed-export declare function compatibleWrappedBuilder(builder: Any, ...args: FixedArray<ESValue>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | Any | Yes | ArkTS-Dyn WrappedBuilder对象。 |
| args | FixedArray&lt;ESValue&gt; | Yes | ArkTS-Dyn WrappedBuilder对象使用时的参数。 |

