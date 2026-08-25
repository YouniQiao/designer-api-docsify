# @ohos.data.distributedDataObject(分布式数据对象)

本模块提供管理基本数据对象的相关能力，包括创建、查询、删除、修改、订阅等；同时支持相同应用多设备间的分布式数据对象协同能力。分布式数据对象处理数据时，不会解析用户数据的内容，存储路径安全性较低，不建议传输个人敏感数据和隐私数据。

**起始版本：** 8

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## 导入模块

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## 汇总

### 函数

| 名称 |
| --- |
| [create(分布式数据对象)](arkts-arkdata-distributeddataobject-create-f.md) |
| [createDistributedObject(分布式数据对象)](arkts-arkdata-distributeddataobject-createdistributedobject-f.md) |
| [genSessionId(分布式数据对象)](arkts-arkdata-distributeddataobject-gensessionid-f.md) |

### 接口

| 名称 |
| --- |
| [BindInfo(分布式数据对象)](arkts-arkdata-distributeddataobject-bindinfo-i.md) |
| [DataObject(分布式数据对象)](arkts-arkdata-distributeddataobject-dataobject-i.md) |
| [DistributedObject(分布式数据对象)](arkts-arkdata-distributeddataobject-distributedobject-i.md) |
| [RevokeSaveSuccessResponse(分布式数据对象)](arkts-arkdata-distributeddataobject-revokesavesuccessresponse-i.md) |
| [SaveSuccessResponse(分布式数据对象)](arkts-arkdata-distributeddataobject-savesuccessresponse-i.md) |

### 类型

| 名称 |
| --- |
| [DataObserver(分布式数据对象)](arkts-arkdata-distributeddataobject-dataobserver-t.md) |
| [ProgressObserver(分布式数据对象)](arkts-arkdata-distributeddataobject-progressobserver-t.md) |
| [StatusObserver(分布式数据对象)](arkts-arkdata-distributeddataobject-statusobserver-t.md) |
