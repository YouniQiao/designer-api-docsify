# isOpenTouchGuide

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## isOpenTouchGuide

```TypeScript
function isOpenTouchGuide(callback: AsyncCallback<boolean>): void
```

判断触摸浏览模式是否开启。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [isOpenTouchGuideSync](arkts-accessibility-accessibility-isopentouchguidesync-f.md)

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isOpenTouchGuide

```TypeScript
function isOpenTouchGuide(): Promise<boolean>
```

判断触摸浏览模式是否开启。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [isOpenTouchGuideSync](arkts-accessibility-accessibility-isopentouchguidesync-f.md)

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
