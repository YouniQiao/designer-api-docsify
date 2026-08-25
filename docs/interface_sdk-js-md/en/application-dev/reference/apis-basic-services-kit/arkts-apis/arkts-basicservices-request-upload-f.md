# upload

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## upload

```TypeScript
function upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void
```

Uploads a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [uploadFile](arkts-basicservices-request-uploadfile-f.md)(context: BaseContext, config: UploadConfig)

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[UploadTask](arkts-basicservices-request-uploadtask-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |


## upload

```TypeScript
function upload(config: UploadConfig): Promise<UploadTask>
```

Uploads a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [uploadFile](arkts-basicservices-request-uploadfile-f.md)(context: BaseContext, config: UploadConfig)

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[UploadTask](arkts-basicservices-request-uploadtask-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
