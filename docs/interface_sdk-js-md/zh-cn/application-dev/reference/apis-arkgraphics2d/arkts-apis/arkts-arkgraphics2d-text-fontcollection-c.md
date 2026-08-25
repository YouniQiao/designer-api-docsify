# FontCollection

字体集，用于管理文本排版所需的字体资源。FontCollection为[ParagraphBuilder](arkts-arkgraphics2d-text-paragraphbuilder-c.md)提供字体匹配和字形查找能力，是文本排版管线的基础组件。提供全局实例 （[getGlobalInstance](#getglobalinstance)）和本地实例（ [getLocalInstance](#getlocalinstance)），全局实例加载的字体在应用内共享，适用于普通应用场景；本地实例各实例独立，加载的字体仅对当前实例生效、实 例间互不影响，推荐卡片场景使用。支持通过[loadFontSync](#loadfontsync)或 [loadFont](#loadfont)加载自定义字体。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## clearCaches

```TypeScript
clearCaches(): void
```

清理字体排版缓存。字体排版缓存本身设有内存上限和自动清理机制，所占内存有限。如无特殊内存要求，不建议清理。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

## getGlobalInstance

```TypeScript
static getGlobalInstance(): FontCollection
```

获取应用全局FontCollection实例。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) |

## getLocalInstance

```TypeScript
static getLocalInstance(): FontCollection
```

获取本地FontCollection实例，推荐卡片场景使用。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [FontCollection](arkts-arkgraphics2d-text-fontcollection-c.md) |

## loadFont

```TypeScript
loadFont(name: string, path: string | Resource): Promise<void>
```

加载自定义字体。使用Promise异步回调。其中参数name对应的值需要在[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的fontFamilies属性配置，才能显示自定义字体效果，支持的字体文件格式包含： ttf、otf。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## loadFontSync

```TypeScript
loadFontSync(name: string, path: string | Resource): void
```

同步接口，加载自定义字体。其中参数name对应的值需要在[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的fontFamilies属性配置，才能显示自定义字体效果。支持的字体文件格式包含：ttf、otf。

**起始版本：** 12

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

## loadFontSyncWithCheck

```TypeScript
loadFontSyncWithCheck(name: string, path: string | Resource, index?: number): void
```

同步接口，加载自定义字体。其中参数name对应的值需要在[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的fontFamilies属性配置，才能显示自定义字体效果。支持的字体文件格式包含：ttf、otf、 ttc。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| index | number | 否 |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |
| [25900002](../errorcode-drawing.md#25900002-文件未找到) |
| [25900003](../errorcode-drawing.md#25900003-打开文件失败) |
| [25900004](../errorcode-drawing.md#25900004-文件定位失败) |
| [25900005](../errorcode-drawing.md#25900005-获取文件大小失败) |
| [25900006](../errorcode-drawing.md#25900006-读取文件失败) |
| [25900007](../errorcode-drawing.md#25900007-文件为空) |
| [25900008](../errorcode-drawing.md#25900008-文件损坏) |

## loadFontWithCheck

```TypeScript
loadFontWithCheck(name: string, path: string | Resource, index?: number): Promise<void>
```

加载自定义字体，使用Promise异步回调。其中参数name对应的值需要在[TextStyle](arkts-arkgraphics2d-text-textstyle-i.md)中的fontFamilies属性配置，才能显示自定义字体效果，支持的字体文件格式包含： ttf、otf、ttc。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| index | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../errorcode-drawing.md#25900001-参数值异常) |
| [25900002](../errorcode-drawing.md#25900002-文件未找到) |
| [25900003](../errorcode-drawing.md#25900003-打开文件失败) |
| [25900004](../errorcode-drawing.md#25900004-文件定位失败) |
| [25900005](../errorcode-drawing.md#25900005-获取文件大小失败) |
| [25900006](../errorcode-drawing.md#25900006-读取文件失败) |
| [25900007](../errorcode-drawing.md#25900007-文件为空) |
| [25900008](../errorcode-drawing.md#25900008-文件损坏) |

## setParagraphCachesEnabled

```TypeScript
setParagraphCachesEnabled(enable: boolean): void
```

设置是否启用排版段落缓存。排版段落缓存可以加速重复文本的排版速度，但会占用额外的内存。未调用此接口前，系统默认开启排版段落缓存。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## unloadFont

```TypeScript
unloadFont(name: string): Promise<void>
```

卸载指定的自定义字体。使用Promise异步回调。使用此接口卸载字体别名所对应的自定义字体后，对应的自定义字体将不再可用。所有使用该字体别名的排版对象都应该被销毁重建。  
- 卸载不存在的字体别名不会产生任何效果且不会抛出错误。  
- 此操作仅影响后续字体使用。  
- 卸载正在使用的字体可能导致文本渲染异常（如乱码或字形缺失）。

**起始版本：** 20

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## unloadFontSync

```TypeScript
unloadFontSync(name: string): void
```

卸载指定的自定义字体，此接口为同步接口。使用此接口卸载字体别名所对应的自定义字体后，对应的自定义字体将不再可用。所有使用该字体别名的排版对象都应该被销毁重建。  
- 卸载不存在的字体别名不会产生任何效果且不会抛出错误。  
- 此操作仅影响后续字体使用。  
- 卸载正在使用的字体可能导致文本渲染异常（如乱码或字形缺失）。

**起始版本：** 20

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
