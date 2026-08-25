# symlink

## 导入模块

```TypeScript
```

## symlink

```TypeScript
declare function symlink(target: string, srcPath: string): Promise<void>
```

基于文件路径创建符号链接，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [symlink](arkts-corefile-file-fs-symlink-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | string | 是 |
| srcPath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## symlink

```TypeScript
declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void
```

基于文件路径创建符号链接，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [symlink](arkts-corefile-file-fs-symlink-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | string | 是 |
| srcPath | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
