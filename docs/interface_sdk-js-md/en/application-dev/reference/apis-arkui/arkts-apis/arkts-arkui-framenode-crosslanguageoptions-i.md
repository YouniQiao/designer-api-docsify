# CrossLanguageOptions

该接口用于配置或查询FrameNode的跨语言访问权限。例如，针对ArkTS语言创建的节点，可通过该接口控制是否允许通过非ArkTS语言进行属性访问或修改。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface CrossLanguageOptions--><!--Device-unnamed-export declare interface CrossLanguageOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeSetting

```TypeScript
attributeSetting?: boolean
```

FrameNode是否支持跨ArkTS语言进行属性设置。true表示支持跨ArkTS语言进行属性设置，false表示不支持跨ArkTS语言进行属性设置。默认值为false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CrossLanguageOptions-attributeSetting?: boolean--><!--Device-CrossLanguageOptions-attributeSetting?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## treeOperating

```TypeScript
treeOperating?: boolean
```

FrameNode是否支持跨ArkTS语言进行组件树操作。true表示支持跨ArkTS语言进行组件树操作，false表示不支持跨ArkTS语言进行组件树操作。默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CrossLanguageOptions-treeOperating?: boolean--><!--Device-CrossLanguageOptions-treeOperating?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

