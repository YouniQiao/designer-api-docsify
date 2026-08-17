# IObserve

Define IObserve interface.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface IObserve--><!--Device-unnamed-export declare interface IObserve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shouldAddRef

```TypeScript
shouldAddRef(iObjectsRenderId: RenderIdType): boolean
```

Collect the dependancy for UI component with state variable

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IObserve-shouldAddRef(iObjectsRenderId: RenderIdType): boolean--><!--Device-IObserve-shouldAddRef(iObjectsRenderId: RenderIdType): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iObjectsRenderId | [RenderIdType](arkts-na-renderidtype-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

## renderingComponent

```TypeScript
readonly renderingComponent: int
```

Rendering component.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IObserve-readonly renderingComponent: int--><!--Device-IObserve-readonly renderingComponent: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## renderingId

```TypeScript
readonly renderingId: RenderIdType
```

Rendering component id.

**Type:** [RenderIdType](arkts-na-renderidtype-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IObserve-readonly renderingId: RenderIdType--><!--Device-IObserve-readonly renderingId: RenderIdType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

