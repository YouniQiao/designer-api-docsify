# FontVariation

可变字体属性。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-interface FontVariation--><!--Device-text-interface FontVariation-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## axis

```TypeScript
axis: string
```

可变字体属性键值对中的关键字标识，如'wght'（字重）、'wdth'（字宽）和'ital'（斜体）等。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontVariation-axis: string--><!--Device-FontVariation-axis: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## isNormalized

```TypeScript
isNormalized?: boolean
```

是否归一化。值为true时，value字段取值范围为-1~1，映射字体文件中配置的最小值到最大值范围，0表示字体文件中配置的默认值；值为false时，value字段取值范围为字体文件本身支持调节的范围；默认为false。

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-FontVariation-isNormalized?: boolean--><!--Device-FontVariation-isNormalized?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## value

```TypeScript
value: double
```

可变字体属性键值对的值。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontVariation-value: double--><!--Device-FontVariation-value: double-End-->

**System capability:** SystemCapability.Graphics.Drawing

