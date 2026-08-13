# CollectionType

```TypeScript
export declare type CollectionType<S> = Array<S> | Map<string | number, S> |
  Set<S> | collections.Array<S> | collections.Map<string | number, S> | collections.Set<S>
```

Defines the types of persistent collection data supported by **globalConnect** using the generic type of the input parameter of **globalConnect**.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export declare type CollectionType<S> = Array<S> | Map<string | number, S> |  Set<S> | collections.Array<S> | collections.Map<string | number, S> | collections.Set<S>--><!--Device-unnamed-export declare type CollectionType<S> = Array<S> | Map<string | number, S> |  Set<S> | collections.Array<S> | collections.Map<string | number, S> | collections.Set<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;S & gt; |
| Map & lt;string |
| number, S & gt; |
| Set & lt;S & gt; |
| collections.Array & lt;S & gt; |
| collections.Map & lt;string |
| number, S & gt; |
| collections.Set & lt;S & gt; |
