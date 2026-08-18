# readSync

## 导入模块

```TypeScript
```

## readSync

```TypeScript
declare function readSync(
  fd: number,
  buffer: ArrayBuffer,
  options?: ReadOptions
): number
```

以同步方法从文件读取数据。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: ReadOptions): number--><!--Device-unnamed-declare function readSync(  fd: number,  buffer: ArrayBuffer,  options?: ReadOptions): number-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| buffer | ArrayBuffer | 是 |
| options | [ReadOptions](arkts-corefile-file-fs-readoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| 13900004 |
| 13900020 |
| 13900005 |
| 13900034 |
| 13900019 |
| 13900044 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |
