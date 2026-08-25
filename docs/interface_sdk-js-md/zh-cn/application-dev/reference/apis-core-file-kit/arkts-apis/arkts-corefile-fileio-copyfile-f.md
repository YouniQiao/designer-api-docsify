# copyFile

## 导入模块

```TypeScript
```

## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>
```

复制文件，使用Promise异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string \| number | 是 |
| dest | string \| number | 是 |
| mode | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void
```

copyFile.

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string \| number | 是 |
| dest | string \| number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## copyFile

```TypeScript
declare function copyFile(
  src: string | number,
  dest: string | number,
  mode: number,
  callback: AsyncCallback<void>
): void
```

复制文件，使用callback异步回调。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string \| number | 是 |
| dest | string \| number | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
