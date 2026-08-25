# createFilter

## 导入模块

```TypeScript
import { uiEffect } from '@kit.ArkGraphics2D';
```

## createFilter

```TypeScript
function createFilter(): Filter
```

创建Filter实例用于给组件添加多种Filter效果。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**示例**

```TypeScript
let filter : uiEffect.Filter = uiEffect.createFilter()
```
