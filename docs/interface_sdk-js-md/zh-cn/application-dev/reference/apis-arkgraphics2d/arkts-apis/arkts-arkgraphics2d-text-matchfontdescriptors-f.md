# matchFontDescriptors

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## matchFontDescriptors

```TypeScript
function matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>
```

根据指定的字体描述符返回所有符合要求的系统字体描述符，使用Promise异步回调。

**起始版本：** 18

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| desc | [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
