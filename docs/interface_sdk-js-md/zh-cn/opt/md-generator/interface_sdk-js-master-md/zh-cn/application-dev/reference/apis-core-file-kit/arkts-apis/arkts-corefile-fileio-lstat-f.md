# lstat

## 导入模块

```TypeScript
```

## lstat

```TypeScript
declare function lstat(path: string): Promise<Stat>
```

获取链接信息，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [lstat](arkts-corefile-file-fs-lstat-f.md#lstat)

<!--Device-unnamed-declare function lstat(path: string): Promise<Stat>--><!--Device-unnamed-declare function lstat(path: string): Promise<Stat>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Stat](arkts-corefile-fileio-stat-depr-i.md)&gt; |


## lstat

```TypeScript
declare function lstat(path: string, callback: AsyncCallback<Stat>): void
```

获取链接信息，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [lstat](arkts-corefile-file-fs-lstat-f.md#lstat)

<!--Device-unnamed-declare function lstat(path: string, callback: AsyncCallback<Stat>): void--><!--Device-unnamed-declare function lstat(path: string, callback: AsyncCallback<Stat>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stat](arkts-corefile-fileio-stat-depr-i.md)&gt; | 是 |
