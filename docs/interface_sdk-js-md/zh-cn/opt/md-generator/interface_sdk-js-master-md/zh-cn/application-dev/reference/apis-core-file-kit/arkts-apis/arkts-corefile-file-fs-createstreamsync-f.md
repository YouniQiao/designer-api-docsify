# createStreamSync

## 导入模块

```TypeScript
```

## createStreamSync

```TypeScript
declare function createStreamSync(path: string, mode: string): Stream
```

以同步方法基于文件路径创建文件流。需要配合[Stream](arkts-corefile-file-fs-stream-i.md#stream)中的close()函数关闭文件流。

**起始版本：** 9

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function createStreamSync(path: string, mode: string): Stream--><!--Device-unnamed-declare function createStreamSync(path: string, mode: string): Stream-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Stream](arkts-corefile-file-fs-stream-i.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900038 |
| 13900033 |
| 13900034 |
| 13900044 |
| 13900041 |
| 13900042 |
| 13900020 |
| 13900022 |
| 13900023 |
| 13900017 |
| 13900018 |
| 13900019 |
| 13900029 |
| 13900030 |
| 13900024 |
| 13900025 |
| 13900027 |
| 13900004 |
| 13900006 |
| 13900001 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900011 |
