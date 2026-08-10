# upload

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## upload

```TypeScript
function upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void
```

创建并启动一个上传任务，使用callback异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [request.uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile)(context:

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the FA model.

<!--Device-request-function upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void--><!--Device-request-function upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void-End-->

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | Yes | 上传的配置信息。 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;UploadTask&gt; | Yes | 回调函数，异步返回UploadTask对象。当上传成功，err为undefined，data为获取到的UploadTask对象；否则为 错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | The permissions check fails. |

## Examples

```TypeScript
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // Replace the URL with the HTTP address of the real server.
  header: { 'Accept': '*/*' },
  method: "POST",
  files: [{ filename: "test", name: "test", uri: "internal://cache/test.jpg", type: "image/jpeg" }], // Set type to the MIME type specified by the HTTP.
  data: [{ name: "name123", value: "123" }],
};
request.upload(uploadConfig, (err: BusinessError, data: request.UploadTask) => {
  if (err) {
    console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  uploadTask = data;
});
```


## upload

```TypeScript
function upload(config: UploadConfig): Promise<UploadTask>
```

创建并启动一个上传任务，使用Promise异步回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [request.uploadFile](arkts-basicservices-request-uploadfile-f.md#uploadfile)(context:

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the FA model.

<!--Device-request-function upload(config: UploadConfig): Promise<UploadTask>--><!--Device-request-function upload(config: UploadConfig): Promise<UploadTask>-End-->

**System capability:** SystemCapability.MiscServices.Upload

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | Yes | 上传的配置信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;UploadTask&gt; | 使用Promise方式，异步返回上传任务UploadTask的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | The permissions check fails. |

## Examples

```TypeScript
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // Replace the URL with the HTTP address of the real server.
  header: { 'Accept': '*/*' },
  method: "POST",
  files: [{ filename: "test", name: "test", uri: "internal://cache/test.jpg", type: "image/jpeg" }], // Set type to the MIME type specified by the HTTP.
  data: [{ name: "name123", value: "123" }],
};
request.upload(uploadConfig).then((data: request.UploadTask) => {
  uploadTask = data;
}).catch((err: BusinessError) => {
  console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
})
```

