# isFontSupported

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## isFontSupported

```TypeScript
function isFontSupported(fontURL: string | Resource): boolean
```

检查系统是否支持指定的字体文件。可在加载自定义字体前预先验证字体文件的可用性，避免因字体不支持导致文本渲染异常。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fontURL | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
