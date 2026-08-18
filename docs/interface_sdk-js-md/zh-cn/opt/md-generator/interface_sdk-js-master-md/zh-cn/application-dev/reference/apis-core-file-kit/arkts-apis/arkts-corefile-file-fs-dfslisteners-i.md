# DfsListeners

事件监听类。创建DFSListener对象，用于监听分布式文件系统状态。

**起始版本：** 12

<!--Device-unnamed-export interface DfsListeners--><!--Device-unnamed-export interface DfsListeners-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

## 导入模块

```TypeScript
```

## onStatus

```TypeScript
onStatus(networkId: string, status: number): void
```

事件回调类。参数由[connectDfs](arkts-corefile-file-fs-connectdfs-f.md#connectdfs)传入。

**起始版本：** 12

<!--Device-DfsListeners-onStatus(networkId: string, status: number): void--><!--Device-DfsListeners-onStatus(networkId: string, status: number): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |
| status | number | 是 |
