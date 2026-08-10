# ArcAlphabetIndexerInitInfo

定义弧形字母索引条的初始化参数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface ArcAlphabetIndexerInitInfo--><!--Device-unnamed-export declare interface ArcAlphabetIndexerInitInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## Modules to Import

```TypeScript
import { ArcAlphabetIndexerAttribute, ArcAlphabetIndexer } from 'kits/@kit.ArkUI';
```

## arrayValue

```TypeScript
arrayValue: string[]
```

字母索引字符串数组，不可设置为空。

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerInitInfo-arrayValue: string[]--><!--Device-ArcAlphabetIndexerInitInfo-arrayValue: string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

## selected

```TypeScript
selected: int | Bindable<int>
```

初始选中项索引值，若超出索引值范围，则取默认值0。

该参数支持[!!](../../../ui/state-management/arkts-new-binding.md)双向绑定变量。

**Type:** int \| Bindable&lt;int&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ArcAlphabetIndexerInitInfo-selected: int | Bindable<int>--><!--Device-ArcAlphabetIndexerInitInfo-selected: int | Bindable<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

