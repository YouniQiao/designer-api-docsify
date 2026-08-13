# create

## Modules to Import

```TypeScript
import { floatView } from '@kit.ArkUI';
```

## create

```TypeScript
function create(config: FloatViewConfiguration): Promise<FloatViewController>
```

Creates a float view controller. This API uses a promise to return the result.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-floatView-function create(config: FloatViewConfiguration): Promise<FloatViewController>--><!--Device-floatView-function create(config: FloatViewConfiguration): Promise<FloatViewController>-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [FloatViewConfiguration](arkts-arkui-floatview-floatviewconfiguration-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |
| [1300016](../errorcode-window.md#1300016-parameter-verification-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { floatView } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private floatViewController: floatView.FloatViewController | undefined = undefined;
  aboutToAppear(): void {
    // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
    let ctx = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // Create a float view configuration object.
    let config: floatView.FloatViewConfiguration = {
      context: ctx,
      templateType: floatView.FloatViewTemplateType.ROUNDED_RECTANGLE
    };
    try {
      // Create a float view controller.
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
