# hiAppEvent(应用事件打点)

本模块提供了应用事件打点能力，包括对打点数据的落盘，以及对打点功能的管理配置。

> **说明：**&gt;
> - 本模块接口从API version 9开始废弃，建议使用新接口[@ohos.hiviewdfx.hiAppEvent](arkts-performanceanalysis-hiappevent-n.md)替代。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** hiAppEvent

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

## 导入模块

```TypeScript
```

## 汇总

### 命名空间

| 名称 |
| --- |
| [Event(应用事件打点)](arkts-performanceanalysis-hiappevent-event-depr-n.md) | 此接口提供了所有预定义事件的事件名称常量。  \| 名称 \| 类型 \| 可读 \| 可写 \| 说明 \| \| ------------------------- \| ------ \| ---- \| ---- \| -------------------- \| \| USER_LOGIN \| string \| 是 \| 否 \| 用户登录事件。 \| \| USER_LOGOUT \| string \| 是 \| 否 \| 用户登出事件。 \| \| DISTRIBUTED_SERVICE_START \| string \| 是 \| 否 \| 分布式服务启动事件。 \|
| [Param(应用事件打点)](arkts-performanceanalysis-hiappevent-param-depr-n.md) | 此接口提供了所有预定义参数的参数名称常量。  \| 名称 \| 类型 \| 可读 \| 可写 \| 说明 \| \| ------------------------------- \| ------ \| ---- \| ---- \| ------------------ \| \| USER_ID \| string \| 是 \| 否 \| 用户自定义ID。 \| \| DISTRIBUTED_SERVICE_NAME \| string \| 是 \| 否 \| 分布式服务名称。 \| \| DISTRIBUTED_SERVICE_INSTANCE_ID \| string \| 是 \| 否 \| 分布式服务实例ID。 \|

### 函数

| 名称 |
| --- |
| [write(应用事件打点)](arkts-performanceanalysis-hiappevent-write-depr-f.md#write) |
| [write(应用事件打点)](arkts-performanceanalysis-hiappevent-write-depr-f.md#write) |
| [configure(应用事件打点)](arkts-performanceanalysis-hiappevent-configure-depr-f.md#configure) |

### 接口

| 名称 |
| --- |
| [ConfigOption(应用事件打点)](arkts-performanceanalysis-hiappevent-configoption-depr-i.md) |

### 枚举

| 名称 |
| --- |
| [EventType(应用事件打点)](arkts-performanceanalysis-hiappevent-eventtype-depr-e.md) |
