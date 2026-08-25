# @ohos.UiTest

UiTest提供UI自动化测试能力，供开发者在测试场景使用，主要支持控件查找与操作、坐标点击/滑动、按键注入、截图、窗口管理、多指操作、鼠标/手写笔/触摸板操作等能力。
 该模块提供以下功能：
 - [On<sup>9+</sup>](arkts-test-uitest-on-c.md)：提供控件特征描述能力，用于控件筛选匹配查找。
 - [Component<sup>9+</sup>](arkts-test-uitest-component-c.md)：代表UI界面上的指定控件，提供控件属性获取，控件点击，滑动查找，文本注入等能力。
 - [Driver<sup>9+</sup>](arkts-test-uitest-driver-c.md)：入口类，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。
 - [UiWindow<sup>9+</sup>](arkts-test-uitest-uiwindow-c.md)：代表UI界面上的窗口对象，提供窗口属性获取，窗口拖动、调整窗口大小等能力。
 - [By<sup>(deprecated)</sup>](arkts-test-uitest-by-c.md)：提供控件特征描述能力，用于控件筛选匹配查找。从API version 8开始支持，从API version 9开始废弃，建议使用
 [On<sup>9+</sup>](arkts-test-uitest-on-c.md)替代。
 - [UiComponent<sup>(deprecated)</sup>](arkts-test-uitest-uicomponent-c.md)：代表UI界面上的指定控件，提供控件属性获取，控件点击，滑动查找，文本注入等能力。从API version 8开始支持，从API version
 9开始废弃，建议使用[Component<sup>9+</sup>](arkts-test-uitest-component-c.md)替代。
 - [UiDriver<sup>(deprecated)</sup>](arkts-test-uitest-uidriver-c.md)：入口类，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。从API version 8开始支持，从API version 9开始废弃，建议使用
 [Driver<sup>9+</sup>](arkts-test-uitest-driver-c.md)替代。
 > **说明：**
 >
 > - 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
 > - 本模块接口在[自动化测试脚本](../../../application-test/uitest-guidelines.md)中使用。
 > - 本模块接口不支持并发调用。


## 导入模块

```TypeScript
import { Component, DisplayRotation, Driver, MatchPattern, MouseButton, ON, On, PointerMatrix, ResizeDirection, UIElementInfo, UIEventObserver, UiDirection, UiWindow, WindowMode, Point, WindowFilter, Rect, TouchPadSwipeOptions, InputTextMode, WindowChangeType, ComponentEventType, WindowChangeOptions, ComponentEventOptions, TouchOptions, KeyOptions, PenKey, PenMode, PenKeyOperation, PenKeyOperationOptions } from 'kits/@kit.TestKit';
import { UiComponent, UiDriver, BY, By } from 'kits/@kit.TestKit';
```

## 汇总

### 类

| 名称 |
| --- |
| [By](arkts-test-uitest-by-c.md) |
| [Component](arkts-test-uitest-component-c.md) |
| [Driver](arkts-test-uitest-driver-c.md) |
| [On](arkts-test-uitest-on-c.md) |
| [PointerMatrix](arkts-test-uitest-pointermatrix-c.md) |
| [UiComponent](arkts-test-uitest-uicomponent-c.md) |
| [UiDriver](arkts-test-uitest-uidriver-c.md) |
| [UiWindow](arkts-test-uitest-uiwindow-c.md) |

### 接口

| 名称 |
| --- |
| [ComponentEventOptions](arkts-test-uitest-componenteventoptions-i.md) |
| [InputTextMode](arkts-test-uitest-inputtextmode-i.md) |
| [KeyOptions](arkts-test-uitest-keyoptions-i.md) |
| [PenKeyOperationOptions](arkts-test-uitest-penkeyoperationoptions-i.md) |
| [Point](arkts-test-uitest-point-i.md) |
| [Rect](arkts-test-uitest-rect-i.md) |
| [TouchOptions](arkts-test-uitest-touchoptions-i.md) |
| [TouchPadSwipeOptions](arkts-test-uitest-touchpadswipeoptions-i.md) |
| [UIElementInfo](arkts-test-uitest-uielementinfo-i.md) |
| [UIEventObserver](arkts-test-uitest-uieventobserver-i.md) |
| [WindowChangeOptions](arkts-test-uitest-windowchangeoptions-i.md) |
| [WindowFilter](arkts-test-uitest-windowfilter-i.md) |

### 枚举

| 名称 |
| --- |
| [ComponentEventType](arkts-test-uitest-componenteventtype-e.md) |
| [DisplayRotation](arkts-test-uitest-displayrotation-e.md) |
| [MatchPattern](arkts-test-uitest-matchpattern-e.md) |
| [MouseButton](arkts-test-uitest-mousebutton-e.md) |
| [PenKey](arkts-test-uitest-penkey-e.md) |
| [PenKeyOperation](arkts-test-uitest-penkeyoperation-e.md) |
| [PenMode](arkts-test-uitest-penmode-e.md) |
| [ResizeDirection](arkts-test-uitest-resizedirection-e.md) |
| [UiDirection](arkts-test-uitest-uidirection-e.md) |
| [WindowChangeType](arkts-test-uitest-windowchangetype-e.md) |
| [WindowMode](arkts-test-uitest-windowmode-e.md) |

### 属性

| 名称 |
| --- |
| [BY](arkts-test-ohosuitest-p.md) |
| [ON](arkts-test-ohosuitest-p.md) |
