# getFormsInfo (System API)

## Modules to Import

```TypeScript
import { formHost } from '@kit.FormKit';
```

## getFormsInfo

```TypeScript
function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void
```

Obtains the widget information provided by a specified application on the device (excluding template widgets). This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void--><!--Device-formHost-function getFormsInfo(bundleName: string, callback: AsyncCallback<Array<formInfo.FormInfo>>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.FormInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## getFormsInfo

```TypeScript
function getFormsInfo(
    bundleName: string,
    moduleName: string,
    callback: AsyncCallback<Array<formInfo.FormInfo>>
  ): void
```

Obtains the widget information provided by a specified application on the device (excluding template widgets). This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(    bundleName: string,    moduleName: string,    callback: AsyncCallback<Array<formInfo.FormInfo>>  ): void--><!--Device-formHost-function getFormsInfo(    bundleName: string,    moduleName: string,    callback: AsyncCallback<Array<formInfo.FormInfo>>  ): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.FormInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## getFormsInfo

```TypeScript
function getFormsInfo(bundleName: string, moduleName?: string): Promise<Array<formInfo.FormInfo>>
```

Obtains the widget information provided by a specified application on the device (excluding template widgets). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(bundleName: string, moduleName?: string): Promise<Array<formInfo.FormInfo>>--><!--Device-formHost-function getFormsInfo(bundleName: string, moduleName?: string): Promise<Array<formInfo.FormInfo>>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;formInfo.FormInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |


## getFormsInfo

```TypeScript
function getFormsInfo(filter: formInfo.FormInfoFilter): Promise<Array<formInfo.FormInfo>>
```

Obtains the widget information provided by a specified application on the device (excluding template widgets). This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-formHost-function getFormsInfo(filter: formInfo.FormInfoFilter): Promise<Array<formInfo.FormInfo>>--><!--Device-formHost-function getFormsInfo(filter: formInfo.FormInfoFilter): Promise<Array<formInfo.FormInfo>>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filter | formInfo.FormInfoFilter | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;formInfo.FormInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
