# GestureGroup

Defines the GestureGroup.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare class GestureGroup--><!--Device-unnamed-export declare class GestureGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => GestureGroup, mode: GestureMode, ...gesture: GestureType[]): GestureGroup
```

Return to Obtain GestureGroup.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroup-static $_instantiate(factory: () => GestureGroup, mode: GestureMode, ...gesture: GestureType[]): GestureGroup--><!--Device-GestureGroup-static $_instantiate(factory: () => GestureGroup, mode: GestureMode, ...gesture: GestureType[]): GestureGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; GestureGroup | Yes |  |
| mode | [GestureMode](arkts-arkui-gesture-gesturemode-e.md) | Yes |  |
| gesture | [GestureType](arkts-arkui-gesturetype-t.md)[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureGroup](arkts-arkui-gesture-gesturegroup-c.md) |  |

## onCancel

```TypeScript
onCancel(event: VoidCallback): GestureGroup
```

The Gesture group is successfully recognized and a callback is triggered when the touch cancel event is received.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroup-onCancel(event: VoidCallback): GestureGroup--><!--Device-GestureGroup-onCancel(event: VoidCallback): GestureGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureGroup](arkts-arkui-gesture-gesturegroup-c.md) |  |

