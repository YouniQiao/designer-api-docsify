# offAccessibilityStateChange

## 导入模块

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from '@kit.AccessibilityKit';
```

## offAccessibilityStateChange

```TypeScript
function offAccessibilityStateChange(callback?: Callback<boolean>): void
```

取消监听辅助应用启用状态变化事件。使用callback异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-accessibility-function offAccessibilityStateChange(callback?: Callback<boolean>): void--><!--Device-accessibility-function offAccessibilityStateChange(callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 | 回调函数，取消指定callback对象的事件响应。需与accessibility.onAccessibilityStateChange的 callback一致。缺省时，表示注销所有已注册事件。 |

**示例**

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`accessibility state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onAccessibilityStateChange(this.callback);
  }

  aboutToDisappear(): void {
    accessibility.offAccessibilityStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

