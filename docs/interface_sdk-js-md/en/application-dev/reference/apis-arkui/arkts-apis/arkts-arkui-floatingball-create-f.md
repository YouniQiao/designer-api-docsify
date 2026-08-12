# create

## Modules to Import

```TypeScript
import { floatingBall } from '@kit.ArkUI';
```

## create

```TypeScript
function create(config: FloatingBallConfiguration): Promise<FloatingBallController>
```

Creates a floating ball controller. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-floatingBall-function create(config: FloatingBallConfiguration): Promise<FloatingBallController>--><!--Device-floatingBall-function create(config: FloatingBallConfiguration): Promise<FloatingBallController>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [FloatingBallConfiguration](arkts-arkui-floatingball-floatingballconfiguration-i.md) | Yes | Parameters for creating the floating ball controller. This parameter cannot be empty, and **context** that is used to construct this parameter cannot be empty. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[FloatingBallController](arkts-arkui-floatingball-floatingballcontroller-i.md)&gt; | Promise used to return the floating ball controller. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1300019](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-window.md#1300019-floating-ball-parameter-verification-error) | Wrong parameters for operating the floating ball. Possible causes: &lt;br&gt;1.The context parameter is null. &lt;br&gt;2.The FloatingBallConfiguration parameter is null. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1300023](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-window.md#1300023-internal-error-of-the-floating-ball) | Floating ball internal error. Possible causes: &lt;br&gt;1.The application context or main window is invalid. &lt;br&gt;2.System internal error, such as null pointer or insufficient memory. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let floatingBallController: floatingBall.FloatingBallController | undefined = undefined;
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext; 
let config: floatingBall.FloatingBallConfiguration = {
  context: ctx,
};
try {
  floatingBall.create(config).then((data: floatingBall.FloatingBallController) => {
    floatingBallController = data;
    console.info(`Succeeded in creating floating ball controller. Data: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to create floating ball controller. Cause:${err.code}, message:${err.message}`);
  });
} catch(e) {
  console.error(`Failed to create floating ball controller. Cause:${e.code}, message:${e.message}`);
}
```

