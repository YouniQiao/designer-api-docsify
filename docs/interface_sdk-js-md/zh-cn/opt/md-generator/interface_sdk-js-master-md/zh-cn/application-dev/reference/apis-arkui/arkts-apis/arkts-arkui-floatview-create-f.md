# create

## 导入模块

```TypeScript
```

## create

```TypeScript
function create(config: FloatViewConfiguration): Promise<FloatViewController>
```

创建标准悬浮窗控制器。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-floatView-function create(config: FloatViewConfiguration): Promise<FloatViewController>--><!--Device-floatView-function create(config: FloatViewConfiguration): Promise<FloatViewController>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [FloatViewConfiguration](arkts-arkui-floatview-floatviewconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { floatView } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private floatViewController: floatView.FloatViewController | undefined = undefined;
  aboutToAppear(): void {
    // 请在组件内获取context，确保this.getUIContext().getHostContext()返回的结果为UIAbilityContext
    let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 创建闪控窗配置对象
    let config: floatView.FloatViewConfiguration = {
      context: ctx,
      templateType: floatView.FloatViewTemplateType.ROUNDED_RECTANGLE
    };
    try {
      // 创建闪控窗控制器
      floatView.create(config).then((data: floatView.FloatViewController) => {
        this.floatViewController = data;
        console.info(`Succeeded in creating float view controller. Data: ${data}`);
      }).catch((err: BusinessError): void => {
        console.error(`Failed to create float view controller. Cause:${err.code}, message:${err.message}`);
      });
    } catch (e) {
      console.error(`Failed to create float view controller. Cause:${e.code}, message:${e.message}`);
    }
  }
}
```
