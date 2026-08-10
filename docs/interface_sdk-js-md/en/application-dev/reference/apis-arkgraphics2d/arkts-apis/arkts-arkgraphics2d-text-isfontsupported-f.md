# isFontSupported

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## isFontSupported

```TypeScript
function isFontSupported(fontURL: string | Resource): boolean
```

检查系统是否支持指定的字体文件。可在加载自定义字体前预先验证字体文件的可用性，避免因字体不支持导致文本渲染异常。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-text-function isFontSupported(fontURL: string | Resource): boolean--><!--Device-text-function isFontSupported(fontURL: string | Resource): boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fontURL | string \| Resource | Yes | 需要检查的字体文件的路径，应为 "file:// + 字体文件绝对路径" 或 "rawfile/目录or文件名"。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 系统是否支持指定的字体文件。返回true表示支持，返回false表示不支持。 |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct isFontSupportedTest {
  build() {
    Column({ space: 10 }) {
      Button("is font supported")
        .onClick(() => {
          let filePath = "file:///system/fonts/NotoSansCJK-Regular.ttc"
          let isSupported = text.isFontSupported(filePath)
          console.info("is font supported: " + isSupported)
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

