# isSeniorModeEnabled

## isSeniorModeEnabled

```TypeScript
function isSeniorModeEnabled(): Promise<boolean>
```

判断关怀模式是否开启。使用Promise异步回调。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-accessibility-function isSeniorModeEnabled(): Promise<boolean>--><!--Device-accessibility-function isSeniorModeEnabled(): Promise<boolean>-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9300000](../errorcode-accessibility.md#9300000-无障碍系统服务工作异常) |

## 示例

```TypeScript
import { accessibility } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    accessibility.isSeniorModeEnabled().then((data: boolean) => {
      console.info(`success data:isSeniorModeEnabled : ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to call isSeniorModeEnabled. Code:${err.code}, message:${err.message}`);
    });
  }

  build() {
    Column() {
    }
  }
}
```
