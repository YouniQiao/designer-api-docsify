# cancelOverflow

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## cancelOverflow

```TypeScript
function cancelOverflow(formId: string): Promise<void>
```

Cancels an animation. This API takes effect only for   
[scene-based widgets](../../../form/arkts-ui-widget-configuration.md#sceneanimationparams-field). This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-formProvider-function cancelOverflow(formId: string): Promise<void>--><!--Device-formProvider-function cancelOverflow(formId: string): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Widget ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 801 | Capability not supported.function cancelOverflow can not work correctly due to limited device capabilities. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 16501011 | The form cannot support this operation. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |

## Examples

```TypeScript
import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288'; // formId of the widget. Use the actual form ID.

try {
  formProvider.cancelOverflow(formId).then(() => {
    console.info('cancelOverflow succeed.');
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

