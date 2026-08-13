# FinalizationRegistryConstructor

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-interface FinalizationRegistryConstructor--><!--Device-unnamed-interface FinalizationRegistryConstructor-End-->

## constructor

```TypeScript
new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>
```

Creates a finalization registry with an associated cleanup callback

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-FinalizationRegistryConstructor-new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>--><!--Device-FinalizationRegistryConstructor-new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cleanupCallback | (heldValue: T) =&gt; void | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [FinalizationRegistry](arkts-na-lib-es2021-weakref-finalizationregistry-i.md)&lt;T&gt; |  |

## prototype

```TypeScript
readonly prototype: FinalizationRegistry<any>
```

**Type:** [FinalizationRegistry](arkts-na-lib-es2021-weakref-finalizationregistry-i.md)&lt;any&gt;

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-FinalizationRegistryConstructor-readonly prototype: FinalizationRegistry<any>--><!--Device-FinalizationRegistryConstructor-readonly prototype: FinalizationRegistry<any>-End-->

