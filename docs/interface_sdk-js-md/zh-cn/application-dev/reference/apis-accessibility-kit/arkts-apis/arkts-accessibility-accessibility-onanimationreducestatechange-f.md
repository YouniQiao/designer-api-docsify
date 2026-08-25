# onAnimationReduceStateChange

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## onAnimationReduceStateChange

```TypeScript
function onAnimationReduceStateChange(callback: Callback<boolean>): void
```

监听减弱动效模式启用状态变化事件。使用callback异步回调。

> **说明：**&gt;
> - 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。&gt;
> - 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用
> [accessibility.offAnimationReduceStateChange](arkts-accessibility-accessibility-offanimationreducestatechange-f.md)取消监听，否则可能会导致崩溃。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |
