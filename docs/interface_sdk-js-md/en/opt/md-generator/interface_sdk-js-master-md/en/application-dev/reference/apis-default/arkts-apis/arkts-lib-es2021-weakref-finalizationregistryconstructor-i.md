# FinalizationRegistryConstructor

## [[Construct]]

```TypeScript
new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>
```

Creates a finalization registry with an associated cleanup callback

<!--Device-FinalizationRegistryConstructor-new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>--><!--Device-FinalizationRegistryConstructor-new<T>(cleanupCallback: (heldValue: T) => void): FinalizationRegistry<T>-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cleanupCallback | (heldValue: T) =&gt; void | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| FinalizationRegistry&lt;T&gt; |

## prototype

```TypeScript
readonly prototype: FinalizationRegistry<any>
```

**Type:** FinalizationRegistry&lt;any&gt;
