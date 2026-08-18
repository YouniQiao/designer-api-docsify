# create

## 导入模块

```TypeScript
```

## create

```TypeScript
function create(config: FloatingBallConfiguration): Promise<FloatingBallController>
```

创建闪控球控制器，使用Promise异步回调。

**起始版本：** 23

<!--Device-floatingBall-function create(config: FloatingBallConfiguration): Promise<FloatingBallController>--><!--Device-floatingBall-function create(config: FloatingBallConfiguration): Promise<FloatingBallController>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [FloatingBallConfiguration](arkts-arkui-floatingball-floatingballconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FloatingBallController](arkts-arkui-floatingball-floatingballcontroller-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 声明闪控球控制器实例
let floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回的结果为UIAbilityContext
let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext; 
// 配置闪控球控制器参数
let config: floatingBall.FloatingBallConfiguration = {
  context: ctx,
};
try {
  // 创建闪控球控制器
  floatingBall.create(config).then((data: floatingBall.FloatingBallController) => {
    // 保存控制器实例
    floatingBallController = data;
    console.info(`Succeeded in creating floating ball controller. Data: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to create floating ball controller. Cause:${err.code}, message:${err.message}`);
  });
} catch (e) {
  console.error(`Failed to create floating ball controller. Cause:${e.code}, message:${e.message}`);
}
```
