# CollectionType

```TypeScript
export declare type CollectionType<S> = Array<S> | Map<string | number, S> |
  Set<S> | collections.Array<S> | collections.Map<string | number, S> | collections.Set<S>
```

globalConnect的入参泛型，用于定义globalConnect支持的持久化集合数据类型。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export declare type CollectionType<S> = Array<S> | Map<string | number, S> |  Set<S> | collections.Array<S> | collections.Map<string | number, S> | collections.Set<S>--><!--Device-unnamed-export declare type CollectionType<S> = Array<S> | Map<string | number, S> |  Set<S> | collections.Array<S> | collections.Map<string | number, S> | collections.Set<S>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| --- | --- |
| Array&lt;S&gt; | 表示值类型为Array类型。 |
| Map&lt;string |  |
| number, S&gt; |  |
| Set&lt;S&gt; | 表示值类型为Set类型。 |
| collections.Array&lt;S&gt; | 表示值类型为collections.Array类型。 |
| collections.Map&lt;string |  |
| number, S&gt; |  |
| collections.Set&lt;S&gt; | 表示值类型为collections.Set类型。 |

