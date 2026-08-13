# hash

## hash

```TypeScript
declare function hash(path: string, algorithm: string): Promise<string>
```

计算文件的哈希值，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [hash](arkts-file-hash.md#@ohos.file.hash)

<!--Device-unnamed-declare function hash(path: string, algorithm: string): Promise<string>--><!--Device-unnamed-declare function hash(path: string, algorithm: string): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |


## hash

```TypeScript
declare function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void
```

计算文件的哈希值，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [hash](arkts-file-hash.md#@ohos.file.hash)

<!--Device-unnamed-declare function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |
