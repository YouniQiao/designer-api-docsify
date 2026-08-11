# create

## Modules to Import

```TypeScript
import { floatingBall } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(config: FloatingBallConfiguration): Promise<FloatingBallController>
```

Creates a floating ball controller. This API uses a promise to return the result.

**Since:** 20

<!--Device-floatingBall-function create(config: FloatingBallConfiguration): Promise<FloatingBallController>--><!--Device-floatingBall-function create(config: FloatingBallConfiguration): Promise<FloatingBallController>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [FloatingBallConfiguration](arkts-arkui-floatingball-floatingballconfiguration-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FloatingBallController&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1300019](../errorcode-window.md#1300019-floating-ball-parameter-verification-error) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1300023](../errorcode-window.md#1300023-internal-error-of-the-floating-ball) |

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
