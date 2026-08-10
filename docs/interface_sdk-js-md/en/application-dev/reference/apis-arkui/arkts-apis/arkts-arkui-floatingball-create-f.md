# create

## Modules to Import

```TypeScript
import { floatingBall } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(config: FloatingBallConfiguration): Promise<FloatingBallController>
```

创建闪控球控制器，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-floatingBall-function create(config: FloatingBallConfiguration): Promise<FloatingBallController>--><!--Device-floatingBall-function create(config: FloatingBallConfiguration): Promise<FloatingBallController>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [FloatingBallConfiguration](arkts-arkui-floatingball-floatingballconfiguration-i.md) | Yes | 创建闪控球控制器的参数。该参数不能为空，并且构造该参数的context不能为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;FloatingBallController&gt; | Promise对象。返回当前创建的闪控球控制器。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1300019 | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.The context parameter is null. &lt;br&gt;2.The FloatingBallConfiguration parameter is null. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 1300023 | Floating ball internal error. Possible causes: &lt;br&gt;1.The application context or main window is invalid. &lt;br&gt;2.System internal error, such as null pointer or insufficient memory. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Declare the floating ball controller instance.
let floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext; 
// Configure the floating ball controller.
let config: floatingBall.FloatingBallConfiguration = {
  context: ctx,
};
try {
  // Create a floating ball controller.
  floatingBall.create(config).then((data: floatingBall.FloatingBallController) => {
    // Save the controller instance.
    floatingBallController = data;
    console.info(`Succeeded in creating floating ball controller. Data: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to create floating ball controller. Cause:${err.code}, message:${err.message}`);
  });
} catch (e) {
  console.error(`Failed to create floating ball controller. Cause:${e.code}, message:${e.message}`);
}
```

