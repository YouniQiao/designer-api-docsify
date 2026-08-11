# MenuAlignParams

Sets the alignment between the drop-down list button and the drop-down list box.

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

Alignment type. Default value: **MenuAlignType.START**

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

Offset of the drop-down list box relative to the drop-down list button after alignment based on the alignment type.Default value: **{dx: 0, dy: 0}**

**Type:** [Offset](arkts-arkui-componentutils-offset-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MenuAlignParams-offset?: Offset--><!--Device-MenuAlignParams-offset?: Offset-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

