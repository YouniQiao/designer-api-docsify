# getFontDescriptorsFromPath

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getFontDescriptorsFromPath

```TypeScript
function getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>
```

根据字体文件路径获取字体描述符数组。使用Promise异步回调。

> **说明：**&gt;
> - 如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回空数组。&gt;
> - [FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md)中的weight字段并不精准对应字体文件内部的字重数值，而是将字体文件中的实际字重四舍五入映射到
> [FontWeight](arkts-arkgraphics2d-text-fontweight-e.md)枚举值后的结果。例如，字体文件字重350会映射为400，对应枚举为W400。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[FontDescriptor](arkts-arkgraphics2d-text-fontdescriptor-i.md)&gt;&gt; |
