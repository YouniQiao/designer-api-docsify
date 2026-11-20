# VirtualFileOnStat

```TypeScript
type VirtualFileOnStat = (id: string) => Promise<VirtualFileItem>
```

用于查询指定虚拟文件的元数据。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-pasteboard-type VirtualFileOnStat = (id: string) => Promise<VirtualFileItem>--><!--Device-pasteboard-type VirtualFileOnStat = (id: string) => Promise<VirtualFileItem>-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 待查询的虚拟文件的文件唯一标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[VirtualFileItem](arkts-basicservices-pasteboard-virtualfileitem-c.md)&gt; | Promise对象，返回虚拟文件的元数据对象。 |
