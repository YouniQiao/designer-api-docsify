# GestureGroup

手势识别组合，即两种及以上手势组合为复合手势，支持顺序识别、并发识别和互斥识别。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class GestureGroup--><!--Device-unnamed-export declare class GestureGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => GestureGroup, mode: GestureMode, ...gesture: GestureType[]): GestureGroup
```

设置组合手势事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroup-static $_instantiate(factory: () => GestureGroup, mode: GestureMode, ...gesture: GestureType[]): GestureGroup--><!--Device-GestureGroup-static $_instantiate(factory: () => GestureGroup, mode: GestureMode, ...gesture: GestureType[]): GestureGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; GestureGroup | Yes |  |
| mode | [GestureMode](arkts-arkui-gesture-gesturemode-e.md) | Yes | 设置组合手势识别模式。&lt;br/&gt;默认值：GestureMode.Sequence |
| gesture | [GestureType](arkts-arkui-gesturecontrol-gesturetype-e.md)[] | Yes | 设置一个或者多个基础手势类型时，这些手势会被识别为组合手势。 若此参数不填则组合手势识别功能不生效。&lt;br/&gt;**说明：**&lt;br/&gt;当需要为一个组件同时添加单击和双击手势时，可在组合手势中添加两个[TapGesture](arkts-arkui-gesture-con.md#tapgesture)， 需要双击手势在前，单击手势在后，否则不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureGroup](arkts-arkui-gesture-gesturegroup-c.md) |  |

## onCancel

```TypeScript
onCancel(event: VoidCallback): GestureGroup
```

手势识别成功，接收到触摸取消事件，触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureGroup-onCancel(event: VoidCallback): GestureGroup--><!--Device-GestureGroup-onCancel(event: VoidCallback): GestureGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) | Yes | 手势事件回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GestureGroup](arkts-arkui-gesture-gesturegroup-c.md) |  |

