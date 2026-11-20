# VirtualFileOnCancel

```TypeScript
type VirtualFileOnCancel = (idList: Array<string>) => Promise<void>
```

用于取消指定虚拟文件的操作。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.1.0开始，该接口支持在原子化服务中使用。

<!--Device-pasteboard-type VirtualFileOnCancel = (idList: Array<string>) => Promise<void>--><!--Device-pasteboard-type VirtualFileOnCancel = (idList: Array<string>) => Promise<void>-End-->

**系统能力：** SystemCapability.MiscServices.Pasteboard

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| idList | Array&lt;string&gt; | 是 | 包含待取消的虚拟文件的文件唯一标识的列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |
