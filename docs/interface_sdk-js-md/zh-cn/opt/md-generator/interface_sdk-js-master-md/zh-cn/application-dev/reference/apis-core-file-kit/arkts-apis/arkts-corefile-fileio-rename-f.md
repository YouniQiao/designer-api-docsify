# rename

## rename

```TypeScript
declare function rename(oldPath: string, newPath: string): Promise<void>
```

重命名文件，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:rename](arkts-corefile-fileio-rename-f.md#rename)

<!--Device-unnamed-declare function rename(oldPath: string, newPath: string): Promise<void>--><!--Device-unnamed-declare function rename(oldPath: string, newPath: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldPath | string | 是 |
| newPath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |


## rename

```TypeScript
declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void
```

重命名文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:rename](arkts-corefile-fileio-rename-f.md#rename)

<!--Device-unnamed-declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldPath | string | 是 |
| newPath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
