# mkdtemp

## mkdtemp

```TypeScript
declare function mkdtemp(prefix: string): Promise<string>
```

创建临时目录，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:mkdtemp](arkts-corefile-fileio-mkdtemp-f.md#mkdtemp)

<!--Device-unnamed-declare function mkdtemp(prefix: string): Promise<string>--><!--Device-unnamed-declare function mkdtemp(prefix: string): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |


## mkdtemp

```TypeScript
declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void
```

创建临时目录，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [@ohos.file.fs:mkdtemp](arkts-corefile-fileio-mkdtemp-f.md#mkdtemp)

<!--Device-unnamed-declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void--><!--Device-unnamed-declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |
