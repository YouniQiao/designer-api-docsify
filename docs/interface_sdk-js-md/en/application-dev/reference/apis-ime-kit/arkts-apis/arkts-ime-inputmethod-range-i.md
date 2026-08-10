# Range

文本的选中范围。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-inputMethod-export interface Range--><!--Device-inputMethod-export interface Range-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## end

```TypeScript
end: int
```

选中文本的末字符在编辑框的索引值。该参数应为大于或等于0的整数，不超过文本实际长度，end值要大于start值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Range-end: int--><!--Device-Range-end: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## start

```TypeScript
start: int
```

选中文本的首字符在编辑框的索引值。该参数应为大于或等于0的整数，不超过文本实际长度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-Range-start: int--><!--Device-Range-start: int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

