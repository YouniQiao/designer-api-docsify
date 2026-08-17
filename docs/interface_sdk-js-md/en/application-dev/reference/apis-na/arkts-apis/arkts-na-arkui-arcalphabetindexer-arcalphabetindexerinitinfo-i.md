# ArcAlphabetIndexerInitInfo

Define the initialization parameters of the arc alphabet index bar

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface ArcAlphabetIndexerInitInfo--><!--Device-unnamed-export declare interface ArcAlphabetIndexerInitInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## arrayValue

```TypeScript
arrayValue: string[]
```

Array of alphabetic indexed strings, cannot be set to empty.

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerInitInfo-arrayValue: string[]--><!--Device-ArcAlphabetIndexerInitInfo-arrayValue: string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## selected

```TypeScript
selected: int | Bindable<int>
```

The index value of the initial selected item.If it is out of the index range, the default value is 0

**Type:** int \| [Bindable](arkts-na-common-bindable-i.md)&lt;int&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerInitInfo-selected: int | Bindable<int>--><!--Device-ArcAlphabetIndexerInitInfo-selected: int | Bindable<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

