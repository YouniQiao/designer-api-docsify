# access

## access

```TypeScript
declare function access(path: string, mode?: number): Promise<void>
```

检查当前进程是否可访问某文件，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [access](arkts-corefile-file-fs-access-f.md#access)

<!--Device-unnamed-declare function access(path: string, mode?: number): Promise<void>--><!--Device-unnamed-declare function access(path: string, mode?: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## access

```TypeScript
declare function access(path: string, callback: AsyncCallback<void>): void
```

检查当前进程是否可访问某文件，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [access](arkts-corefile-file-fs-access-f.md#access)

<!--Device-unnamed-declare function access(path: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function access(path: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## access

```TypeScript
declare function access(path: string, mode: number, callback: AsyncCallback<void>): void
```

检查当前进程是否可访问某文件，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [access](arkts-corefile-file-fs-access-f.md#access)

<!--Device-unnamed-declare function access(path: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function access(path: string, mode: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
