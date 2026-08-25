# offEnabledAccessibilityExtensionListChange（系统接口）

## 导入模块

```TypeScript
import { config } from '@kit.AccessibilityKit';
```

## offEnabledAccessibilityExtensionListChange

```TypeScript
function offEnabledAccessibilityExtensionListChange(callback?: Callback<void>): void
```

取消启用的辅助扩展的列表变化监听。使用callback异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_ACCESSIBILITY_CONFIG

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { config } from '@kit.AccessibilityKit';

@Entry
@Component
struct Index {
  callback: () => void = this.eventCallback;
  eventCallback(): void {
    console.info(`enabled accessibility extension list change`);
  }

  aboutToAppear(): void {
    config.onEnabledAccessibilityExtensionListChange(this.callback);
  }

  aboutToDisappear(): void {
    config.offEnabledAccessibilityExtensionListChange(this.callback);
  }

  build() {
    Column() {
    }
  }
}
```
