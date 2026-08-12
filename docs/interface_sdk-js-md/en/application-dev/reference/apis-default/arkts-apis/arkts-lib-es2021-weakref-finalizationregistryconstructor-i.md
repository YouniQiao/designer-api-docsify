# FinalizationRegistryConstructor

**ArkTS mode:** ArkTS-Dyn only

## [[Construct]]

```TypeScript
new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>
```

Creates a finalization registry with an associated cleanup callback

**ArkTS mode:** ArkTS-Dyn only

<!--Device-FinalizationRegistryConstructor-new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>--><!--Device-FinalizationRegistryConstructor-new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cleanupCallback | (heldValue: T) =&gt; void | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [FinalizationRegistry](arkts-lib-es2021-weakref-finalizationregistry-i.md)&lt;T&gt; |  |

## prototype

```TypeScript
readonly prototype: FinalizationRegistry<any>
```

**Type:** [FinalizationRegistry](arkts-lib-es2021-weakref-finalizationregistry-i.md)&lt;any&gt;

**ArkTS mode:** ArkTS-Dyn only

