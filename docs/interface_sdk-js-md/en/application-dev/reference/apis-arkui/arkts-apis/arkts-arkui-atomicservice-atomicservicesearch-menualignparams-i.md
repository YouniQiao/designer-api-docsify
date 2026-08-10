# MenuAlignParams

下拉按钮与下拉菜单间的对齐方式设置项。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-export interface MenuAlignParams--><!--Device-unnamed-export interface MenuAlignParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SearchParams, AtomicServiceSearch, SearchButtonParams, OperationParams, SelectParams, InputFilterParams, MenuAlignParams } from 'kits/@kit.ArkUI';
```

## alignType

```TypeScript
alignType: MenuAlignType
```

对齐方式类型。默认值：`MenuAlignType.START`。

**Type:** [MenuAlignType](arkts-arkui-select-menualigntype-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MenuAlignParams-alignType: MenuAlignType--><!--Device-MenuAlignParams-alignType: MenuAlignType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: Offset
```

按照对齐类型对齐后，下拉菜单相对下拉按钮的偏移量。默认值：`{dx: 0, dy: 0}`。

**Type:** [Offset](arkts-arkui-componentutils-offset-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MenuAlignParams-offset?: Offset--><!--Device-MenuAlignParams-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

