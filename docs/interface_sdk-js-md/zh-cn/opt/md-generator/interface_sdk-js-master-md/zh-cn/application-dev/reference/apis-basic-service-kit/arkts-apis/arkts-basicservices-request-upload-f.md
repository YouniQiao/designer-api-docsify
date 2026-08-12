# upload

## upload

```TypeScript
function upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void
```

创建并启动一个上传任务，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [uploadFile](request.uploadFile(context:)

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-request-function upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void--><!--Device-request-function upload(config: UploadConfig, callback: AsyncCallback<UploadTask>): void-End-->

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[UploadTask](arkts-basicservices-request-uploadtask-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // 需要手动将url替换为真实服务器的HTTP协议地址
  header: { 'Accept': '*/*' },
  method: 'POST',
  files: [{ filename: 'test', name: 'test', uri: 'internal://cache/test.jpg', type: 'image/jpeg' }], // 建议type填写HTTP协议规范的MIME类型
  data: [{ name: 'name123', value: '123' }],
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

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [uploadFile](request.uploadFile(context:)

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-request-function upload(config: UploadConfig): Promise<UploadTask>--><!--Device-request-function upload(config: UploadConfig): Promise<UploadTask>-End-->

**系统能力：** SystemCapability.MiscServices.Upload

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [UploadConfig](arkts-basicservices-request-uploadconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[UploadTask](arkts-basicservices-request-uploadtask-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
let uploadTask: request.UploadTask;
let uploadConfig: request.UploadConfig = {
  url: 'http://www.example.com', // 需要手动将url替换为真实服务器的HTTP协议地址
  header: { 'Accept': '*/*' },
  method: 'POST',
  files: [{ filename: 'test', name: 'test', uri: 'internal://cache/test.jpg', type: 'image/jpeg' }], // 建议type填写HTTP协议规范的MIME类型
  data: [{ name: 'name123', value: '123' }],
};
request.upload(uploadConfig).then((data: request.UploadTask) => {
  uploadTask = data;
}).catch((err: BusinessError) => {
  console.error(`Failed to request the upload. Code: ${err.code}, message: ${err.message}`);
});
```
