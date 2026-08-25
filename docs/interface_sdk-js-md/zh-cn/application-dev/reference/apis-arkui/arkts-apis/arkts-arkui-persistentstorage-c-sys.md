# PersistentStorage

PersistentStorage提供了UI状态的持久化存储能力，将选定的AppStorage属性持久化到文件中，在应用重启时从文件中恢复这些属性值并写入到AppStorage。具体UI使用说明，详见 [PersistentStorage：持久化存储UI状态](../../../ui/state-management/arkts-persiststorage.md)。

> **说明：**&gt;
> 从API version 12开始，PersistentStorage支持null、undefined。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(appStorage: AppStorage, storage: Storage)
```

构造函数。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [appStorage](arkts-arkui-commontsetsapi-p-sys.md) | [AppStorage](arkts-arkui-appstorage-c.md) | 是 |
| storage | [Storage](../../apis-arkdata/arkts-apis/arkts-arkdata-system-storage-storage-c.md) | 是 |
