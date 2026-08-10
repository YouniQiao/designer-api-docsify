# onFlashReminderStateChange

## Modules to Import

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
```

## onFlashReminderStateChange

```TypeScript
function onFlashReminderStateChange(callback: Callback<boolean>): void
```

监听闪烁提醒功能启用状态变化事件。使用callback异步回调。

> **说明：**
> 
> - 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。
> 
> - 调用此方法后，务必在对象生命周期结束前使用
> [accessibility.offFlashReminderStateChange](accessibility.offFlashReminderStateChange(callback?: Callback&lt;boolean&gt;))
> 取消监听，否则可能会导致崩溃。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-accessibility-function onFlashReminderStateChange(callback: Callback<boolean>): void--><!--Device-accessibility-function onFlashReminderStateChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | Yes | 回调函数。返回true表示闪烁提醒模式已开启；返回false表示闪烁提醒模式已关闭。 |

## Examples

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: (data: boolean) => void = this.eventCallback;
  eventCallback(data: boolean): void {
    console.info(`subscribe flashReminder state change, result: ${JSON.stringify(data)}`);
  }

  aboutToAppear(): void {
    accessibility.onFlashReminderStateChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```

