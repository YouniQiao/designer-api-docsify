# Binding

只读数据绑定的泛型类可以绑定任意类型的数据（需要与@builder参数列表同时使用）。当调用函数时，需要使用makeBinding来进行值的传递。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class Binding<T>--><!--Device-unnamed-export declare class Binding<T>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
get value(): T
```

提供get访问器以获取当前绑定值。

**Type:** T

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Binding-get value(): T--><!--Device-Binding-get value(): T-End-->

