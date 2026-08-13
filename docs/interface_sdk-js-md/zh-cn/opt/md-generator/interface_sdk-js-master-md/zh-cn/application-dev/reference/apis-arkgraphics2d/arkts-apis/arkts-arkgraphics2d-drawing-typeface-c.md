# Typeface

Typeface类用于表示和管理字体对象。支持的字体操作包括：获取字体族名、从字体文件或rawfile资源构造字体、结合字体属性构造新字体，以及检查字体的加粗、斜体状态等。 > **说明：** > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

**废弃版本：** -1

<!--Device-drawing-class Typeface--><!--Device-drawing-class Typeface-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## getFamilyName

```TypeScript
getFamilyName(): string
```

获取字体的族名，即一套字体设计的名称。

**起始版本：** 11

**废弃版本：** -1

<!--Device-Typeface-getFamilyName(): string--><!--Device-Typeface-getFamilyName(): string-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| string |

## getFamilyName

```TypeScript
getFamilyName(): string | undefined
```

获取字体的族名，即一套字体设计的名称。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Typeface-getFamilyName(): string | undefined--><!--Device-Typeface-getFamilyName(): string | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| string |

## isBold

```TypeScript
isBold(): boolean
```

检查字体是否加粗。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Typeface-isBold(): boolean--><!--Device-Typeface-isBold(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## isItalic

```TypeScript
isItalic(): boolean
```

检查字体是否为斜体。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Typeface-isItalic(): boolean--><!--Device-Typeface-isItalic(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## makeFromCurrent

```TypeScript
makeFromCurrent(typefaceArguments: TypefaceArguments): Typeface
```

基于当前字体结合字体属性构造新的字体对象。

**起始版本：** 20

**废弃版本：** -1

<!--Device-Typeface-makeFromCurrent(typefaceArguments: TypefaceArguments): Typeface--><!--Device-Typeface-makeFromCurrent(typefaceArguments: TypefaceArguments): Typeface-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| typefaceArguments | [TypefaceArguments](arkts-arkgraphics2d-drawing-typefacearguments-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## makeFromCurrent

```TypeScript
makeFromCurrent(typefaceArguments: TypefaceArguments): Typeface | undefined
```

基于当前字体结合字体属性构造新的字体对象。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Typeface-makeFromCurrent(typefaceArguments: TypefaceArguments): Typeface | undefined--><!--Device-Typeface-makeFromCurrent(typefaceArguments: TypefaceArguments): Typeface | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| typefaceArguments | [TypefaceArguments](arkts-arkgraphics2d-drawing-typefacearguments-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## makeFromFile

```TypeScript
static makeFromFile(filePath: string): Typeface
```

从指定字体文件构造字体。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Typeface-static makeFromFile(filePath: string): Typeface--><!--Device-Typeface-static makeFromFile(filePath: string): Typeface-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## makeFromFile

```TypeScript
static makeFromFile(filePath: string): Typeface | undefined
```

从指定字体文件构造字体。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Typeface-static makeFromFile(filePath: string): Typeface | undefined--><!--Device-Typeface-static makeFromFile(filePath: string): Typeface | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## makeFromFileWithArguments

```TypeScript
static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface
```

根据字体文件路径和字体属性构造新的字体。

**起始版本：** 20

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Typeface-static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface--><!--Device-Typeface-static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| typefaceArguments | [TypefaceArguments](arkts-arkgraphics2d-drawing-typefacearguments-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## makeFromFileWithArguments

```TypeScript
static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface | undefined
```

根据字体文件路径和字体属性构造新的字体。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Typeface-static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface | undefined--><!--Device-Typeface-static makeFromFileWithArguments(filePath: string, typefaceArguments: TypefaceArguments): Typeface | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filePath | string | 是 |
| typefaceArguments | [TypefaceArguments](arkts-arkgraphics2d-drawing-typefacearguments-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## makeFromRawFile

```TypeScript
static makeFromRawFile(rawfile: Resource): Typeface
```

使用指定的字体文件构造字体，该字体文件需保存在应用资源文件夹的rawfile路径下。

**起始版本：** 18

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Typeface-static makeFromRawFile(rawfile: Resource): Typeface--><!--Device-Typeface-static makeFromRawFile(rawfile: Resource): Typeface-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rawfile | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## makeFromRawFile

```TypeScript
static makeFromRawFile(rawfile: Resource): Typeface | undefined
```

使用指定的字体文件构造字体，该字体文件需保存在应用资源文件夹的rawfile路径下。

**起始版本：** 23

**废弃版本：** -1

<!--Device-Typeface-static makeFromRawFile(rawfile: Resource): Typeface | undefined--><!--Device-Typeface-static makeFromRawFile(rawfile: Resource): Typeface | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rawfile | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## makeFromRawFileWithArguments

```TypeScript
static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface
```

使用指定的字体文件和字体属性构造新的字体，该字体文件需保存在应用资源文件夹的rawfile路径下。

**起始版本：** 20

**废弃版本：** -1

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-Typeface-static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface--><!--Device-Typeface-static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rawfile | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| typefaceArguments | [TypefaceArguments](arkts-arkgraphics2d-drawing-typefacearguments-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |

## makeFromRawFileWithArguments

```TypeScript
static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface | undefined
```

使用指定的字体文件和字体属性构造新的字体，该字体文件需保存在应用资源文件夹的rawfile路径下。

**起始版本：** 24

**废弃版本：** -1

<!--Device-Typeface-static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface | undefined--><!--Device-Typeface-static makeFromRawFileWithArguments(rawfile: Resource, typefaceArguments: TypefaceArguments): Typeface | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rawfile | [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |
| typefaceArguments | [TypefaceArguments](arkts-arkgraphics2d-drawing-typefacearguments-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |
