# getCompatibleState

## getCompatibleState

```TypeScript
export declare function getCompatibleState<T>(state: IDecoratedV1Variable<T>): ESValue
```

Obtains the compatible state.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function getCompatibleState<T>(state: IDecoratedV1Variable<T>): ESValue--><!--Device-unnamed-export declare function getCompatibleState<T>(state: IDecoratedV1Variable<T>): ESValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [IDecoratedV1Variable](arkts-na-decorator-idecoratedv1variable-i.md)&lt;T&gt; | Yes | the source state |

**Return value:**

| Type | Description |
| --- | --- |
| ESValue | the compatible state |

