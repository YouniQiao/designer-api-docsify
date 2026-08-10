# transferCompatibleBuilder

## transferCompatibleBuilder

```TypeScript
export declare function transferCompatibleBuilder<T extends Function>(@Builder builder: T): ESValue
```

在ArkTS-Sta中给ArkTS-Dyn的@BuilderParam传递@Builder函数（适用于非字面量更新场景）。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function transferCompatibleBuilder<T extends Function>(@Builder builder: T): ESValue--><!--Device-unnamed-export declare function transferCompatibleBuilder<T extends Function>(@Builder builder: T): ESValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| builder | T | Yes | 自定义构建函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| ESValue | 可互操作的自定义构建函数。 |

