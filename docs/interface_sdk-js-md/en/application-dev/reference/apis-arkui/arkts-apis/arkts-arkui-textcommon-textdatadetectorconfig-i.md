# TextDataDetectorConfig

文本识别配置项。该配置只支持[Text](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md)组件和  
[RichEditor](../../../reference/apis-arkui/arkui-ts/ts-basic-components-richeditor.md)组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextDataDetectorConfig--><!--Device-unnamed-export declare interface TextDataDetectorConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

设置文本识别成功后的实体颜色。

默认值：'#ff0a59f7'

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextDataDetectorConfig-color?: ResourceColor--><!--Device-TextDataDetectorConfig-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoration

```TypeScript
decoration?: DecorationStyleInterface
```

设置文本识别成功后的实体装饰线样式。

默认值：

{

 type: TextDecorationType.Underline,

 color: 与实体颜色一致,

 style: TextDecorationStyle.SOLID

}

**Type:** [DecorationStyleInterface](arkts-arkui-decorationstyleinterface-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextDataDetectorConfig-decoration?: DecorationStyleInterface--><!--Device-TextDataDetectorConfig-decoration?: DecorationStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enablePreviewMenu

```TypeScript
enablePreviewMenu?: boolean
```

设置是否开启文本识别长按显示预览菜单。true表示开启，false表示未开启。

默认值：false

当[copyOptions](../../../reference/apis-arkui/arkui-ts/ts-basic-components-richeditor.md#copyoptions)设置为None时，若enablePreviewMenu设置为true，长按AI实体也不能显示预览菜单。

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextDataDetectorConfig-enablePreviewMenu?: boolean--><!--Device-TextDataDetectorConfig-enablePreviewMenu?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDetectResultUpdate

```TypeScript
onDetectResultUpdate?: Callback<string>
```

文本识别成功后，触发onDetectResultUpdate回调。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextDataDetectorConfig-onDetectResultUpdate?: Callback<string>--><!--Device-TextDataDetectorConfig-onDetectResultUpdate?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## types

```TypeScript
types: TextDataDetectorType[] | undefined | null
```

设置文本识别的实体类型。设置types为null或者undefined或者[]时，识别所有类型的实体，否则只识别指定类型的实体。

**Type:** TextDataDetectorType[] \| undefined \| null

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextDataDetectorConfig-types: TextDataDetectorType[] | undefined | null--><!--Device-TextDataDetectorConfig-types: TextDataDetectorType[] | undefined | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

