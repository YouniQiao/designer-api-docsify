# getFontCount

## 导入模块

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## getFontCount

```TypeScript
function getFontCount(path: string | Resource) : number
```

根据字体文件路径获取包含的字体文件数。如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回0。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |
