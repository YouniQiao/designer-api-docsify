# VirtualFileOnRead

```TypeScript
type VirtualFileOnRead = (id: string, offset: number, length: number) => Promise<Uint8Array>
```

用于查询指定虚拟文件的文件内容。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-pasteboard-type VirtualFileOnRead = (id: string, offset: long, length: int) => Promise<Uint8Array>--><!--Device-pasteboard-type VirtualFileOnRead = (id: string, offset: long, length: int) => Promise<Uint8Array>-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 待查询的虚拟文件的文件唯一标识。 |
| offset | number | 是 | 查询的虚拟文件内容的起始位置（单位：字节）。 |
| length | number | 是 | 查询的虚拟文件内容的数据长度（单位：字节）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Uint8Array&gt; | Promise对象，返回从offset开始，长度为length的虚拟文件数据。 |
