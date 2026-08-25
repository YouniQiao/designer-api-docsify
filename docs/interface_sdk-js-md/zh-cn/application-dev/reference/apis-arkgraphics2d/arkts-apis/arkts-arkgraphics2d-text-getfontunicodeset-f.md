# getFontUnicodeSet

## 导入模块

```TypeScript
import { text } from '@kit.ArkGraphics2D';
```

## getFontUnicodeSet

```TypeScript
function getFontUnicodeSet(path: string | Resource, index: int) : Promise<Array<int>>
```

根据字体文件路径获取字体unicode数组。使用Promise异步回调。如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回空数组。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| index | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;Array & lt;number & gt; & gt;<br>ArkTS-Sta：Promise & lt;Array & lt;int & gt; & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct GetFontUnicodeSetTest {
  build() {
    Column({ space: 10 }) {
      Button("get fontUnicode")
        .onClick(() => {
          let promise = text.getFontUnicodeSet("file:///system/fonts/HMSymbolVF.ttf", 0)
          promise.then((unicodeSet) => {
            for (let index = 0; index < unicodeSet.length; index++) {
              console.info(unicodeSet[index].toString())
            }
          })
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

ArkTS-Sta示例：

```TypeScript
import {Entry, Component, Column, Button} from '@ohos.arkui.component'
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct GetFontUnicodeSetTest {
  build() {
    Column() {
      Button("get fontUnicode").onClick(() => {
        text.getFontUnicodeSet("file:///system/fonts/HMSymbolVF.ttf", 0).then((unicodeSet:Array<int>) => {
          for (let index = 0; index < unicodeSet.length; index++) {
            console.info(unicodeSet[index].toString())
          }
        }).catch((error: Error) => {
          console.error(`Failed to get font unicode, error: ${JSON.stringify(error)}`)
        });
      })
    }
  }
}
```
