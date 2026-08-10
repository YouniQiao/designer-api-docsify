# enableCompatibleObservedV2ForStatic

## enableCompatibleObservedV2ForStatic

```TypeScript
export declare function enableCompatibleObservedV2ForStatic<T>(value: T): T
```

在ArkTS-Sta中引用ArkTS-Dyn中使用@ObservedV2和@Trace修饰的类。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function enableCompatibleObservedV2ForStatic<T>(value: T): T--><!--Device-unnamed-export declare function enableCompatibleObservedV2ForStatic<T>(value: T): T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 在ArkTS-Dyn中@ObservedV2修饰的class。 |

**Return value:**

| Type | Description |
| --- | --- |
| T | 返回当前组件。 |

