# isOpenTouchGuideSync

## 导入模块

```TypeScript
```

## isOpenTouchGuideSync

```TypeScript
function isOpenTouchGuideSync(): boolean
```

查询触摸浏览模式是否开启。

**起始版本：** 23

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-accessibility-function isOpenTouchGuideSync(): boolean--><!--Device-accessibility-function isOpenTouchGuideSync(): boolean-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

let status: boolean = accessibility.isOpenTouchGuideSync();
```
