# requestOverflow

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## requestOverflow

```TypeScript
function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>
```

Requests an animation. This API takes effect only for   
[scene-based widgets](../../../form/arkts-ui-widget-configuration.md#sceneanimationparams-field). This API uses a promise to return the result.

> **NOTE：**
> 

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-formProvider-function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>--><!--Device-formProvider-function requestOverflow(formId: string, overflowInfo: formInfo.OverflowInfo): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| [overflowInfo](arkts-form-forminfo-overflowrequest-i-sys.md) | formInfo.OverflowInfo | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501003-widget-not-operatable) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16501001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [16500060](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500060-service-connection-failure) |
| [16501011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501011-api-not-supported) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [16500100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |

## Examples

```TypeScript
import { formInfo, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

let formId: string = '12400633174999288'; // formId of the widget. Use the actual form ID.
let overflowInfo: formInfo.OverflowInfo = {
  area: {
    left: -10,
    top: -10,
    width: 180,
    height: 180
  },
  duration: 1000,
  useDefaultAnimation: false,
};

try {
  formProvider.requestOverflow(formId, overflowInfo).then(() => {
    console.info('requestOverflow succeed.');
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
