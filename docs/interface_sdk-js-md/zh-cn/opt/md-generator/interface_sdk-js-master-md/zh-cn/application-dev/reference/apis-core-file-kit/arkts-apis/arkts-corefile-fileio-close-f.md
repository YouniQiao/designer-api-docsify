# close

## close

```TypeScript
declare function close(fd: number): Promise<void>
```

关闭文件，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:close](arkts-corefile-fileio-close-f.md#close)

<!--Device-unnamed-declare function close(fd: number): Promise<void>--><!--Device-unnamed-declare function close(fd: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |


## close

```TypeScript
declare function close(fd: number, callback: AsyncCallback<void>): void
```

关闭文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:close](arkts-corefile-fileio-close-f.md#close)

<!--Device-unnamed-declare function close(fd: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function close(fd: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
