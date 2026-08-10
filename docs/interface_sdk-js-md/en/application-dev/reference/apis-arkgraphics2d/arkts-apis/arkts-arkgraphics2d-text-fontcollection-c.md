# FontCollection

字体集，用于管理文本排版所需的字体资源。FontCollection为[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md)提供字体匹配和字形查找能力，是文本排版管线的基础组件。提供全局实例（[getGlobalInstance](arkts-arkgraphics2d-text-fontcollection-c.md#getglobalinstance)）和本地实例（  
[getLocalInstance](arkts-arkgraphics2d-text-fontcollection-c.md#getlocalinstance)），全局实例加载的字体在应用内共享，适用于普通应用场景；本地实例各实例独立，加载的字体仅对当前实例生效、实例间互不影响，推荐卡片场景使用。支持通过[loadFontSync](arkts-arkgraphics2d-text-fontcollection-c.md#loadfontsync)或  
[loadFont](arkts-arkgraphics2d-text-fontcollection-c.md#loadfont)加载自定义字体。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-text-class FontCollection--><!--Device-text-class FontCollection-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## clearCaches

```TypeScript
clearCaches(): void
```

清理字体排版缓存。字体排版缓存本身设有内存上限和自动清理机制，所占内存有限。如无特殊内存要求，不建议清理。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-FontCollection-clearCaches(): void--><!--Device-FontCollection-clearCaches(): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button().onClick(() => {
        text.FontCollection.getGlobalInstance().clearCaches();
      })
    }
  }
}
```

## getGlobalInstance

```TypeScript
static getGlobalInstance(): FontCollection
```

获取应用全局FontCollection实例。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontCollection-static getGlobalInstance(): FontCollection--><!--Device-FontCollection-static getGlobalInstance(): FontCollection-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) | 应用全局FontCollection实例对象，可用于管理字体加载、卸载和排版等操作。 |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

function textFunc() {
  let fontCollection = text.FontCollection.getGlobalInstance();
}

@Entry
@Component
struct Index {
  fun: Function = textFunc;
  build() {
    Column() {
      Button().onClick(() => {
        this.fun();
      })
    }
  }
}
```

## getLocalInstance

```TypeScript
static getLocalInstance(): FontCollection
```

获取本地FontCollection实例，推荐卡片场景使用。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-FontCollection-static getLocalInstance(): FontCollection--><!--Device-FontCollection-static getLocalInstance(): FontCollection-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Return value:**

| Type | Description |
| --- | --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) | 本地FontCollection实例对象，推荐卡片场景使用，可用于管理字体加载、卸载和排版等操作。 |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'
let fontCollection = text.FontCollection.getLocalInstance();
```

## loadFont

```TypeScript
loadFont(name: string, path: string | Resource): Promise<void>
```

加载自定义字体。使用Promise异步回调。其中参数name对应的值需要在[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的fontFamilies属性配置，才能显示自定义字体效果，支持的字体文件格式包含：ttf、otf。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-FontCollection-loadFont(name: string, path: string | Resource): Promise<void>--><!--Device-FontCollection-loadFont(name: string, path: string | Resource): Promise<void>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 加载字体后，调用该字体所使用的别名，可填写任意字符串，可使用该别名指定并使用该字体。 |
| path | string \| Resource | Yes | 需要加载的字体文件的路径，支持两种格式： "file:// + 字体文件绝对路径" 或 "rawfile/目录or文件名"。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

let fontCollection: text.FontCollection = new text.FontCollection();

@Entry
@Component
struct RenderTest {
  async loadFontPromise() {
    fontCollection.loadFont('testName', 'file:///system/fonts/a.ttf').then((data) => {
      console.info(`Succeeded in doing loadFont ${JSON.stringify(data)} `);
    }).catch((error: Error) => {
      console.error(`Failed to do loadFont, error: ${JSON.stringify(error)} message: ${error.message}`);
    });
  }

  aboutToAppear() {
    this.loadFontPromise();
  }

  build() {
  }
}
```

## loadFontSync

```TypeScript
loadFontSync(name: string, path: string | Resource): void
```

同步接口，加载自定义字体。其中参数name对应的值需要在[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的fontFamilies属性配置，才能显示自定义字体效果。支持的字体文件格式包含：ttf、otf。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-FontCollection-loadFontSync(name: string, path: string | Resource): void--><!--Device-FontCollection-loadFontSync(name: string, path: string | Resource): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 加载字体后，调用该字体所使用的名称。 |
| path | string \| Resource | Yes | 需要导入的字体文件的路径，应为 "file:// + 字体文件绝对路径" 或 "rawfile/目录or文件名"。 |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

let fontCollection: text.FontCollection = new text.FontCollection();

@Entry
@Component
struct RenderTest {
  LoadFontSyncTest() {
    fontCollection.loadFontSync('Clock_01', 'file:///system/fonts/HarmonyClock_01.ttf')
    let fontFamilies: Array<string> = ["Clock_01"]
    let myTextStyle: text.TextStyle = {
      fontFamilies: fontFamilies
    };
    let myParagraphStyle: text.ParagraphStyle = {
      textStyle: myTextStyle,
    }
    let paragraphBuilder: text.ParagraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);

    let textData = "Test loadFontSync to load the font file HarmonyClock_01.ttf.";
    paragraphBuilder.addText(textData);
    let paragraph: text.Paragraph = paragraphBuilder.build();
    paragraph.layoutSync(600);
  }

  aboutToAppear() {
    this.LoadFontSyncTest();
  }

  build() {
  }
}
```

## loadFontSyncWithCheck

ArkTS-Dyn:
```TypeScript
loadFontSyncWithCheck(name: string, path: string | Resource, index?: number): void
```

ArkTS-Sta:
```TypeScript
loadFontSyncWithCheck(name: string, path: string | Resource, index?: int): void
```

同步接口，加载自定义字体。其中参数name对应的值需要在[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的fontFamilies属性配置，才能显示自定义字体效果。支持的字体文件格式包含：ttf、otf、ttc。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-FontCollection-loadFontSyncWithCheck(name: string, path: string | Resource, index?: int): void--><!--Device-FontCollection-loadFontSyncWithCheck(name: string, path: string | Resource, index?: int): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 加载字体成功后，该字体对应的名称，可填写任意字符串，可使用该名称指定并使用该字体。 |
| path | string \| Resource | Yes | 需要加载的字体文件的路径，支持两种格式： "file:// + 字体文件绝对路径" 或 \\$rawfile('字体文件路径')。 |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 字体文件格式为ttc时，指定加载的字体索引。默认为0：表示加载ttc的第一个字体。 &lt;br&gt;非ttc格式文件索引值无意义，若指定索引，只能为0。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900008 | Corrupted file. |
| 25900003 | Failed to open the file. |
| 25900002 | File not found. |
| 25900001 | Parameter error. |
| 25900007 | Empty file. |
| 25900006 | Failed to read the file. |
| 25900005 | Failed to get the file size. |
| 25900004 | File seek failed. |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

let fc: text.FontCollection = text.FontCollection.getGlobalInstance();

@Entry
@Component
struct Index {
  message: string = 'Hello World';
  fontFamily: string = 'family';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontFamily(this.fontFamily)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          fc.loadFontSyncWithCheck(this.fontFamily, 'file:///system/fonts/NotoSansCJK-Regular.ttc', 1);
          try {
            fc.loadFontSyncWithCheck(this.fontFamily, '/system/fonts/NotoSansCJK-Regular.ttc', 1);
          } catch (e) {
            console.error(`Failed to do loadFontWithCheck, error: ${JSON.stringify(e)} message: ${e.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## loadFontWithCheck

ArkTS-Dyn:
```TypeScript
loadFontWithCheck(name: string, path: string | Resource, index?: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
loadFontWithCheck(name: string, path: string | Resource, index?: int): Promise<void>
```

加载自定义字体，使用Promise异步回调。其中参数name对应的值需要在[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的fontFamilies属性配置，才能显示自定义字体效果，支持的字体文件格式包含：ttf、otf、ttc。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-FontCollection-loadFontWithCheck(name: string, path: string | Resource, index?: int): Promise<void>--><!--Device-FontCollection-loadFontWithCheck(name: string, path: string | Resource, index?: int): Promise<void>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 加载字体成功后，该字体对应的名称，可填写任意字符串，可使用该名称指定并使用该字体。 |
| path | string \| Resource | Yes | 需要加载的字体文件的路径，支持两种格式： "file:// + 字体文件绝对路径" 或 \\$rawfile('字体文件路径')。 |
| index | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 字体文件格式为ttc时，指定加载的字体索引。默认为0：表示加载ttc的第一个字体。 &lt;br&gt;非ttc格式文件索引值无意义，若指定索引，只能为0。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 25900008 | Corrupted file. |
| 25900003 | Failed to open the file. |
| 25900002 | File not found. |
| 25900001 | Parameter error. |
| 25900007 | Empty file. |
| 25900006 | Failed to read the file. |
| 25900005 | Failed to get the file size. |
| 25900004 | File seek failed. |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

let fc: text.FontCollection = text.FontCollection.getGlobalInstance();

@Entry
@Component
struct Index {
  message: string = 'Hello World';
  fontFamily: string = 'family';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontFamily(this.fontFamily)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          fc.loadFontWithCheck(this.fontFamily, 'file:///system/fonts/NotoSansCJK-Regular.ttc', 1).then((data) => {
            console.info(`Succeeded in doing loadFontWithCheck ${JSON.stringify(data)} `);
          }).catch((error: Error) => {
            console.error(`Failed to do loadFontWithCheck, error: ${JSON.stringify(error)} message: ${error.message}`);
          });
          fc.loadFontWithCheck(this.fontFamily, '/system/fonts/NotoSansCJK-Regular.ttc', 1).then((data) => {
            console.info(`Succeeded in doing loadFontWithCheck ${JSON.stringify(data)} `);
          }).catch((error: Error) => {
            console.error(`Failed to do loadFontWithCheck, error: ${JSON.stringify(error)} message: ${error.message}`);
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## setParagraphCachesEnabled

```TypeScript
setParagraphCachesEnabled(enable: boolean): void
```

设置是否启用排版段落缓存。排版段落缓存可以加速重复文本的排版速度，但会占用额外的内存。未调用此接口前，系统默认开启排版段落缓存。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FontCollection-setParagraphCachesEnabled(enable: boolean): void--><!--Device-FontCollection-setParagraphCachesEnabled(enable: boolean): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | 是否启用排版段落缓存。true表示启用，false表示禁用。 |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('Enable Paragraph Caching').onClick(() => {
        text.FontCollection.getGlobalInstance().setParagraphCachesEnabled(true);
      })
      Button('Disable Paragraph Caching').onClick(() => {
        text.FontCollection.getGlobalInstance().setParagraphCachesEnabled(false);
      })
    }
  }
}
```

## unloadFont

```TypeScript
unloadFont(name: string): Promise<void>
```

卸载指定的自定义字体。使用Promise异步回调。

使用此接口卸载字体别名所对应的自定义字体后，对应的自定义字体将不再可用。

所有使用该字体别名的排版对象都应该被销毁重建。

- 卸载不存在的字体别名不会产生任何效果且不会抛出错误。  
- 此操作仅影响后续字体使用。  
- 卸载正在使用的字体可能导致文本渲染异常（如乱码或字形缺失）。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-FontCollection-unloadFont(name: string): Promise<void>--><!--Device-FontCollection-unloadFont(name: string): Promise<void>-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 需要卸载的字体的别名，与加载字体时使用的别名相同。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct UnloadFontTest {
  private fc: text.FontCollection = text.FontCollection.getGlobalInstance();
  @State content: string = "Default font"

  build() {
    Column({ space: 10 }) {
      Text(this.content)
        .fontFamily("custom")
      Button("load font")
        .onClick(async () => {
          await this.fc.loadFont("custom", "file:///system/fonts/NotoSansCJK-Regular.ttc")
          this.content = "Custom font"
        })
      Button("unload font")
        .onClick(async () => {
          await this.fc.unloadFont("custom")
          this.content = "Default font"
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

## unloadFontSync

```TypeScript
unloadFontSync(name: string): void
```

卸载指定的自定义字体，此接口为同步接口。

使用此接口卸载字体别名所对应的自定义字体后，对应的自定义字体将不再可用。

所有使用该字体别名的排版对象都应该被销毁重建。

- 卸载不存在的字体别名不会产生任何效果且不会抛出错误。  
- 此操作仅影响后续字体使用。  
- 卸载正在使用的字体可能导致文本渲染异常（如乱码或字形缺失）。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-FontCollection-unloadFontSync(name: string): void--><!--Device-FontCollection-unloadFontSync(name: string): void-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 需要取消注册的字体别名，与加载字体时使用的别名相同。 |

## Examples

```TypeScript
import { text } from '@kit.ArkGraphics2D'

@Entry
@Component
struct UnloadFontSyncTest {
  private fc: text.FontCollection = text.FontCollection.getGlobalInstance();
  @State content: string = "Default font"

  build() {
    Column({ space: 10 }) {
      Text(this.content)
        .fontFamily("custom")
      Button("load font")
        .onClick(() => {
          this.fc.loadFontSync("custom", "file:///system/fonts/NotoSansCJK-Regular.ttc")
          this.content = "Custom font"
        })
      Button("unload font")
        .onClick(() => {
          this.fc.unloadFontSync("custom")
          this.content = "Default font"
        })
    }.width("100%")
    .height("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

