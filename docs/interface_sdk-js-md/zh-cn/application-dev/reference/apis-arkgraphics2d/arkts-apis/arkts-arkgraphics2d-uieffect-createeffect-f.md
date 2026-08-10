# createEffect

## 导入模块

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## createEffect

```TypeScript
function createEffect(): VisualEffect
```

创建VisualEffect实例用于给组件添加多种VisualEffect效果。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**卡片能力：** 从API版本24开始，该接口支持在ArkTS卡片中使用。

<!--Device-uiEffect-function createEffect(): VisualEffect--><!--Device-uiEffect-function createEffect(): VisualEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VisualEffect](../../apis-arkui/arkts-components/arkts-arkui-visualeffect-t.md) | 返回VisualEffect实例，支持添加多种VisualEffect效果。 |

## 示例

```TypeScript
// 创建VisualEffect实例
let visualEffect: uiEffect.VisualEffect = uiEffect.createEffect();
```

