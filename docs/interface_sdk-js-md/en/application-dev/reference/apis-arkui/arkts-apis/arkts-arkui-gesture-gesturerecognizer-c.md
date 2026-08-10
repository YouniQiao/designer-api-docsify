# GestureRecognizer

手势识别器对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class GestureRecognizer--><!--Device-unnamed-export declare class GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getEventTargetInfo

```TypeScript
getEventTargetInfo(): EventTargetInfo
```

返回当前手势识别器对应组件的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getEventTargetInfo(): EventTargetInfo--><!--Device-GestureRecognizer-getEventTargetInfo(): EventTargetInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [EventTargetInfo](arkts-arkui-eventtargetinfo-c.md) | 当前手势识别器对应组件的信息。 |

## getFingerCount

```TypeScript
getFingerCount(): int
```

返回预设手指识别数阈值。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getFingerCount(): int--><!--Device-GestureRecognizer-getFingerCount(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| int | 预设手指识别数阈值。&lt;br/&gt;取值范围：[1, 10], 整数。 |

## getState

```TypeScript
getState(): GestureRecognizerState
```

返回当前手势识别器的状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getState(): GestureRecognizerState--><!--Device-GestureRecognizer-getState(): GestureRecognizerState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [GestureRecognizerState](arkts-arkui-gesturerecognizerstate-e.md) | 当前手势识别器的状态。 |

## getTag

```TypeScript
getTag(): string
```

返回当前手势识别器的tag。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getTag(): string--><!--Device-GestureRecognizer-getTag(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | 当前手势识别器的标志。 |

## getType

```TypeScript
getType(): GestureControl.GestureType
```

返回当前手势识别器的类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-getType(): GestureControl.GestureType--><!--Device-GestureRecognizer-getType(): GestureControl.GestureType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| GestureControl.GestureType | 当前手势识别器的类型。 |

## isBuiltIn

```TypeScript
isBuiltIn(): boolean
```

返回当前手势识别器是否为系统内置手势。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isBuiltIn(): boolean--><!--Device-GestureRecognizer-isBuiltIn(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前手势识别器是否为系统内置手势。true表示手势识别器为系统内置手势，false表示非系统内置手势。 |

## isEnabled

```TypeScript
isEnabled(): boolean
```

返回当前手势识别器的使能状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isEnabled(): boolean--><!--Device-GestureRecognizer-isEnabled(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前手势识别器的使能状态。true表示当前手势识别器能够回调应用事件，false表示当前手势识别器不回调应用事件。 |

## isFingerCountLimit

```TypeScript
isFingerCountLimit(): boolean
```

返回预设手势是否会检测触摸屏幕上手指识别数量。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isFingerCountLimit(): boolean--><!--Device-GestureRecognizer-isFingerCountLimit(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 预设手势是否会检测触摸屏幕上手指识别数量。当绑定手势事件且会检测触摸屏幕上手指的数量时，返回true。当绑定手势事件且不会检测触摸屏幕上手指的数量时，返回false。 |

## isHostBelongsTo

```TypeScript
isHostBelongsTo(uniqueId: int): boolean
```

返回当前手势识别器绑定节点是否为传入组件的后代节点。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isHostBelongsTo(uniqueId: int): boolean--><!--Device-GestureRecognizer-isHostBelongsTo(uniqueId: int): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uniqueId | int | Yes | 组件的唯一ID。可以通过[getUniqueId](arkts-arkui-eventtargetinfo-c.md#getuniqueid)接口获取该ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前手势识别器绑定节点是否为传入组件的后代节点。true表示当前绑定节点为传入组件的后代节点，false表示当前绑定节点非传入组件的后代节点。 |

## isValid

```TypeScript
isValid(): boolean
```

返回当前手势识别器是否有效。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-isValid(): boolean--><!--Device-GestureRecognizer-isValid(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 当前手势识别器是否有效。&lt;br/&gt;当该识别器绑定的组件被析构或该识别器不在响应链上时返回false。&lt;br/&gt;当该识别器绑定的组件未被析构且该识别器在响应链上时返回true。 |

## preventBegin

```TypeScript
preventBegin(): void
```

在手指全部抬起前阻止手势识别器参与当前手势识别。如果系统已确定该手势识别器的结果（无论成功与否），调用此接口将无效。此方法与GestureRecognizer.[setEnabled](arkts-arkui-gesturerecognizer-c.md#setenabled)(isEnabled: boolean)不同，  
[setEnabled](arkts-arkui-gesturerecognizer-c.md#setenabled)并不会阻止手势识别器对象参与手势识别过程，而只会影响手势对应的回调函数是否执行。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-preventBegin(): void--><!--Device-GestureRecognizer-preventBegin(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setEnabled

```TypeScript
setEnabled(isEnabled: boolean): void
```

设置当前手势识别器的使能状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureRecognizer-setEnabled(isEnabled: boolean): void--><!--Device-GestureRecognizer-setEnabled(isEnabled: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean | Yes | 手势识别器的使能状态。true表示当前手势识别器能够回调应用事件，false表示当前手势识别器不回调应用事件。 |

