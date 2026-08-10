# FinalizationRegistryConstructor

**ArkTS模式：** 仅支持ArkTS-Dyn

## [[Construct]]

```TypeScript
new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>
```

Creates a finalization registry with an associated cleanup callback

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-FinalizationRegistryConstructor-new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>--><!--Device-FinalizationRegistryConstructor-new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cleanupCallback | (heldValue: T) =&gt; void | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| FinalizationRegistry&lt;T&gt; |  |

## prototype

```TypeScript
readonly prototype: FinalizationRegistry<any>
```

**类型：** FinalizationRegistry&lt;any&gt;

**ArkTS模式：** 仅支持ArkTS-Dyn

