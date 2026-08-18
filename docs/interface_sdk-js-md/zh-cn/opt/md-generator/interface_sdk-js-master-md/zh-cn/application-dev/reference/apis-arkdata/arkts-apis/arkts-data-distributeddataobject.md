# @ohos.data.distributedDataObject

本模块提供管理基本数据对象的相关能力，包括创建、查询、删除、修改、订阅等；同时支持相同应用多设备间的分布式数据对象协同能力。分布式数据对象处理数据时，不会解析用户数据的内容，存储路径安全性较低，不建议传输个人敏感数据和隐私数据。

**起始版本：** 23

<!--Device-unnamed-declare namespace distributedDataObject--><!--Device-unnamed-declare namespace distributedDataObject-End-->

**系统能力：** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [create](arkts-arkdata-distributeddataobject-create-f.md#create) |
| [createDistributedObject](arkts-arkdata-distributeddataobject-createdistributedobject-f.md#createdistributedobject) |
| [genSessionId](arkts-arkdata-distributeddataobject-gensessionid-f.md#gensessionid) |

### 接口

| 名称 |
| --- |
| [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) |
| [DataObject](arkts-arkdata-distributeddataobject-dataobject-i.md) |
| [DistributedObject](arkts-arkdata-distributeddataobject-distributedobject-i.md) |
| [RevokeSaveSuccessResponse](arkts-arkdata-distributeddataobject-revokesavesuccessresponse-i.md) |
| [SaveSuccessResponse](arkts-arkdata-distributeddataobject-savesuccessresponse-i.md) |

### 类型

| 名称 |
| --- |
| [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) |
| [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) |
| [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) |
