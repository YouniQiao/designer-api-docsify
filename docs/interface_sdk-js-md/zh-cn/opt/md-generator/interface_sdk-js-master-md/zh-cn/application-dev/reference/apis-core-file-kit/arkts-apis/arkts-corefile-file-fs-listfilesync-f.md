# listFileSync

## listFileSync

```TypeScript
declare function listFileSync(
  path: string,
  options?: ListFileOptions
): string[]
```

默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。 可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**起始版本：** 9

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function listFileSync(  path: string,  options?: ListFileOptions): string[]--><!--Device-unnamed-declare function listFileSync(  path: string,  options?: ListFileOptions): string[]-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| options | [ListFileOptions](arkts-corefile-file-fs-listfileoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string[] |

**错误码：**

| 错误码ID |
| --- |
| 13900002 |
| 13900018 |
| 13900008 |
| 13900042 |
| 13900011 |
