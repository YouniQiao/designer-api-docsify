# createFilter

## 导入模块

```TypeScript
import uiEffect from '@kit.ArkGraphics2D';
```

## createFilter

```TypeScript
function createFilter(): Filter
```

创建Filter实例用于给组件添加多种Filter效果。

**起始版本：** 12

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) | 返回Filter实例，支持添加多种Filter效果。 |

**示例**

```TypeScript
// 创建Filter实例
let filter: uiEffect.Filter = uiEffect.createFilter();
```
