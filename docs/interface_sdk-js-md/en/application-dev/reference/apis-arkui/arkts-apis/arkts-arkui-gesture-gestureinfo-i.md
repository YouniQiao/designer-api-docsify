# GestureInfo

手势信息类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface GestureInfo--><!--Device-unnamed-export declare interface GestureInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSystemGesture

```TypeScript
isSystemGesture: boolean
```

当前手势是否为组件自带手势。true表示是，false表示否。

默认值：false

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureInfo-isSystemGesture: boolean--><!--Device-GestureInfo-isSystemGesture: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tag

```TypeScript
tag?: string
```

手势标志。

**说明：**

未设置事件标志tag属性时，tag不返回或返回undefined。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureInfo-tag?: string--><!--Device-GestureInfo-tag?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: GestureControl.GestureType
```

手势类型。

**说明：**

当手势为未暴露类型的系统内置手势事件时，type的值为-1。

**Type:** GestureControl.GestureType

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureInfo-type: GestureControl.GestureType--><!--Device-GestureInfo-type: GestureControl.GestureType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

