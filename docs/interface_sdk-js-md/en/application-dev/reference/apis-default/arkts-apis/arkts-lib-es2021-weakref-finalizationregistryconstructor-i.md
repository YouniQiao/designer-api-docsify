# FinalizationRegistryConstructor

**ArkTS mode:** 

## Modules to Import

```TypeScript
```

## [[Construct]]

```TypeScript
new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>
```

Creates a finalization registry with an associated cleanup callback

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cleanupCallback | (heldValue: T) = & gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## prototype

```TypeScript
readonly prototype: FinalizationRegistry<any>
```

**Type:** [FinalizationRegistry](arkts-lib-es2021-weakref-finalizationregistry-i.md)&lt;any&gt;

**ArkTS mode:** 
