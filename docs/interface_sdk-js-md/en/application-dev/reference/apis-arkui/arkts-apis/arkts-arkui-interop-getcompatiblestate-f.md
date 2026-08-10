# getCompatibleState

## getCompatibleState

```TypeScript
export declare function getCompatibleState<T>(state: IDecoratedV1Variable<T>): ESValue
```

为ArkTS-Sta的状态变量获取一个ArkTS-Dyn的@State代理对象，用于与ArkTS-Dyn的状态变量进行互操作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function getCompatibleState<T>(state: IDecoratedV1Variable<T>): ESValue--><!--Device-unnamed-export declare function getCompatibleState<T>(state: IDecoratedV1Variable<T>): ESValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [IDecoratedV1Variable](arkts-arkui-decorator-idecoratedv1variable-i.md)&lt;T&gt; | Yes | ArkTS-Sta的状态变量。 |

**Return value:**

| Type | Description |
| --- | --- |
| ESValue | ArkTS-Dyn的 |

