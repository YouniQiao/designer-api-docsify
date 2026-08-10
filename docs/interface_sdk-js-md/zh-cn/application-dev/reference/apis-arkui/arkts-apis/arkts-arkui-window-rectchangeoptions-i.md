# RectChangeOptions

窗口矩形（窗口位置及窗口大小）变化返回的值及变化原因。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-window-interface RectChangeOptions--><!--Device-window-interface RectChangeOptions-End-->

**系统能力：** SystemCapability.Window.SessionManager

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## reason

```TypeScript
reason: RectChangeReason
```

窗口矩形变化的原因。

**类型：** [RectChangeReason](arkts-arkui-uiextension-rectchangereason-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RectChangeOptions-reason: RectChangeReason--><!--Device-RectChangeOptions-reason: RectChangeReason-End-->

**系统能力：** SystemCapability.Window.SessionManager

## rect

```TypeScript
rect: Rect
```

New value of the window rectangle.

**类型：** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-RectChangeOptions-rect: Rect--><!--Device-RectChangeOptions-rect: Rect-End-->

**系统能力：** SystemCapability.Window.SessionManager

