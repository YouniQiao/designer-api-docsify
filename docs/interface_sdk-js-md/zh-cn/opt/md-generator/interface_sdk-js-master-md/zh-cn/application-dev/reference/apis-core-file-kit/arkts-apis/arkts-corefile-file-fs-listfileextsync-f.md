# listFileExtSync

## listFileExtSync

```TypeScript
declare function listFileExtSync(
  path: string,
  options?: ListFileExtOptions
): string[]
```

以同步方法列出目录下所有文件名，支持通过自定义过滤函数对文件名进行过滤。 可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare function listFileExtSync(  path: string,  options?: ListFileExtOptions): string[]--><!--Device-unnamed-declare function listFileExtSync(  path: string,  options?: ListFileExtOptions): string[]-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| options | [ListFileExtOptions](arkts-corefile-file-fs-listfileextoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string[] |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900002 |
| 13900018 |
| 13900011 |
