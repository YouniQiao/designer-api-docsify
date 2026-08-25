# create

## 导入模块

```TypeScript
import { displaySync } from '@kit.ArkGraphics2D';
```

## create

```TypeScript
function create(): DisplaySync
```

创建DisplaySync对象，通过此对象设置UI自绘制内容帧率。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [DisplaySync](arkts-arkgraphics2d-displaysync-displaysync-i.md) |

**示例**

```TypeScript
let backDisplaySync: displaySync.DisplaySync = displaySync.create();
```
