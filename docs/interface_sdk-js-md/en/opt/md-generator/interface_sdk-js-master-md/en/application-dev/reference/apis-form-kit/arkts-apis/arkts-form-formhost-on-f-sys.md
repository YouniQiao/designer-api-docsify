# on (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## on("formUninstall")

```TypeScript
function on(type: "formUninstall", callback: Callback<string>): void
```

Subscribes to widget uninstall events. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Widget uninstall is different from widget removal. When an application is uninstalled, the corresponding widget
> is automatically uninstalled.

**Since:** 9

<!--Device-formHost-function on(type: "formUninstall", callback: Callback<string>): void--><!--Device-formHost-function on(type: "formUninstall", callback: Callback<string>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | "formUninstall" | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## on('formOverflow')

```TypeScript
function on(type: 'formOverflow', callback: Callback<formInfo.OverflowRequest>): void
```

Subscribes to the interactive widget animation request event. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-formHost-function on(type: 'formOverflow', callback: Callback<formInfo.OverflowRequest>): void--><!--Device-formHost-function on(type: 'formOverflow', callback: Callback<formInfo.OverflowRequest>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'formOverflow' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.OverflowRequest&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formHost.on('formOverflow', (request: formInfo.OverflowRequest) => {
    console.info(`formHost on formOverflow, formId is ${request.formId}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```


## on('changeSceneAnimationState')

```TypeScript
function on(type: 'changeSceneAnimationState', 
    callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void
```

Subscribes to the event of switching the interactive widget state. An interactive widget can be in the active or inactive state. In the inactive state, the interactive widget is the same as a common widget. In the active state, the interactive widget can start the **LiveFormExtensionAbility** process developed by the widget host to implement interactive widget animations. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-formHost-function on(type: 'changeSceneAnimationState',     callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void--><!--Device-formHost-function on(type: 'changeSceneAnimationState',     callback: Callback<formInfo.ChangeSceneAnimationStateRequest>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'changeSceneAnimationState' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.ChangeSceneAnimationStateRequest&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formHost.on('changeSceneAnimationState', (request: formInfo.ChangeSceneAnimationStateRequest): void => {
    console.info(`formHost on changeSceneAnimationState, formId is ${request.formId}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```


## on('getFormRect')

```TypeScript
function on(type: 'getFormRect', callback: formInfo.GetFormRectInfoCallback): void
```

Subscribes to the event of requesting widget position and dimension. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-formHost-function on(type: 'getFormRect', callback: formInfo.GetFormRectInfoCallback): void--><!--Device-formHost-function on(type: 'getFormRect', callback: formInfo.GetFormRectInfoCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'getFormRect' | Yes |
| callback | formInfo.GetFormRectInfoCallback | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { formHost, formInfo } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  formHost.on('getFormRect', (formId: string): Promise<formInfo.Rect> => {
    // The widget host needs to process the request, and calculate and return the widget dimension and position information.
    return new Promise<formInfo.Rect>((resolve: Function) => {
      console.info(`formHost on getFormRect, formId is ${formId}`);
      let formRect: formInfo.Rect = {
        left: 0,
        top: 0,
        width: 0,
        height: 0
      };
      resolve(formRect);
    })
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```


## on('getLiveFormStatus')

```TypeScript
function on(type: 'getLiveFormStatus',  callback: formInfo.GetLiveFormStatusCallback): void
```

Listens to the event of get live form status.

**Since:** 20

<!--Device-formHost-function on(type: 'getLiveFormStatus',  callback: formInfo.GetLiveFormStatusCallback): void--><!--Device-formHost-function on(type: 'getLiveFormStatus',  callback: formInfo.GetLiveFormStatusCallback): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'getLiveFormStatus' | Yes |
| callback | formInfo.GetLiveFormStatusCallback | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
