# isOpenAccessibility

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## isOpenAccessibility

```TypeScript
function isOpenAccessibility(callback: AsyncCallback<boolean>): void
```

判断是否启用了辅助应用。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [isOpenAccessibilitySync](arkts-accessibility-accessibility-isopenaccessibilitysync-f.md)

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isOpenAccessibility

```TypeScript
function isOpenAccessibility(): Promise<boolean>
```

判断是否启用了辅助应用。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [isOpenAccessibilitySync](arkts-accessibility-accessibility-isopenaccessibilitysync-f.md)

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
