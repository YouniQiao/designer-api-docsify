# getFontDescriptorByFullName

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getFontDescriptorByFullName

```TypeScript
function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>
```

根据字体名称和类型获取字体描述符，使用Promise异步回调。字体描述符是描述字体特征的数据结构，包含字体外观和属性的详细信息。

**起始版本：** 14

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fullName | string | 是 |
| fontType | [SystemFontType](arkts-arkgraphics2d-text-systemfonttype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
