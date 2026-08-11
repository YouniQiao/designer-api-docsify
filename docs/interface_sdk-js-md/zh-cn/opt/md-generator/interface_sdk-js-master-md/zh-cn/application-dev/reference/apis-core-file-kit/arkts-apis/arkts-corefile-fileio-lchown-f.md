# lchown

## lchown

```TypeScript
declare function lchown(path: string, uid: number, gid: number): Promise<void>
```

基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是符号链接所指向的实际文件，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

<!--Device-unnamed-declare function lchown(path: string, uid: number, gid: number): Promise<void>--><!--Device-unnamed-declare function lchown(path: string, uid: number, gid: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| uid | number | 是 |
| gid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |


## lchown

```TypeScript
declare function lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void
```

基于文件路径改变文件所有者，更改符号链接本身的所有者，而不是更改符号链接所指向的实际文件，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

<!--Device-unnamed-declare function lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| uid | number | 是 |
| gid | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
