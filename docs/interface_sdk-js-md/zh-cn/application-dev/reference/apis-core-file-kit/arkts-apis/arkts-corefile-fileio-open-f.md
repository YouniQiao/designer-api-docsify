# open

## 导入模块

```TypeScript
```

## open

```TypeScript
declare function open(path: string, flags?: number, mode?: number): Promise<number>
```

打开文件，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [open](arkts-corefile-file-fs-open-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| flags | number | 否 |
| mode | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |


## open

```TypeScript
declare function open(path: string, callback: AsyncCallback<number>): void
```

打开文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [open](arkts-corefile-file-fs-open-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## open

```TypeScript
declare function open(path: string, flags: number, callback: AsyncCallback<number>): void
```

打开文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [open](arkts-corefile-file-fs-open-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| flags | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## open

```TypeScript
declare function open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void
```

打开文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [open](arkts-corefile-file-fs-open-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| flags | number | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |
