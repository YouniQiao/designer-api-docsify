# mmapSync

## mmapSync

```TypeScript
declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping
```

以同步方法基于文件描述符或文件对象创建文件映射对象。将文件内容映射到内存，以实现文件的高效读写访问。注意：读写模式（MappingMode.READ_WRITE）下，若映射范围超过原始文件大小，将自动扩展文件大小。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping--><!--Device-unnamed-declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [file](arkts-corefile-storagestatistics-storagestats-i-sys.md) | number \| [File](arkts-corefile-file-fs-file-i.md) | 是 |
| mode | [MappingMode](arkts-corefile-file-fs-mappingmode-e.md) | 是 |
| offset | number | 是 |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| [FileMapping](arkts-corefile-file-fs-filemapping-i.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900021 |
| 13900023 |
| 13900017 |
| 13900050 |
| 13900024 |
| 13900056 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900001 |
| 13900012 |
| 13900015 |
| 13900008 |
| 13900010 |
| 13900011 |
