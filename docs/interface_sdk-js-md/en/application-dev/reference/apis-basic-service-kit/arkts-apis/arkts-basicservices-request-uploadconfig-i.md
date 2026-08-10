# UploadConfig

上传任务的配置信息。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-request-interface UploadConfig--><!--Device-request-interface UploadConfig-End-->

**System capability:** SystemCapability.MiscServices.Upload

## Modules to Import

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## begins

```TypeScript
begins?: long
```

上传任务开始时读取的文件起点，单位为字节（B）。默认值为0，取值范围为闭区间，表示从头开始传输。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-UploadConfig-begins?: long--><!--Device-UploadConfig-begins?: long-End-->

**System capability:** SystemCapability.MiscServices.Upload

## data

```TypeScript
data: Array<RequestData>
```

请求的表单数据。

**Type:** Array&lt;RequestData&gt;

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-UploadConfig-data: Array<RequestData>--><!--Device-UploadConfig-data: Array<RequestData>-End-->

**System capability:** SystemCapability.MiscServices.Upload

## ends

```TypeScript
ends?: long
```

上传任务结束时读取的文件终点，单位为字节（B）。默认值为-1，取值范围为闭区间，表示传输到整个文件末尾结束。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-UploadConfig-ends?: long--><!--Device-UploadConfig-ends?: long-End-->

**System capability:** SystemCapability.MiscServices.Upload

## files

```TypeScript
files: Array<File>
```

要上传的文件列表。文件以HTTP的multipart/form-data格式提交。

**Type:** Array&lt;File&gt;

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-UploadConfig-files: Array<File>--><!--Device-UploadConfig-files: Array<File>-End-->

**System capability:** SystemCapability.MiscServices.Upload

## header

```TypeScript
header: Object
```

添加要包含在上传请求中的HTTP或HTTPS标志头。

**Type:** Object

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-UploadConfig-header: Object--><!--Device-UploadConfig-header: Object-End-->

**System capability:** SystemCapability.MiscServices.Upload

## index

```TypeScript
index?: int
```

任务的路径索引，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-UploadConfig-index?: int--><!--Device-UploadConfig-index?: int-End-->

**System capability:** SystemCapability.MiscServices.Upload

## method

```TypeScript
method: string
```

HTTP请求方法：POST、PUT，缺省为POST。使用POST新增资源，使用PUT修改资源。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-UploadConfig-method: string--><!--Device-UploadConfig-method: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

## url

```TypeScript
url: string
```

资源地址。从API 6到API 14，最大长度为2048个字符；从API 15开始，最大长度为8192个字符。支持  
[HTTP拦截](../../../basic-services/request/app-file-upload-download.md#http拦截)功能。

**Type:** string

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-UploadConfig-url: string--><!--Device-UploadConfig-url: string-End-->

**System capability:** SystemCapability.MiscServices.Upload

