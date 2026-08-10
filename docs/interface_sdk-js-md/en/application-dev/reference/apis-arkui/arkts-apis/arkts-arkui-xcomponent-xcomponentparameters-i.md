# XComponentParameters

定义XComponent的具体配置参数，支持Native侧触发XComponent生命周期回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface XComponentParameters--><!--Device-unnamed-export declare interface XComponentParameters-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: XComponentController
```

给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。

**Type:** [XComponentController](arkts-arkui-xcomponent-xcomponentcontroller-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentParameters-controller?: XComponentController--><!--Device-XComponentParameters-controller?: XComponentController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: string
```

组件的唯一标识，支持最大的字符串长度128。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentParameters-id: string--><!--Device-XComponentParameters-id: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## nativeXComponentHandler

```TypeScript
nativeXComponentHandler: Callback<NativeXComponentPointer>
```

用于处理NativeXComponent实例的回调。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;NativeXComponentPointer&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentParameters-nativeXComponentHandler: Callback<NativeXComponentPointer>--><!--Device-XComponentParameters-nativeXComponentHandler: Callback<NativeXComponentPointer>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: XComponentType
```

用于指定XComponent组件类型。

**Type:** [XComponentType](arkts-arkui-xcomponenttype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentParameters-type: XComponentType--><!--Device-XComponentParameters-type: XComponentType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

